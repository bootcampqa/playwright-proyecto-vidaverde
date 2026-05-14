from playwright.sync_api import Page
from pages.checkout_page import CheckoutPage
from pages.confirmation_page import ConfirmationPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


#Realizado por Lorena
def test_compra_con_tarjeta_vacia(page: Page):

    checkout_page = CheckoutPage (page)
    productos_page = ProductsPage (page)
    cart_page = CartPage (page)

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.open_products_page()

    print("When filtra por nombre “palas”")
    productos_page.filtrar_por_nombre("palas")

    print("And agrega el producto al carrito")
    productos_page.añadir_producto("Juego de Palas")

    print("And visita la página del carrito")
    cart_page.abrir_cart_page()

    print("And hace click en proceder al pago")
    cart_page.hacer_click_pago()

    print("When rellena el campo de nombre válido “Maria Diaz”")
    checkout_page.rellenar_nombre_contacto("Maria Diaz")

    print("And rellena el campo email válido “test@gmail.com”")
    checkout_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion válida “Calle Aragón, 25, Madrid”")
    checkout_page.rellenar_direccion_contacto("Calle Aragon 25 Madrid")

    print("And hace click en completar compra")
    checkout_page.completar_click_compra()

    print("Then el usuario permanece en la página de check out Finalizar Compra | Vida Verde ")
    checkout_page.visualizar_checkout_compra()

#Realizado por Lorena
def test_compra_con_tarjeta_invalida(page: Page):
    
    checkout_page = CheckoutPage (page)
    productos_page = ProductsPage (page)
    cart_page = CartPage (page)

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.open_products_page()

    print("When filtra por nombre “palas”")
    productos_page.filtrar_por_nombre("palas")

    print("And agrega el producto al carrito")
    productos_page.añadir_producto("Juego de Palas")

    print("And visita la página del carrito")
    cart_page.abrir_cart_page()

    print("And hace click en proceder al pago")
    cart_page.hacer_click_pago()

    print("When rellena el campo de nombre válido “Maria Diaz”")
    checkout_page.rellenar_nombre_contacto("Maria Diaz")

    print("And rellena el campo email válido “test@gmail.com”")
    checkout_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion válida “Calle Aragón, 25, Madrid”")
    checkout_page.rellenar_direccion_contacto("Calle Aragon 25 Madrid")

    print("And rellena la tarjeta inválida")
    checkout_page.añadir_tarjeta("1111424242424242")

    print("And hace click en completar compra")
    checkout_page.completar_click_compra()

    print("Then debe ver un mensaje de error en la tarjeta")
    checkout_page.verificar_error_tarjeta("Tarjeta de crédito no válida")


    #Realizado por Eli
def test_compra_datos_validos (page: Page):

    checkout_page = CheckoutPage (page)
    productos_page = ProductsPage (page)
    cart_page = CartPage (page)
    confirmation_page = ConfirmationPage(page)

    print("Given el usuario abre la página de productos Nuestros Productos | Vida Verde ")
    productos_page.open_products_page()

    print("When filtra por nombre “palas”")
    productos_page.filtrar_por_nombre("palas")

    print("And agrega el producto al carrito")
    productos_page.añadir_producto("Juego de Palas")

    print("And visita la página del carrito")
    cart_page.abrir_cart_page()

    print("And hace click en proceder al pago")
    cart_page.hacer_click_pago()

    print("Then debe ver el resumen del pedido con")
    checkout_page.verifica_resumen_compra()

    print("then debe ver el producto “juego de palas”")
    checkout_page.verificar_producto_compra("Juego de Palas")

    print("then debe ver precio del producto “15.99”")
    checkout_page.verificar_precio_compra("Juego de Palas15.99 €")

    print("then debe ver el subtotal “15.99”")
    checkout_page.verificar_subtotal_compra("15.99 €")

    print("then debe ver el IVA “3.36”")
    checkout_page.verificar_iva_compra("3.36 €")

    print("then debe ver el envío “5”")
    checkout_page.verificar_envio_compra("5.00 €")

    print("and debe ver el total “24”")
    checkout_page.verificar_total_compra("24.35 €")

    print("When rellena el campo de nombre válido “Maria Diaz”")
    checkout_page.rellenar_nombre_contacto("Maria Diaz")

    print("And rellena el campo email válido “test@gmail.com”")
    checkout_page.rellenar_email_contacto("test@gmail.com")

    print("And rellena la direccion válida “Calle Aragón, 25, Madrid”")
    checkout_page.rellenar_direccion_contacto("Calle Aragon 25 Madrid")

    print("And rellena la tarjeta válida")
    checkout_page.añadir_tarjeta("4242424242424242")

    print("And hace click en completar compra")
    checkout_page.completar_click_compra()

    print ("Comprueba el resumen del pedido completado confirmando el mensaje de '¡Compra realizada con éxito!'")
    confirmation_page.verificar_compra_realizada()
    print("Ve el producto 'Juego de palas' por valor '15,99€'")
    confirmation_page.verificar_producto_y_valor("Juego de Palas15.99 €")
    print("Ve el IVA '3,36€'")
    confirmation_page.verificar_IVA("IVA (21%)3.36 €")
    print("Ve el envío '5€'")
    confirmation_page.verificar_envio("Envío5.00 €")
    print("Ve el total de compra por importe '24,35€'")
    confirmation_page.verificar_total_compra("Total24.35 €")
    print ("Hace clic en 'Volver a la tienda'")
    confirmation_page.hace_clic_volver_tienda()
 
    print ("Ve la URL https://web-qa.dev.adalab.es/products")
    productos_page.verify_products_url()