from pydantic import BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
from datetime import datetime
import enum
from typing import List

class FillialOptions(str, enum.Enum): 
    f1 = "Fillial 1"
    f2 = "Fillial 2"
    f3 = "Fillial 3"

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