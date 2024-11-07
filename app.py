from videoanalyser import analyze_video
from videorecorder import record_scroll_video

def run_scraper(url):
    video_path = "scroll_video.mp4"
    record_scroll_video(url, video_path)
    # analysis = analyze_video(video_path)
    # print("Video Analysis:")
    # print(analysis)

# Example usage
url_to_scrape = "https://example.com"
run_scraper(url_to_scrape)
