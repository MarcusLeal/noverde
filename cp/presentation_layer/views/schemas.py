from flask_restplus import Model, fields

loan_model = Model(
    'loan',
    {
        'name': fields.String(
            required=True,
            description="Nome do cliente",
            pattern=r'.*\S.*'),
        'cpf': fields.String(
            required=True,
            description="CPF do cliente",
            pattern=r'.*\S.*'),
        'birthdate': fields.String(
            required=True,
            description="Data de nascimento do cliente",
            pattern=r'.*\S.*'),
        'amount': fields.Float(
            required=True,
            description="Valor desejado, entre R$ 1.000,00 e R$ 4.000,00",
            pattern=r'.*\S.*',
            min=1000.0,
            max=4000.00),
        'terms': fields.String(
            required=True,
            description="Quantidade de parcelas desejadas. Valores disponíveis: 6, 9 ou 12",
            enum=("6", "9", "12")),
        'income': fields.Float(
            required=True,
            description="Renda mensal do cliente",
            pattern=r'.*\S.*'), }
)
