from flask import Blueprint, jsonify
from flask import request

from rest.helpers.decorator import nsq_required  # admin_required, secret_key_required
from rest.controllers import NsqController
bp = Blueprint(__name__, "nsq")

nsqcontroller = NsqController()


@bp.route("/nsq/campaign", methods=["POST"])
@nsq_required()
def get_campaign_nsq_stats_data():

    topic = request.form.get("topic")  # get managix ad id from form ad_id
    wb = request.form.get("response_url")
    channel = request.form.get("channel")

    nsqcontroller.getNsqStats(topic, wb, channel)


@bp.route("/is_alive", methods=["GET"])
def is_alive():

    return jsonify(
        is_alive=True
    )