import re

from playwright.sync_api import Page, expect


class ProductPage:
    """A single product page, e.g. /product/chrizma-luxe/"""

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator("h1").first
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.success_message = page.locator(".woocommerce-message")

    def open(self, slug: str) -> None:
        self.page.goto(f"/product/{slug}/")

    def verify_loaded(self) -> None:
        expect(self.page).to_have_url(re.compile(r"/product/"))
        expect(self.title).to_be_visible()

    def select_size(self, size: str) -> None:
        # Sizes are shown as clickable swatches; each has a title like "Large".
        self.page.get_by_title(size, exact=True).click()
        # The button stays "disabled" (via a CSS class) until the site's JS
        # registers the chosen size. expect() keeps retrying until it's ready.
        expect(self.add_to_cart_button).not_to_have_class(re.compile(r"\bdisabled\b"))

    def add_to_cart(self) -> None:
        self.add_to_cart_button.click()

    def verify_added_to_cart(self, product_name: str) -> None:
        expect(self.success_message).to_contain_text("has been added to your cart")
        expect(self.success_message).to_contain_text(product_name, ignore_case=True)
