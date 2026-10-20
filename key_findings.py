
import pandas as pd

# Load dataset
df = pd.read_csv("indian_music_data_final.csv")

# Convert publication date
df["Published_Date"] = pd.to_datetime(
    df["Published_Date"], utc=True
)

# Remove videos with zero views for engagement calculations
engagement_df = df[df["Views"] > 0].copy()

engagement_df["Like_Rate (%)"] = (
    engagement_df["Likes"] / engagement_df["Views"] * 100
)

engagement_df["Comment_Rate (%)"] = (
    engagement_df["Comments"] / engagement_df["Views"] * 100
)

# Overall KPIs
print("========== PROJECT SUMMARY ==========")
print("Videos analyzed:", df["Video_ID"].nunique())
print(f"Total views: {df['Views'].sum():,}")
print(f"Average views: {df['Views'].mean():,.0f}")
print(f"Median views: {df['Views'].median():,.0f}")
print(f"Total likes: {df['Likes'].sum():,}")
print(f"Total comments: {df['Comments'].sum():,}")

# Most viewed video
most_viewed = df.loc[df["Views"].idxmax()]

print("\n========== MOST VIEWED VIDEO ==========")
print("Title:", most_viewed["Video_Title"])
print("Channel:", most_viewed["Artist_Channel"])
print(f"Views: {most_viewed['Views']:,}")
print("URL:", most_viewed["Video_URL"])

# Channel with most views in our dataset
channel_views = (
    df.groupby("Artist_Channel")["Views"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== TOP CHANNEL IN COLLECTED DATA ==========")
print("Channel:", channel_views.index[0])
print(f"Views across collected videos: {channel_views.iloc[0]:,}")

# Engagement summary
print("\n========== ENGAGEMENT ==========")
print(
    f"Average like rate: "
    f"{engagement_df['Like_Rate (%)'].mean():.2f}%"
)
print(
    f"Average comment rate: "
    f"{engagement_df['Comment_Rate (%)'].mean():.3f}%"
)

# Publication-year distribution
yearly = df.groupby(df["Published_Date"].dt.year).size()

print("\n========== VIDEOS BY PUBLICATION YEAR ==========")
print(yearly.to_string())

# Highest-volume year in our collected dataset
print(
    "\nYear with most collected videos:",
    yearly.idxmax(),
    f"({yearly.max()} videos)"
)

print("\n========== TOP 5 CHANNELS BY TOTAL VIEWS ==========")

top_channels = (
    df.groupby("Artist_Channel")["Views"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_channels.to_string())


print("\n========== TOP 10 VIDEOS BY LIKE RATE ==========")

df["Like_Rate (%)"] = (
    df["Likes"] / df["Views"].replace(0, float("nan")) * 100
)

top_like_rate = df.nlargest(10, "Like_Rate (%)")[
    ["Video_Title", "Artist_Channel", "Views", "Likes", "Like_Rate (%)"]
]

print(
    top_like_rate.to_string(
        index=False,
        formatters={
            "Views": "{:,}".format,
            "Likes": "{:,}".format,
            "Like_Rate (%)": "{:.2f}%".format
        }
    )
)
