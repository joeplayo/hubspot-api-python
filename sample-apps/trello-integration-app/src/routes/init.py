from os import getenv
from flask import Blueprint, render_template, url_for, redirect
from hubspot.crm.extensions.cards import (
    CardPatchRequest,
    CardFetchBodyPatch,
    CardObjectTypeBody,
    CardActions,
    CardCreateRequest,
    CardDisplayBody,
)
from auth import auth_required
from helpers.hubspot import create_client_with_developer_api_key
from repositories import SettingsRepository

module = Blueprint("init", __name__)


@module.route("/extension", methods=["GET"])
@auth_required
def extension():
    extension_card_id = SettingsRepository.find_one().extension_card_id
    return render_template(
        "init/extension.html",
        extension_card_id=extension_card_id,
        card_title="Trello Integration Test Card",
    )


@module.route("/extension", methods=["POST"])
@auth_required
def create_card():
    hubspot = create_client_with_developer_api_key()
    app_id = getenv("HUBSPOT_APPLICATION_ID")
    deal_object_type = CardObjectTypeBody(
        name="deals", properties_to_send=["hs_object_id", "dealname"],
    )
    fetch = CardFetchBodyPatch(
        target_url=url_for("trello.cards.card_extension_data", _external=True),
        object_types=[deal_object_type],
    )
    actions = CardActions(base_urls=[url_for("home", _external=True)])
    card_id = SettingsRepository.find_one().extension_card_id
    if card_id is None:
        card_title = "Trello Integration Test Card"
        card_create_request = CardCreateRequest(
            title=card_title, fetch=fetch, actions=actions, display=CardDisplayBody()
        )
        response = hubspot.crm.extensions.cards.cards_api.create(
            app_id=app_id, card_create_request=card_create_request,
        )
        SettingsRepository.save_extension_card_id(response.id)
    else:
        card_patch_request = CardPatchRequest(fetch=fetch, actions=actions,)
        hubspot.crm.extensions.cards.cards_api.update(
            app_id=app_id, card_id=card_id, card_patch_request=card_patch_request
        )

    return redirect(url_for("mappings.home"))
