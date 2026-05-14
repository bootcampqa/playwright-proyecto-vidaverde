from playwright.sync_api import Page, expect

#Realizado por Jenniffer
class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/cart'
        self.title = "Carrito de Compra"

    def abrir_cart_page(self):
        self.page.goto(self.url)

    def verificar_producto_en_carrito(self, product_name):
        expect(self.page.get_by_text(product_name)).to_be_visible()

    def verificar_categoria_en_carrito(self, categoria_name):
        expect(self.page.get_by_text(categoria_name)).to_be_visible()

    def verificar_precio_compra(self, precio):
        expect(self.page.get_by_text(precio)).to_be_visible()

    def verificar_total_precio(self, total):
        expect(self.page.get_by_text(total)).to_be_visible()

    def verificar_numero_productos(self, cantidad):
        expect(self.page.locator(".cart-item")).to_have_count(cantidad)

    def verificar_subtotal_compra(self, subtotal):
        expect(self.page.get_by_text(subtotal)).to_be_visible()

    def verificar_iva_compra(self, iva):
        expect(self.page.get_by_text("IVA (21%)"+iva)).to_be_visible()

    def verificar_envío_compra(self, envío):
        expect(self.page.get_by_text("5.00")).to_be_visible()

    def eliminar_producto(self, product_name):
        self.page.get_by_role("button", name=f"Eliminar {product_name}").click()

    def verificar_producto_no_visible_carrito(self, product_name):
        expect(self.page.get_by_text(product_name)).not_to_be_visible()

    def verificar_resumen_pedido(self):
        expect(self.page.get_by_text("Resumen del Pedido")).to_be_visible()

    def vaciar_carrito(self):
        self.page.get_by_role("button", name="Vaciar carrito").click()

    def ir_a_checkout(self):
        self.page.get_by_role("button", name="Finalizar compra").click()


#Realizado Lorena y Eli ❤️
    def hacer_click_pago(self):
        self.page.get_by_role("link", name="Proceder al Pago").click()
    
    