from pages.cart_page import CartPage
from pages.product_page import ProductPage

# A product that is in stock and has a "Large" size. If the shop sells out
# or removes it, change these two values.
PRODUCT_SLUG = "chrizma-luxe"
PRODUCT_NAME = "chrizma luxe"
SIZE = "Large"


def test_add_product_to_cart(product_page: ProductPage, cart_page: CartPage):
    product_page.open(PRODUCT_SLUG)
    product_page.select_size(SIZE)
    product_page.add_to_cart()
    product_page.verify_added_to_cart(PRODUCT_NAME)

    cart_page.open()
    cart_page.verify_contains(PRODUCT_NAME)
