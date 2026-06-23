from googleapiclient.discovery import build
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd
import json
import os
from datetime import datetime

# =========================
# Load Environment Variables
# =========================

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# =========================
# Database Connection
# =========================

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# =========================
# YouTube Client
# =========================

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

try:

    print("Searching videos...")

    video_ids = []
    search_items = []
    next_page_token = None

    for page in range(10):  # ~500 videos

        print(f"Fetching page {page + 1}")

        response = youtube.search().list(
            q="data engineering",
            part="snippet",
            maxResults=50,
            type="video",
            pageToken=next_page_token
        ).execute()

        search_items.extend(response.get("items", []))

        for item in response.get("items", []):

            video_id = item.get("id", {}).get("videoId")

            if video_id:
                video_ids.append(video_id)

        next_page_token = response.get("nextPageToken")

        if not next_page_token:
            break

    print(f"Collected {len(video_ids)} video IDs")

    # =========================
    # Save Raw JSON
    # =========================

    os.makedirs(
        "data/raw/youtube/json",
        exist_ok=True
    )

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    json_file = (
        f"data/raw/youtube/json/"
        f"youtube_raw_{timestamp}.json"
    )

    search_response = {"items": search_items}

    with open(json_file, "w", encoding="utf-8") as f:
        json.dump(search_response, f, indent=4)

    print(f"Raw JSON saved: {json_file}")

    if len(video_ids) == 0:
        raise Exception("No video IDs returned by API")

    # =========================
    # Get Statistics
    # =========================

    records = []

    for i in range(0, len(video_ids), 50):

        batch_ids = video_ids[i:i + 50]

        video_response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(batch_ids)
        ).execute()

        for item in video_response.get("items", []):

            snippet = item.get("snippet", {})
            stats = item.get("statistics", {})

            records.append({
                "video_id": item.get("id"),
                "title": snippet.get("title"),
                "channel_name": snippet.get("channelTitle"),
                "published_at": snippet.get("publishedAt"),
                "views": int(stats.get("viewCount", 0)),
                "likes": int(stats.get("likeCount", 0)),
                "comments": int(stats.get("commentCount", 0)),
                "extracted_at": datetime.now()
            })

    df = pd.DataFrame(records)

    if df.empty:
        raise Exception("No records created")

    df = df.drop_duplicates(subset=["video_id"])

    print("\nSample Data:")
    print(df.head())

    # =========================
    # Load to PostgreSQL
    # =========================

    df.to_sql(
        "raw_youtube",
        engine,
        if_exists="append",
        index=False
    )

    print(f"\n{len(df)} records inserted into raw_youtube")

except Exception as e:
    print(f"\nERROR: {e}")
