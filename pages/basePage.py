from playwright.sync_api import Page, Locator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self, url: str):
        """Navigate to a specified URL."""
        self.page.goto(url)

    def click(self, element: Locator):
        """Click an element (expects a Locator)."""
        element.click()

    def type(self, element: Locator, text: str):
        """Type an input field (expects a Locator)."""
        element.type(text)

    def fill(self, element: Locator, text: str):
        """Fill an input field (expects a Locator)."""
        element.fill(text)

    def press_enter_on_element(self, element: Locator):
        """press enter on element."""
        element.press("Enter")

    def press_enter_on_page(self):
        """press enter on page."""
        self.page.keyboard.press("Enter")

    def get_title_of_page(self) -> str:
        """Get the title of the page."""
        return self.page.title()

    def get_text(self, element: Locator) -> str:
        """Get the text content of an element (expects a Locator)."""
        return element.inner_text()

    def is_visible(self, element: Locator) -> bool:
        """Check if an element is visible (expects a Locator)."""
        return element.is_visible()

    def wait_for_element_to_be_visible(self, element: Locator, timeout: int = 5000):
        """Wait for an element to be visible (expects a Locator)."""
        element.wait_for(state="visible", timeout=timeout)

    def take_screenshot(self, path: str = "screenshot.png"):
        """Take a screenshot of the page."""
        self.page.screenshot(path=path)

    def switch_to_iframe(self, locator_str: str):
        """Switch to an iframe using a selector string and return the FrameLocator object."""
        self.page.locator(locator_str).wait_for(state="visible")
        frame = self.page.frame_locator(locator_str)
        return frame
