import datetime
import uuid
from enum import Enum
from sqlalchemy import Column, VARCHAR, INTEGER, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import ChoiceType, PasswordType, EmailType

from .._declbase import DeclarativeBaseGuid
from ..sa_extra import _DateTime

user_types = {'Admin', 'User', 'Owner', 'Manager'}


class UserType(Enum):
    admin = "Admin"
    user = "User"
    owner = "Owner"
    manager = "Manager"


class User(DeclarativeBaseGuid):
    __tablename__ = 'user'
    __table_args__ = {}

    # column definitions
    picture = Column('picture', VARCHAR(length=200), nullable=True)
    fname = Column('firstName', VARCHAR(length=25), nullable=False)
    lname = Column('lastName', VARCHAR(length=25), nullable=False)
    email = Column('email', EmailType, nullable=False)
    age = Column('age', INTEGER, nullable=False)
    gender = Column('gender', VARCHAR(length=10), nullable=False)
    identifier = Column('identifier', VARCHAR(length=10), unique=True, nullable=False)
    secret = Column('secret', PasswordType(schemes=['bcrypt', 'plaintext'],
                                           deprecated=['plaintext']), nullable=False)
    status = Column('status', VARCHAR(length=10), nullable=False)
    password_reset = Column('password_reset', VARCHAR(5), nullable=False, unique=True,
                            default=lambda: str(uuid.uuid4().hex)[10:15])
    role = Column('role', ChoiceType(UserType), nullable=False)

    def __init__(self,
                 picture=None,
                 fname="",
                 lname="",
                 email="",
                 age=0,
                 gender="Male",
                 identifier="",
                 secret="",
                 status="Permanent",
                 role="",
                 salary=0,
                 added_by=0,
                 branch_id=""):
        self.picture = picture
        self.fname = fname
        self.lname = lname
        self.age = age
        self.email = email
        self.gender = gender
        self.identifier = identifier
        self.secret = secret.encode("utf8")
        self.status = status
        self.role = role
        self.salary = salary
        self.added_by = added_by
        self.last_update_by = self.added_by
        self.branch_id = branch_id