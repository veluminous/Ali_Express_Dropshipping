"""update update_dt

Revision ID: 1c1cf1730b14
Revises: 506cf1588def
Create Date: 2021-07-11 19:42:20.748324

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1c1cf1730b14"
down_revision = "506cf1588def"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("product_lists", "update_dt")
    op.add_column("product_lists", sa.Column("update_dt", nullable=True, onupdate=sa.text("now()")))
    op.drop_column("search_texts", "update_dt")
    op.add_column("search_texts", sa.Column("update_dt", nullable=True, onupdate=sa.text("now()")))
    op.drop_column("product_details", "update_dt")
    op.add_column(
        "product_details", sa.Column("update_dt", nullable=True, onupdate=sa.text("now()"))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("product_lists", "update_dt")
    op.drop_column("search_texts", "update_dt")
    op.drop_column("product_details", "update_dt")
    # ### end Alembic commands ###
