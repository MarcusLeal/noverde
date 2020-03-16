import logging

from sqlalchemy import or_

from cp.app import db
from cp.application_layer.persistency.tables import loan_table
from cp.domain_layer.models.loan import Loan
from cp.domain_layer.ports.loan import LoanRepository

logger = logging.getLogger("flask.app."+__name__)


class SQLAlchemyLoanRepository(LoanRepository):
    """
    I am the Loan repository that uses postgres as the storage mechanism
    """

    @classmethod
    def filter_loan(
            cls, *, id: str = None, cpf: str = None) -> Loan:

        try:
            logger.info(
                "Getting Loan",
                extra={
                    "props": {
                        "service": "PostgreSQL",
                        "service method": "filter",
                        "loan_id": str(id),
                        "cpf": cpf
                    }
                })
            loan = db.session.query(loan_table).filter(or_(
                loan_table.c.id == id, loan_table.c.cpf == cpf)).first()
        except Exception as e:
            logger.exception(
                "Error while trying to get Loan",
                extra={
                    "props": {
                        "service": "PostgreSQL",
                        "service method": "filter",
                        "loan_id": str(id),
                        "cpf": cpf,
                        "error message": str(e)
                    }
                })
            db.session.rollback()
            raise e

        if loan:
            return Loan(
                name=loan.name,
                cpf=loan.cpf,
                birthdate=loan.birthdate,
                amount=loan.amount,
                terms=loan.terms,
                income=loan.income,
                id=loan.id)
        else:
            return None

    @classmethod
    def insert_loan(
            cls, name: str, cpf: str, birthdate: str,
            amount: float, terms: int, income: float) -> Loan:

        try:
            logger.info(
                "Persisting Loan",
                extra={
                    "props": {
                        "service": "PostgreSQL",
                        "service method": "insert",
                        "loan_name": name,
                        "loan_cpf": cpf,
                        "loan_amount": amount
                    }
                })
            loan = loan_table.insert().values(
                name=name,
                cpf=cpf,
                birthdate=birthdate,
                amount=amount,
                terms=terms,
                income=income)

            cursor = db.session.execute(loan)
            db.session.commit()
            loan_id = cursor.inserted_primary_key[0]

            return cls.filter_loan(id=loan_id)

        except Exception as e:
            logger.exception(
                "Error while trying to persist Loan",
                extra={
                    "props": {
                        "service": "PostgreSQL",
                        "service method": "insert",
                        "loan_name": name,
                        "loan_cpf": cpf,
                        "loan_amount": amount,
                        "error message": str(e)
                    }
                })
            db.session.rollback()
            raise e
