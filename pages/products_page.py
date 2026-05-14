from playwright.sync_api import Page, expect

class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://web-qa.dev.adalab.es/products'
        self.title = "Catálogo de Productos"

    
    def open_products_page(self):
        self.page.goto(self.url)

    def verify_products_category(self, category):
        expect(self.page.get_by_text(category).nth(2)).to_be_visible()

    def verify_products_name(self,product_name):
        expect(self.page.get_by_role("heading", name=product_name)).to_be_visible()

    def verify_products_price(self,price):
        expect(self.page.get_by_text(price)).to_be_visible()

    def verify_products_title(self):
        expect(self.page.locator("h1")).to_contain_text(self.title)

    def verify_products_url(self):
        expect(self.page).to_have_url(self.url)
    
    def filtrar_por_nombre(self, nombre):
        self.page.get_by_role("searchbox", name="Nombre").fill(nombre)

    def filtrar_por_categoria(self, categoria): 
        self.page.get_by_label("Categoría").select_option(categoria)

    def filtrar_por_precio_minimo(self, minimo): 
        self.page.get_by_role("spinbutton", name="Precio mínimo").fill(minimo)

    def filtrar_por_precio_maximo(self, maximo):
        self.page.get_by_role("spinbutton", name="Precio máximo").fill(maximo)

    def verificar_mensaje_no_resultados(self):
        expect(self.page.get_by_text("No se encontraron productos")).to_be_visible()            


