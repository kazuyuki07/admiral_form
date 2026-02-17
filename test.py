from mjml import mjml_to_html
import html


with open('templates/form_email.mjml', 'r', encoding='utf-8') as form:

    result = mjml_to_html(form)
    print(html.escape(result.html))