from fastapi import APIRouter, HTTPException
from datetime import datetime
from form_schemas import Form, EmailRequest, FillialOptions
from to_email import Frmail

form_router = APIRouter(prefix="/form", tags=["Form📄"])

@form_router.post("/send_form", response_model= EmailRequest)
async def send_form(
    full_name: str,
    birthday: str,
    parrents_full_name: str,
    number_phone: str,
    fillial: FillialOptions,
):
    form = Frmail(full_name, birthday, parrents_full_name, number_phone, fillial)
    if not number_phone.startswith('+79') or len(number_phone) != 12:
        raise HTTPException(
            status_code= 422,
            detail= 'Неверный формат номер телефона: +79XXXXXXXXX (12 цифр)'
        )


    request = EmailRequest(
        email_sender=form.SENDER,
        email_receiver=form.RECEIVER,
        sent=datetime.now(),
        form=Form(
            full_name=full_name,
            birthday=form.birthday,
            parrents_full_name=parrents_full_name,
            number_phone=number_phone,
            fillial=fillial,
        )
    )

    form.send_email()

    return request