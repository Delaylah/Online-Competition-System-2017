from . import api
from flask import request, jsonify, render_template


@api.app_errorhandler(404)
def page_not_found(e):
    """ 404 Error response with JSON to web service clients, and with HTML to others. """

    if request.accept_mimetypes.accept_json and not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response

    return render_template('errors/404.html'), 404
