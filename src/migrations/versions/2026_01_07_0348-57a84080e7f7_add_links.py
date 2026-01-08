"""add links

Revision ID: 57a84080e7f7
Revises:
Create Date: 2026-01-07 03:48:23.786153

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "57a84080e7f7"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "links",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("dest_url", sa.String(), nullable=False),
        sa.Column("slug", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("slug"),
    )


def downgrade() -> None:
    op.drop_table("links")
