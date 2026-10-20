
import os
import pandas as pd
from dotenv import load_dotenv
from googleapiclient.discovery import build

# Load API key
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("YouTube API key not found. Check your .env file.")

# Connect to YouTube
youtube = build("youtube", "v3", developerKey=API_KEY)

# Search terms covering Indian music

search_terms = [
    "Tamil film songs official music video",
    "Tamil independent songs official",
    "Hindi Bollywood songs official music video",
    "Hindi independent songs official",
    "Telugu film songs official music video",
    "Malayalam film songs official music video",
    "Kannada film songs official music video",
    "Punjabi songs official music video",
    "Bengali songs official music video",
    "Marathi songs official music video",
    "Indian devotional songs official",
    "Indian classical music performance"
]


videos = {}

for term in search_terms:
    print(f"Searching: {term}")

    try:
        request = youtube.search().list(
            part="snippet",
            q=term,
            type="video",
            videoCategoryId="10",
            order="viewCount",
            maxResults=50,
            regionCode="IN"
        )

        response = request.execute()

        for item in response.get("items", []):
            video_id = item["id"]["videoId"]
            snippet = item["snippet"]

            videos[video_id] = {
                "Video_ID": video_id,
                "Video_Title": snippet["title"],
                "Artist_Channel": snippet["channelTitle"],
                "Published_Date": snippet["publishedAt"],
                "Video_URL": f"https://www.youtube.com/watch?v={video_id}"
            }

    except Exception as error:
        print(f"Could not complete search for '{term}': {error}")

# Fetch statistics in batches of up to 50
video_ids = list(videos.keys())
results = []

for start in range(0, len(video_ids), 50):
    batch_ids = video_ids[start:start + 50]

    try:
        response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(batch_ids)
        ).execute()

        for item in response.get("items", []):
            stats = item.get("statistics", {})
            snippet = item["snippet"]
            video_id = item["id"]

            results.append({
                "Video_ID": video_id,
                "Video_Title": snippet["title"],
                "Artist_Channel": snippet["channelTitle"],
                "Published_Date": snippet["publishedAt"],
                "Views": int(stats.get("viewCount", 0)),
                "Likes": int(stats.get("likeCount", 0)),
                "Comments": int(stats.get("commentCount", 0)),
                "Video_URL": f"https://www.youtube.com/watch?v={video_id}"
            })

    except Exception as error:
        print(f"Could not retrieve a statistics batch: {error}")

# Save data
df = pd.DataFrame(results)

if not df.empty:
    df = df.drop_duplicates(subset="Video_ID")
    df.to_csv(
    "indian_music_data_refined.csv",
    index=False,
    encoding="utf-8-sig"
)
    print(f"\nCollection complete! Saved {len(df)} videos.")
    print("File: indian_music_data.csv")
    print(df.head())
else:
    print("No video data collected. Check your API key, quota, and errors.")
