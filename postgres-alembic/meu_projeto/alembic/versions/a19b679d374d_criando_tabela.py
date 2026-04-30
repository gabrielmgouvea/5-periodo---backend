"""criando_tabela

Revision ID: a19b679d374d
Revises: 
Create Date: 2026-04-30 20:23:19.969223

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a19b679d374d'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'produtos',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('nome', sa.String(length=50), nullable=False)
    )

def downgrade() -> None:
    op.drop_table('produtos')
