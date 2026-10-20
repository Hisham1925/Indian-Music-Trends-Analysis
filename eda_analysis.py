
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("indian_music_data_final.csv")

# Convert publication date to datetime
df["Published_Date"] = pd.to_datetime(
    df["Published_Date"],
    utc=True
)

# 1. Top 10 videos by views
top_videos = df.sort_values(
    by="Views",
    ascending=False
).head(10)

print("\n===== TOP 10 VIDEOS BY VIEWS =====")
print(
    top_videos[
        ["Video_Title", "Artist_Channel", "Views"]
    ].to_string(index=False)
)

# 2. Top 10 channels by total views in this dataset
top_channels = (
    df.groupby("Artist_Channel")
    .agg(
        Total_Videos=("Video_ID", "nunique"),
        Total_Views=("Views", "sum"),
        Average_Views=("Views", "mean")
    )
    .sort_values("Total_Views", ascending=False)
    .head(10)
)

print("\n===== TOP 10 CHANNELS BY TOTAL VIEWS =====")
print(top_channels.to_string())

# 3. Overall statistics
print("\n===== OVERALL STATISTICS =====")
print("Total videos:", df["Video_ID"].nunique())
print("Total views across collected videos:", f"{df['Views'].sum():,}")
print("Average views per video:", f"{df['Views'].mean():,.0f}")
print("Median views per video:", f"{df['Views'].median():,.0f}")
