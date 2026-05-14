from playwright.sync_api import Page, expect
from pages.contact_page import ContactPage

def test_complete_and_submit_the_contact_form_with_mandatory_fields(page: Page):

    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    

    print("And rellena el email")
    contact_page.fill_contact_email("test@gmail.com")

    print("And rellena el mensaje")
    contact_page.fill_contact_message("test mensaje")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()

    print("Then debería ver un mensaje de éxito")
    contact_page.verify_message_form("¡Mensaje enviado con éxito!")



def test_form_with_required_name_field_left_empty(page: Page):
    contact_page = ContactPage(page)
    print("Given the users enters contact page 'Contact| Vida Verde'")
    contact_page.open_contact_page()

    print ("fills required email with 'test@gmail.com'")
    contact_page.fill_contact_email("test@gmail.com")
   
    print ("fills required message with 'test mesage'")
    contact_page.fill_contact_message("test mensaje")

    print ("clicks send")
    contact_page.press_send_contact()

    print ("user should see the error message 'name is mandatory'")
    contact_page.verify_message_form("El nombre es obligatorio")
  


def test_form_with_required_email_field_left_empty(page: Page):

    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    

    print("And deja vacío el campo email")

    print("And rellena el mensaje")
    contact_page.fill_contact_message("test mensaje")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()

    print ("Then se muestra un mensaje de error email obligatorio")
    contact_page.verify_message_form("El email es obligatorio")
    
   
    
def test_submit_form_empty_required_message(page: Page):
    
    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    

    print("And rellena el email")
    contact_page.fill_contact_email("test@gmail.com")

    print("And deja el campo obligatorio mensaje vacio")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()
    
    print("Then they should see an error message: El mensaje es obligatorio")
    contact_page.verify_message_form("El mensaje es obligatorio")

def test_form_invalid_required_email(page: Page):
    
    contact_page = ContactPage(page)

    print("Given la usuaria abre la página de contacto 'Contáctanos | Vida Verde'")
    contact_page.open_contact_page()

    print("When rellena el nombre")
    contact_page.fill_contact_name("Marta Diaz")
    

    print("And rellena el email con formato inválido")
    contact_page.fill_contact_email("test")

    print("And rellena el mensaje")
    contact_page.fill_contact_message("test mensaje")

    print("And pulsa el boton enviar")
    contact_page.press_send_contact()

    print("Then they should see an error message")
    contact_page.verify_message_form("El formato del email no es válido")