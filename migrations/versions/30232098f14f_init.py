"""init

Revision ID: 30232098f14f
Revises: 
Create Date: 2022-04-20 22:27:10.373057

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "30232098f14f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hairproduct",
        sa.Column("product_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("product_brand", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("product_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("straight", sa.Boolean(), nullable=True),
        sa.Column("wavy", sa.Boolean(), nullable=True),
        sa.Column("curly", sa.Boolean(), nullable=True),
        sa.Column("coily", sa.Boolean(), nullable=True),
        sa.Column("fine", sa.Boolean(), nullable=True),
        sa.Column("medium", sa.Boolean(), nullable=True),
        sa.Column("thick", sa.Boolean(), nullable=True),
        sa.Column("image_link", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("product_id"),
    )
    op.create_table(
        "skinproduct",
        sa.Column("product_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("product_brand", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("product_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("oily", sa.Boolean(), nullable=True),
        sa.Column("dry", sa.Boolean(), nullable=True),
        sa.Column("normal", sa.Boolean(), nullable=True),
        sa.Column("image_link", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("product_id", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("product_id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("skinproduct")
    op.drop_table("hairproduct")
    # ### end Alembic commands ###
