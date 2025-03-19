from playwright.sync_api import Page, Locator, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, element: Locator):
        """Click an element (expects a Locator)."""
        element.click()

    def type(self, element: Locator, text: str, delay: int = 100):
        """Type an input field (expects a Locator)."""
        element.type(text, delay=delay)

    def fill(self, element: Locator, text: str):
        """Fill an input field (expects a Locator)."""
        element.fill(text)

    def get_text(self, element: Locator) -> str:
        """Get the text content of an element (expects a Locator)."""
        return element.inner_text()

    def is_visible(self, element: Locator) -> bool:
        """Check if an element is visible (expects a Locator)."""
        return element.is_visible()

    def wait_for_timeout(self, time: int) -> None:
        self.page.wait_for_timeout(time)

    def wait_for_element_to_be_visible_locator(self, element: Locator, timeout: int = 5000):
        """Wait for an element to be visible (expects a locator)."""
        expect(element).to_be_visible(timeout=timeout)
