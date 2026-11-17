import pytest
from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.landing_page import LandingPage
from pages.product_page import ProductPage

# Fixtures: pytest creates these automatically for any test that lists the
# fixture's name as a parameter. Never import or call them yourself.
# `page` comes from pytest-playwright: a fresh browser tab for every test.


@pytest.fixture
def landing_page(page: Page) -> LandingPage:
    landing = LandingPage(page)
    landing.open()
    return landing


@pytest.fixture
def product_page(page: Page) -> ProductPage:
    return ProductPage(page)


@pytest.fixture
def cart_page(page: Page) -> CartPage:
    return CartPage(page)
