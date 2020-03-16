from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import List
from uuid import UUID


@dataclass
class CreditAssessmentProfileFactory:
    assessment_params: dict
    is_default: bool = False
    uuid: UUID = None

    def create_credit_assessment_profile(self) -> 'CreditAssessmentProfile':
        from cp.domain_layer.models.analysis import (
            CreditAssessmentProfile, CreditAssessorsEnum)

        return CreditAssessmentProfile(
            uuid=self.uuid,
            is_default=self.is_default,
            assessment_params=self.assessment_params,
            assessors=[CreditAssessorsEnum[assessor_name].value
                       for assessor_name in self.assessment_params])


@dataclass
class CreditAssessmentReportCollectionFactory:
    loan: 'Loan'
    profile_version: 'CreditAssessmentVersion'
    credit_report_list: List['CreditReport']
    creation_date: datetime = None
    uuid: UUID = None

    def create_credit_assessment_report_collection(
            self) -> 'CreditAssessmentReportCollection':
        from cp.domain_layer.models.analysis import CreditAssessmentReportCollection

        return CreditAssessmentReportCollection(
            loan=self.loan,
            profile_version=self.profile_version,
            credit_report_list=self.credit_report_list,
            creation_date=self.creation_date,
            uuid=self.uuid)