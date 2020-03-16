
from flask import current_app

from cp.application_layer.adapters.loan_repository import \
    SQLAlchemyLoanRepository
from cp.domain_layer.factories import CreditAssessmentProfileFactory
from cp.domain_layer.models.analysis import CreditAssessmentProfile
from cp.domain_layer.models.loan import Loan


class LoanUseCase:
    """
    I am loan use case, called to get information from loan and start credit analysys .
    """
    @classmethod
    def request_loan(cls, loan_data: 'LoanMapping') -> Loan:
        loan = Loan.create_loan(
            name=loan_data.name,
            cpf=loan_data.cpf,
            birthdate=loan_data.birthdate,
            amount=loan_data.amount,
            terms=loan_data.terms,
            income=loan_data.income,
            using_repository=SQLAlchemyLoanRepository)

        credit_assessment_profile = CreditAssessmentProfileFactory(
            assessment_params=current_app.config['CREDIT_ANALISES_PARAMETERS'],
            is_default=True).create_credit_assessment_profile()

        if credit_assessment_profile.assess_credit(loan=loan):
            pass

        return loan
