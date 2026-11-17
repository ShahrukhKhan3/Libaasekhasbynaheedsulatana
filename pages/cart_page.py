from playwright.sync_api import Page, expect


class CartPage:
    """The shopping cart: /cart/"""

    def __init__(self, page: Page):
        self.page = page

    def open(self) -> None:
        self.page.goto("/cart/")

    def verify_contains(self, product_name: str) -> None:
        expect(self.page.get_by_text(product_name, exact=False).first).to_be_visible()
