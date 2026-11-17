import re

from playwright.sync_api import Page, expect


class LandingPage:
    """Home page: https://libasekhasbynaheed.com/"""

    def __init__(self, page: Page):
        self.page = page
        # Product images have no alt text, so we find product cards by their link URL.
        self.product_links = page.locator("a[href*='/product/']:has(img)")

    def open(self) -> None:
        self.page.goto("/")  # resolved against base_url in pytest.ini

    def verify_loaded(self) -> None:
        expect(self.page).to_have_title(re.compile(r"libasekhasbynaheed\.com", re.IGNORECASE))
        expect(self.product_links.first).to_be_visible()

    def open_first_product(self) -> None:
        self.product_links.first.click()
