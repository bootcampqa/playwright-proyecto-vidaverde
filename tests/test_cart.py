from playwright.sync_api import Page, expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage

#Realizado por Jenniffer
def test_carrito_agregar_productos_al_carrito_ver_resumen_y_vaciar_carrito(page: Page):
    
    productos_page = ProductsPage(page)
    cart_page = CartPage(page)
    
    print("When la usuaria visita la página de productos “Nuestros Productos | Vida Verde  ”")
    productos_page.open_products_page()
    
    print("And filtra por nombre “Sansevieria”")
    productos_page.filtrar_por_nombre("Sansevieria")

    print("And añade el producto al carrito")
    productos_page.añadir_producto("Sansevieria")
    
    print("And limpia el filtro")
    productos_page.limpiar_filtros()
    
    print("and filtra por nombre “Maceta de barro”")
    productos_page.filtrar_por_nombre("Maceta de barro")

    print("And añade el producto al carrito")
    productos_page.añadir_producto("Maceta de Barro Grande")
    
    print("and visita el carrito de la compra")
    cart_page.abrir_cart_page()
    
    print("then debe ver el nombre “Sansevieria”")
    cart_page.verificar_producto_en_carrito("Sansevieria")
    
    print("and su categoría “Plantas”")
    cart_page.verificar_categoria_en_carrito("Plantas")
    
    print("and su precio “22.00 €”")
    cart_page.verificar_precio_compra("22.00 €")
    
    print("and debe ver el producto “Maceta de Barro Grande”")
    cart_page.verificar_producto_en_carrito("Maceta de Barro Grande")
    
    print("and su categoría “Macetas”")
    cart_page.verificar_categoria_en_carrito("Macetas")
    
    print("and su precio “10.50 €”")
    cart_page.verificar_precio_compra("10.50 €")
    
    print("and debe ver el resumen del pedido con los siguientes datos:")
    cart_page.verificar_resumen_pedido()
    
    print("subtotal la suma de ambos “32.50”")
    cart_page.verificar_subtotal_compra("Productos (2)32.50 €")
    
    print("con IVA 21% “6.83”")
    cart_page.verificar_iva_compra("6.83 €")
    
    print("and debe ver el total de Envío “5”")
    cart_page.verificar_envío_compra("Envío 5.00 €")
    
    print("and debe ver el total “44.33”")
    cart_page.verificar_total_precio("Total44.33 €")
    
    print("when hace clic en vaciar carrito")
    cart_page.vaciar_carrito()
    
    print("then debe ver el mensaje “tu carrito está vacío”")
    cart_page.verificar_producto_en_carrito("Tu carrito está vacío")


#Realizado por Jenniffer
def test_carrito_quitar_productos_del_carrito_y_ver_resumen(page: Page):
    
    productos_page = ProductsPage(page)
    cart_page = CartPage(page)
    
    print("When la usuaria visita la página de productos “Nuestros Productos | Vida Verde  ”")
    productos_page.open_products_page()
    
    print("And filtra por nombre Ficus")
    productos_page.filtrar_por_nombre("Ficus Lyrata")
    
    print("And añade el producto al carrito")
    productos_page.añadir_producto("Ficus Lyrata")
    
    print("And limpia el filtro")
    productos_page.limpiar_filtros()
    
    print("and filtra por nombre “Tijeras”")
    productos_page.filtrar_por_nombre("Tijeras de Podar")
    
    print("And añade el producto al carrito")
    productos_page.añadir_producto("Tijeras de Podar")
    
    print("and visita el carrito de la compra")
    cart_page.abrir_cart_page()
    
    print("when elimina el producto “ficus” desde la página del carrito")
    cart_page.eliminar_producto("ficus")
    
    print("then no debe ver el producto “ficus”")
    cart_page.verificar_producto_no_visible_carrito("Ficus")
    
    print("then debe ver el resumen actualizado")
    cart_page.verificar_resumen_pedido()
   
    print("subtotal la suma de ambos “18.50”")
    cart_page.verificar_subtotal_compra("Productos (1)18.50 €")
    
    print("and el iva “3.88”")
    cart_page.verificar_iva_compra("3.88 €")
    
    print("and debe ver el total de Envío “5”")
    cart_page.verificar_envío_compra("Envío 5.00 €")
    
    print("and el total “27.38”")
    cart_page.verificar_total_precio("Total27.38 €")
    


