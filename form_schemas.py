import enum
from datetime import datetime
from typing import List

from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber


class FillialOptions(str, enum.Enum):
    f1 = "Москва, Затонная, 22"
    f2 = "Москва, Новинки, 8"
    f3 = "Москва, Судостроительная улица, 46с1"
    f4 = "Москва, Стадион Огонёк"
    # f4 = "Москва, Судостроительная, 48"
    # f5 = "Москва, Спортивная, вл 2"
    # f6 = "Москва, Судостроительная 32к3"


class Fillials(BaseModel):
    option: List[str]


class FormInput(BaseModel):
    full_name: str
    birthday: str
    parrents_full_name: str
    number_phone: str
    fillial: FillialOptions


class Form(BaseModel):
    full_name: str
    birthday: datetime
    parrents_full_name: str
    number_phone: PhoneNumber
    fillial: FillialOptions


class EmailRequest(BaseModel):
    email_sender: str
    email_receiver: str
    sent: datetime
    form: Form
