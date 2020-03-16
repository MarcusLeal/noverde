from abc import ABC


class CreditAnalisesService(ABC):
    """
    I know how to send a credit request for analises on the credit engine
    """

    @classmethod
    def request_analysis_score(cls, loan: 'Loan'):
        raise NotImplementedError

    @classmethod
    def request_analysis_commitment(cls, loan: 'Loan'):
        raise NotImplementedError
