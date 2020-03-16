from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID

from cp.app import db

loan_table = db.Table(
    'loans', db.metadata,
    db.Column('id',
              UUID(as_uuid=True),
              server_default=db.text('uuid_generate_v4()'),
              unique=True, nullable=False, primary_key=True),
    db.Column('name', db.String(120)),
    db.Column('cpf', db.String(11)),
    db.Column('birthdate', db.Date),
    db.Column('amount', db.Float),
    db.Column('terms', db.Integer),
    db.Column('income', db.Float),
    db.Column('insert_at', db.DateTime, default=datetime.utcnow),
    db.Column('update_at', db.DateTime, default=datetime.utcnow,
              onupdate=datetime.utcnow))
