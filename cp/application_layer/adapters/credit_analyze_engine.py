import logging

import requests
from flask import current_app

from cp.domain_layer.ports.analysis import CreditAnalisesService

logger = logging.getLogger("flask.app."+__name__)


class CreditAnalysis(CreditAnalisesService):

    @classmethod
    def request_analysis_score(cls, loan: 'Loan'):

        url = f'{current_app.config["CREDIT_ANALISES_ENGINE_URI"]}/score'

        headers = {
            'content-type': 'application/json',
            'x-api-key': current_app.config["CREDIT_ANALISES_ENGINE_TOKEN"]
        }

        data = {"cpf": loan.cpf}

        logger.info(
            "Sending analysis request to credit analyses engine",
            extra={
                "props": {
                    "service": "credit analyse engine",
                    "url": url,
                    "method": "POST",
                    "headers": headers,
                    "cpf": loan.cpf,
                }
            })
        return {"score": 600}
        # response = requests.post(url, headers=headers, json=data)

        # logger.info(
        #     "Credit analyses engine request received",
        #     extra={
        #         "props": {
        #             "service": "credit analyse engine",
        #             "url": url,
        #             "response_code": response.status_code,
        #             "response_text": response.text
        #         }
        #     })
        # if response.status_code == 200:
        #     response_json = response.json()
        # else:
        #     return None

    @classmethod
    def request_analysis_commitment(cls, loan: 'Loan'):

        url = f'{current_app.config["CREDIT_ANALISES_ENGINE_URI"]}/commitment'

        headers = {
            'content-type': 'application/json',
            'x-api-key': current_app.config["CREDIT_ANALISES_ENGINE_TOKEN"]
        }

        data = {"cpf": loan.cpf}

        logger.info(
            "Sending analysis request to commitment analyses engine",
            extra={
                "props": {
                    "service": "commitment analyse engine",
                    "url": url,
                    "method": "POST",
                    "headers": headers,
                    "cpf": loan.cpf,
                }
            })
        return {"commitment": 0.6}
        # response = requests.post(url, headers=headers, json=data)

        # logger.info(
        #     "Commitment analyses engine request received",
        #     extra={
        #         "props": {
        #             "service": "credit analyse engine",
        #             "url": url,
        #             "response_code": response.status_code,
        #             "response_text": response.text
        #         }
        #     })
        # if response.status_code == 200:
        #     response_json = response.json()
        # else:
        #     return None
