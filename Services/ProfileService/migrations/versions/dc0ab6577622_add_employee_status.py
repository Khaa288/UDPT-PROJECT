"""add employee status

Revision ID: dc0ab6577622
Revises: d78c0cb14ba3
Create Date: 2024-08-23 14:55:57.120483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc0ab6577622'
down_revision = 'd78c0cb14ba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
    sa.Column('UserId', sa.Integer(), nullable=False),
    sa.Column('Username', sa.String(length=128), nullable=False),
    sa.Column('Password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('UserId'),
    sa.UniqueConstraint('Username')
    )
    op.create_table('Employee',
    sa.Column('EmployeeId', sa.Integer(), nullable=False),
    sa.Column('UserId', sa.Integer(), nullable=False),
    sa.Column('FirstName', sa.String(length=128), nullable=False),
    sa.Column('MiddleName', sa.String(length=128), nullable=False),
    sa.Column('LastName', sa.String(length=128), nullable=False),
    sa.Column('IdCardNum', sa.String(length=128), nullable=False),
    sa.Column('TaxNum', sa.String(length=128), nullable=False),
    sa.Column('Address', sa.String(length=128), nullable=False),
    sa.Column('PhoneNum', sa.String(length=128), nullable=False),
    sa.Column('BankAccountNum', sa.String(length=128), nullable=False),
    sa.Column('Gender', sa.String(length=128), nullable=False),
    sa.Column('Role', sa.String(length=128), nullable=False),
    sa.Column('JobTitle', sa.String(length=128), nullable=False),
    sa.Column('Status', sa.Enum('ACTIVATED', 'DEACTIVATED', name='employeestatus'), nullable=False),
    sa.ForeignKeyConstraint(['UserId'], ['User.UserId'], ),
    sa.PrimaryKeyConstraint('EmployeeId')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Employee')
    op.drop_table('User')
    # ### end Alembic commands ###
