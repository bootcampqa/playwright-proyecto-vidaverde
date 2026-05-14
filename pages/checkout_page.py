from playwright.sync_api import Page, expect
#Realizado por Lorena
class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/checkout'
    
    def abrir_cart_page(self):
        self.page.goto(self.url)

    def hacer_click_pago(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()

    def verifica_resumen_compra(self):
        expect(self.page.get_by_role("heading", name="Resumen del pedido")).to_be_visible()

    def verificar_producto_compra(self,name):
        expect(self.page.get_by_text(name)).to_be_visible()

    def verificar_precio_compra(self,name):
        expect(self.page.get_by_role("listitem").filter(has_text=name).locator("data")).to_be_visible()

    def verificar_subtotal_compra(self,subtotal):
        expect(self.page.get_by_role("definition").filter(has_text=subtotal).locator("data")).to_be_visible()

    def verificar_iva_compra(self,iva):
        expect(self.page.get_by_text(iva)).to_be_visible()

    def verificar_envio_compra(self,envio):
        expect(self.page.get_by_text(envio)).to_be_visible()

    def verificar_total_compra(self,total):
        expect(self.page.get_by_text(total)).to_be_visible()

    def rellenar_nombre_contacto (self, nombre):
        self.page.get_by_role("textbox", name="Nombre Completo *").fill(nombre)

    def rellenar_email_contacto (self, email):
        self.page.get_by_role("textbox", name="Email *").fill(email)

    def rellenar_direccion_contacto (self, direccion):
        self.page.get_by_role("textbox", name="Dirección *").fill(direccion)

    def completar_click_compra(self):
        self.page.get_by_role("button", name="Completar Compra").click()

    def visualizar_checkout_compra(self):
        expect(self.page.get_by_role("heading", name="Finalizar Compra")).to_be_visible()

    def verificar_error_tarjeta(self, mensaje):
        expect(self.page.get_by_text(mensaje)).to_be_visible()

    def añadir_tarjeta(self, numerotarjeta):
        self.page.get_by_role("textbox", name="Número de Tarjeta de Crédito *").fill(numerotarjeta)




    
    
