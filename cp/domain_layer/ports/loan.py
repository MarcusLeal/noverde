from abc import ABC
from cp.domain_layer.models.loan import Loan


class LoanRepository(ABC):

    @classmethod
    def filter_loan(
            cls, *, id: str = None, cpf: str = None) -> Loan:
        raise NotImplementedError

    @classmethod
    def insert_loan(
            cls, name: str, cpf: str, birthdate: str,
            amount: float, terms: int, income: float) -> Loan:
        raise NotImplementedError
