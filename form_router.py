from datetime import datetime

from fastapi import APIRouter, HTTPException

from form_schemas import EmailRequest, Form, FormInput
from to_email import Frmail

form_router = APIRouter(prefix="/form", tags=["Form📄"])


@form_router.post("/send_form", response_model=EmailRequest)
async def send_form(data: FormInput):
    form = Frmail(
        data.full_name, 
        data.birthday, 
        data.parrents_full_name, 
        data.number_phone,
        data.fillial)
    
    if not form.number_phone.startswith("+7 9"):
        raise HTTPException(
            status_code=422,
            detail="Неверный формат номер телефона",
        )

    request = EmailRequest(
        email_sender=form.SENDER,
        email_receiver=form.RECEIVER,
        sent=datetime.now(),
        form=Form(
            full_name=data.full_name,
            birthday=form.birthday,
            parrents_full_name=data.parrents_full_name,
            number_phone=data.number_phone,
            fillial=data.fillial,
        ),
    )

    form.send_email()

    return request
