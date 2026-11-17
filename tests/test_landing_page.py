from pages.landing_page import LandingPage
from pages.product_page import ProductPage


def test_landing_page_loads(landing_page: LandingPage):
    landing_page.verify_loaded()


def test_open_first_product(landing_page: LandingPage, product_page: ProductPage):
    landing_page.open_first_product()
    product_page.verify_loaded()
