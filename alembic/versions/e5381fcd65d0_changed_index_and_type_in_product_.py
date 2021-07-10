"""Changed index and type in product_details and dropped items and users table

Revision ID: e5381fcd65d0
Revises: 005a8708d74d
Create Date: 2021-07-06 17:45:12.453887

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e5381fcd65d0'
down_revision = '005a8708d74d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_items_description', table_name='items')
    op.drop_index('ix_items_id', table_name='items')
    op.drop_index('ix_items_title', table_name='items')
    op.drop_table('items')
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_id', table_name='users')
    op.drop_table('users')
    op.add_column('product_details', sa.Column('create_dt', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.add_column('product_details', sa.Column('update_dt', postgresql.TIMESTAMP(timezone=True), nullable=True))
    op.drop_index('ix_product_details_hasProperties', table_name='product_details')
    op.drop_index('ix_product_details_hasPurchaseLimit', table_name='product_details')
    op.drop_index('ix_product_details_hasVariations', table_name='product_details')
    op.drop_index('ix_product_details_htmlDescription', table_name='product_details')
    op.drop_index('ix_product_details_id', table_name='product_details')
    op.drop_index('ix_product_details_maxPurchaseLimit', table_name='product_details')
    op.drop_index('ix_product_details_priceSummary', table_name='product_details')
    op.drop_index('ix_product_details_processingTimeInDays', table_name='product_details')
    op.drop_index('ix_product_details_properties', table_name='product_details')
    op.drop_index('ix_product_details_shipping', table_name='product_details')
    op.drop_index('ix_product_details_totalOrders', table_name='product_details')
    op.drop_index('ix_product_details_totalStock', table_name='product_details')
    op.drop_index('ix_product_details_unitName', table_name='product_details')
    op.drop_index('ix_product_details_unitNamePlural', table_name='product_details')
    op.drop_index('ix_product_details_unitsPerProduct', table_name='product_details')
    op.drop_index('ix_product_details_variations', table_name='product_details')
    op.drop_index('ix_product_details_wishlistCount', table_name='product_details')
    op.drop_column('product_details', 'priceSummary')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product_details', sa.Column('priceSummary', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('ix_product_details_wishlistCount', 'product_details', ['wishlistCount'], unique=False)
    op.create_index('ix_product_details_variations', 'product_details', ['variations'], unique=False)
    op.create_index('ix_product_details_unitsPerProduct', 'product_details', ['unitsPerProduct'], unique=False)
    op.create_index('ix_product_details_unitNamePlural', 'product_details', ['unitNamePlural'], unique=False)
    op.create_index('ix_product_details_unitName', 'product_details', ['unitName'], unique=False)
    op.create_index('ix_product_details_totalStock', 'product_details', ['totalStock'], unique=False)
    op.create_index('ix_product_details_totalOrders', 'product_details', ['totalOrders'], unique=False)
    op.create_index('ix_product_details_shipping', 'product_details', ['shipping'], unique=False)
    op.create_index('ix_product_details_properties', 'product_details', ['properties'], unique=False)
    op.create_index('ix_product_details_processingTimeInDays', 'product_details', ['processingTimeInDays'], unique=False)
    op.create_index('ix_product_details_priceSummary', 'product_details', ['priceSummary'], unique=False)
    op.create_index('ix_product_details_maxPurchaseLimit', 'product_details', ['maxPurchaseLimit'], unique=False)
    op.create_index('ix_product_details_id', 'product_details', ['id'], unique=False)
    op.create_index('ix_product_details_htmlDescription', 'product_details', ['htmlDescription'], unique=False)
    op.create_index('ix_product_details_hasVariations', 'product_details', ['hasVariations'], unique=False)
    op.create_index('ix_product_details_hasPurchaseLimit', 'product_details', ['hasPurchaseLimit'], unique=False)
    op.create_index('ix_product_details_hasProperties', 'product_details', ['hasProperties'], unique=False)
    op.drop_column('product_details', 'update_dt')
    op.drop_column('product_details', 'create_dt')
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('users_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.create_table('items',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='items_owner_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='items_pkey')
    )
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.create_index('ix_items_id', 'items', ['id'], unique=False)
    op.create_index('ix_items_description', 'items', ['description'], unique=False)
    # ### end Alembic commands ###