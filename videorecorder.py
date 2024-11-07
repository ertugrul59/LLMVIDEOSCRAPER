from playwright.sync_api import sync_playwright
import time

def record_scroll_video(url, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        page.video.start(path=output_path, size={"width": 1280, "height": 720})
        
        # Scroll from top to bottom
        page.evaluate("""
            () => {
                const scrollHeight = document.body.scrollHeight;
                const scrollStep = window.innerHeight / 2;
                const scrollInterval = 100;
                let currentPosition = 0;
                
                function smoothScroll() {
                    if (currentPosition < scrollHeight) {
                        window.scrollTo(0, currentPosition);
                        currentPosition += scrollStep;
                        setTimeout(smoothScroll, scrollInterval);
                    }
                }
                
                smoothScroll();
            }
        """)
        
        # Wait for scrolling to complete
        time.sleep(10)  # Adjust based on page length
        
        page.video.stop()
        browser.close()
