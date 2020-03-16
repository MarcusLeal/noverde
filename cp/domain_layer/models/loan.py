from dataclasses import dataclass
from datetime import date
from decimal import Decimal
from uuid import UUID


@dataclass
class Loan:
    """
    I represent a loan
    """
    name: str
    cpf: str
    birthdate: str
    amount: Decimal
    terms: int
    income: Decimal
    id: UUID = None

    @property
    def client_age(self):
        today = date.today()
        return today.year - self.birthdate.year - \
            ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

    @classmethod
    def get_loan(
            cls, id: str, cpf: str,
            using_repository: 'LoanRepository'):

        return using_repository.filter_loan(
            uuid=uuid, cpf=cpf)

    @classmethod
    def create_loan(
            cls, name: str, cpf: str, birthdate: str, amount: float,
            terms: int, income: float, *, using_repository: 'LoanRepository'):

        return using_repository.insert_loan(
            name=name, cpf=cpf, birthdate=birthdate,
            amount=amount, terms=terms, income=income)
