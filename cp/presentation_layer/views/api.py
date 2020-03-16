import logging
from json import loads

from flask import Blueprint, jsonify, request
from flask_restplus import Api, Resource, marshal

from cp.application_layer.use_cases.loan import LoanUseCase
from cp.presentation_layer.mappings import LoanMapping
from cp.presentation_layer.views.schemas import loan_model
from lutils.decorators import requires_fields_validation, requires_json

VERSION = '1.0'
DOC = 'CHALLENGE API'

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          version=VERSION,
          title='CHALLENGE API',
          description=DOC,
          doc='/docs/swagger',
          authorizations={
              'x-api-key': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'x-api-key'
              },
              'Token': {
                  'type': 'apiKey',
                  'in': 'header',
                  'name': 'Authorization'
              }
          })

ns = api.namespace('', description='CHALLENGE E-commerce endpoints')

api.models[loan_model.name] = loan_model

logger = logging.getLogger("flask.app."+__name__)


@ns.route('/', doc=False)
class Index(Resource):
    def get(self):
        return dict(
            service='Noverde - Challenge API',
            version=VERSION)


@ns.route('/loan')
@ns.route('/loan/<string:id>')
class Loan(Resource):
    @ns.response(200, 'OK')
    def get(self, id):
        return jsonify({"message": "OK"})

    @requires_json
    @requires_fields_validation
    @ns.response(200, 'OK')
    @ns.expect(loan_model)
    def post(self):
        payload = loads(request.data)

        logger.info(
            "Apply for loan",
            extra={
                "props": {
                    "request": "/api/loan",
                    "method": "POST",
                    "data": payload,
                }
            })

        mapping = LoanMapping(payload=payload)

        loan = LoanUseCase.request_loan(loan_data=mapping)
        return jsonify({'id': loan.id})
