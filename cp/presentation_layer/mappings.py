
class PayloadMapping:
    """ Payload to domain mappings
    """

    def __init__(self, *, payload):
        self.payload = payload


class LoanMapping(PayloadMapping):
    """ I map from the payload format to a common vocabulary,
    to decouple the lower layers from the partners.
    """

    @property
    def name(self):
        return self.payload['name']

    @property
    def cpf(self):
        return self.payload['cpf']

    @property
    def birthdate(self):
        return self.payload['birthdate']

    @property
    def amount(self):
        return self.payload['amount']

    @property
    def terms(self):
        return self.payload['terms']

    @property
    def income(self):
        return self.payload['income']
