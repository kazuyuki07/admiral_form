from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime
import enum
from typing import List

class FillialOptions(str, enum.Enum):
    f1 = "Коломенская" 
    f2 = "Царицино"
    
    # f1 = "Затонная, 22"
    # f2 = "Судостроительная, 48"
    # f3 = "Судостроительная, 46"
    # f4 = "Новинки, 8"
    # f5 = "Спортивная, вл 2"
    # f6 = "Судостроительная 32к3"

class Fillials(BaseModel):
    option: List[str]

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
