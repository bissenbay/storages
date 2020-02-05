"""Create indexes for has_artifact table

Revision ID: bb26306538f0
Revises: 7d970baad7f2
Create Date: 2020-01-15 11:30:42.763848+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb26306538f0'
down_revision = '7d970baad7f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('has_artifact_python_artifact_id', 'has_artifact', ['python_artifact_id'], unique=False)
    op.create_index('has_artifact_python_package_version_entity_id', 'has_artifact', ['python_package_version_entity_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('has_artifact_python_package_version_entity_id', table_name='has_artifact')
    op.drop_index('has_artifact_python_artifact_id', table_name='has_artifact')
    # ### end Alembic commands ###