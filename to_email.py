from mjml import mjml_to_html
from jinja2 import Template
import smtplib
import configparser
import os
from dotenv import load_dotenv
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from form_schemas import FillialOptions

class Frmail:
    def __init__(self, 
                 full_name: str, 
                 birthday: str,
                 parrents_full_name: str,
                 number_phone: str,
                 fillial: str
    ):        
        config = configparser.ConfigParser()
        config.read('email_config.ini')

        self.birthday = datetime.strptime(birthday, '%d.%m.%Y')

        load_dotenv()

        self.SENDER = os.getenv('EMAIL_SENDER')
        self.RECEIVER = os.getenv('EMAIL_RECEIVER')
        self.PASSWORD = os.getenv('EMAIL_PASSWORD')

        self.HOST = config['SMTP']['host']
        self.PORT = config['SMTP']['port']


        context = {
            'full_name': full_name,
            'birthday': birthday,
            'parrents_full_name': parrents_full_name,
            'number_phone': number_phone,
            'fillial': FillialOptions(fillial).value
        }

        with open('templates/form_email.mjml', 'r', encoding='utf-8') as form:
            template = Template(form.read())

        rendered_mjml = template.render(**context)

        result = mjml_to_html(rendered_mjml)
        self.html_email = result.html


    def send_email(self):
        msg = MIMEMultipart('alternative')
        msg['From'] = self.SENDER
        msg['To'] = self.RECEIVER
        msg['Subject'] = 'Заявка на запись'

        msg.attach(MIMEText(self.html_email, 'html', 'utf-8'))


        try:
            with smtplib.SMTP(self.HOST, self.PORT) as server:
                server.starttls()
                server.login(self.SENDER, self.PASSWORD)
                server.send_message(msg)
            
            print('✔️ Письмо с формой - отправлено!')

        except Exception as e:
            print('❌ Не отправлено:\n\n' + str(e))