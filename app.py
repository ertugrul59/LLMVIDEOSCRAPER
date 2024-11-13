from videoanalyser import analyze_video
from videorecorder import record_scroll_video


def run_scraper(url):
    video_path = "./recordings"
    record_scroll_video(url, video_path, headless=False)

    # recorder = ScrollRecorder(headless=False)
    # recorder.record_page(url)

    # analysis = analyze_video(video_path)
    # print("Video Analysis:")
    # print(analysis)


# Example usage
url_to_scrape = "https://www.coingecko.com"
run_scraper(url_to_scrape)
