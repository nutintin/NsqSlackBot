import logging

from flask import Blueprint
from flask import jsonify

from rest.exceptions import RestException

bp = Blueprint(__name__, "error")
log = logging.getLogger(__name__)


@bp.app_errorhandler(RestException)
def handle_rest_exception(e):
	"""This error will show if RestException raised"""
	log.warning(e)
	response = e.to_dict()
	return jsonify(response), e.status_code


@bp.app_errorhandler(404)
def page_not_found(e):
	"""Not found handle"""
	log.warning(e)
	response = {
		"message": "Resource Not exists"
	}
	return jsonify(response), 404


@bp.app_errorhandler(405)
def method_not_allowed(e):
	"""Method not allowed handle"""
	log.warning(e)
	response = {
		"message": "Method not allowed"
	}
	return jsonify(response), 405


@bp.app_errorhandler(500)
def server_error(e):
	"""This error will show if error un handle"""
	log.error(e)
	response = {
		"message": "Internal server error"
	}
	return jsonify(response), 500
