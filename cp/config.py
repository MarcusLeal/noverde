import logging
import os
from json import loads


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    DEPLOY_ENV = os.environ.get('DEPLOY_ENV', 'Development')
    LOGS_LEVEL = logging.INFO
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    RESTPLUS_VALIDATE = True

    # Config credit-engine
    CREDIT_ANALISES_ENGINE_URI = os.environ.get(
        'CREDIT_ANALISES_ENGINE_URI')
    CREDIT_ANALISES_ENGINE_TOKEN = os.environ.get(
        'CREDIT_ANALISES_ENGINE_TOKEN')
    CREDIT_ANALISES_PARAMETERS = os.environ.get(
        'CREDIT_ANALISES_PARAMETERS', {
            "age_assessment": {'min_age': 18},
            "credit_score_assessment": {"min_credit_score": 600}})


class TestingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI_TEST')


class StagingConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    LOGS_LEVEL = logging.CRITICAL


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    LOGS_LEVEL = int(os.environ.get('LOGS_LEVEL', logging.ERROR))
