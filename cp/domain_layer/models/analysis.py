from abc import ABC
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import List
from uuid import UUID

from money.money import Money

from cp.application_layer.adapters.credit_analyze_engine import CreditAnalysis
from cp.domain_layer.factories import CreditAssessmentReportCollectionFactory

class CreditRiskEnum(Enum):
    HIGH_RISK = 3
    MEDIUM_RISK = 2
    LOW_RISK = 1


@dataclass
class CreditAssessmentProfile:
    """
    I represent a credit assessment profile that will be used to evaluate the
    client risk based on my assessors and my assessment_params
    """
    is_default: bool
    assessment_params: dict
    assessors: List['CreditAssessor']
    uuid: UUID = None

    def assess_credit(
            self, loan: 'Loan') -> bool:

        credit_reports = [assessor.assess_credit(
            loan=loan,
            **self.assessment_params[CreditAssessorsEnum(assessor).name]
        ) for assessor in self.assessors]

        return CreditRiskEnum(max(credit_report.decision.value
                            for credit_report in credit_reports))


class CreditAssessor(ABC):
    """
    I represent a risk assessment, I know how to assess a risk based on
    parameters and create a CreditReport with my assessment
    """

    @classmethod
    def assess_credit(
            cls,
            loan: 'Loan',
            **params) -> 'CreditReport':
        raise NotImplementedError


class CreditScoreAssessor(CreditAssessor):
    @classmethod
    def assess_credit(
            cls,
            loan: 'Loan',
            min_credit_score: str,
            using_service=CreditAnalysis) -> 'CreditReport':

        response = using_service.request_analysis_score(loan=loan)

        decision = CreditRiskEnum.LOW_RISK \
            if response['score'] <= min_credit_score else CreditRiskEnum.HIGH_RISK

        return CreditScoreReport(decision=decision, score=response['score'])

class CommitmentAssessor(CreditAssessor):
    @classmethod
    def assess_credit(
            cls,
            loan: 'Loan',
            using_service=CreditAnalysis) -> 'CreditReport':

        response = using_service.request_analysis_commitment(loan=loan)

        return CreditScoreReport(decision=decision)


class CreditAgeAssessor(CreditAssessor):
    @classmethod
    def assess_credit(
            cls,
            loan: 'Loan',
            min_age: int) -> 'CreditReport':

        decision = CreditRiskEnum.LOW_RISK \
            if loan.client_age > min_age else CreditRiskEnum.HIGH_RISK

        return CreditAgeReport(decision=decision, score=loan.client_age)


@dataclass
class CreditReport(ABC):
    """
    I represent the report generated by a risk assessor, I know the assessment
    result and the decision made by the assessor
    """
    decision: 'CreditRiskEnum'
    score: [int, str]
    context: dict = None
    uuid: UUID = None

    def as_dict(self):
        return {
            'uuid': str(self.uuid),
            'score': self.score,
            'context': self.context,
            'decision': self.decision}


@dataclass
class CreditScoreReport(CreditReport):
    """
    I know the credit score from client credit analysis
    My score is a string containing only a letter from A to E
    """


@dataclass
class CreditAgeReport(CreditReport):
    """
    I know the fraud score and analyze if client data is trustworthy.
    My score is a integer representing a percentage from 0 to 100.
    """


@dataclass
class RiskAssessmentReportCollection:
    """
    I am the collection of reports generated by the assessors from a
    CreditAssessmentProfile, I know how to persist the reports
    """
    loan: 'Loan'
    credit_report_list: List['CreditReport']
    creation_date: datetime = None
    uuid: UUID = None

    @property
    def decision(self) -> 'CreditRiskEnum':
        return CreditRiskEnum(max(risk_report.decision.value
                            for risk_report in self.credit_report_list))

    @classmethod
    def create_risk_report_collection(
            cls,
            loan: 'Loan',
            credit_report_list: List['CreditReport'],
            using_repository: 'RiskAssessmentReportCollectionRepository',
            with_factory=CreditAssessmentReportCollectionFactory
    ) -> 'CreditAssessmentReportCollection':

        return using_repository.persist_risk_assessment_reports(
            loan=loan,
            credit_report_list=credit_report_list,
            using_factory=with_factory)


class CreditAssessorsEnum(Enum):
    age_assessment = CreditAgeAssessor
    credit_score_assessment = CreditScoreAssessor
    commitment_assessment = CommitmentAssessor
