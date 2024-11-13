from playwright.sync_api import sync_playwright
import time


def record_scroll_video(url, output_path, headless=False):
    with sync_playwright() as p:
        # Launch browser with video recording enabled
        browser = p.chromium.launch(
            headless=headless,
        )
        context = browser.new_context(
            record_video_dir=output_path,
            viewport={"width": 1280, "height": 720},
        )

        # Create new pagedsada
        page = context.new_page()

        try:
            # Navigate to URL
            page.goto(url)

            # Get initial page dimensions
            page_dimensions = page.evaluate(
                """
                () => ({
                    scrollHeight: document.documentElement.scrollHeight,
                    viewportHeight: window.innerHeight
                })
            """
            )

            scroll_height = page_dimensions["scrollHeight"]
            viewport_height = page_dimensions["viewportHeight"]

            # Calculate scroll parameters
            scroll_step = viewport_height / 16  # Scroll half a viewport at a time
            total_steps = (scroll_height / scroll_step) + 1
            scroll_interval = 100  # milliseconds between scrolls

            # Perform smooth scrolling
            for step in range(int(total_steps)):
                current_position = min(step * scroll_step, scroll_height)
                page.evaluate(f"window.scrollTo(0, {current_position})")
                time.sleep(scroll_interval / 1000)  # Convert ms to seconds

            # Scroll back to top (optional)
            page.evaluate("window.scrollTo(0, 0)")

            # Wait for any final animations to complete
            time.sleep(1)

        finally:
            # Close context and browser
            context.close()
            browser.close()


# Example usage
if __name__ == "__main__":
    url = "https://example.com"
    output_directory = "./recordings"  # Directory to store video files
    record_scroll_video(url, output_directory)
