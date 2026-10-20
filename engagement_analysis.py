import pandas as pd

# Load dataset
df = pd.read_csv("indian_music_data_final.csv")

# Avoid division by zero
df = df[df["Views"] > 0].copy()

# Calculate engagement rates
df["Like_Rate (%)"] = (
    df["Likes"] / df["Views"] * 100
)

df["Comment_Rate (%)"] = (
    df["Comments"] / df["Views"] * 100
)

# Top 10 videos by like rate
top_like_rate = df.nlargest(10, "Like_Rate (%)")

print("\n===== TOP 10 VIDEOS BY LIKE RATE =====")
print(
    top_like_rate[
        ["Video_Title", "Artist_Channel", "Views",
         "Likes", "Like_Rate (%)"]
    ].to_string(index=False, formatters={
        "Like_Rate (%)": "{:.2f}%".format
    })
)

# Top 10 videos by comment rate
top_comment_rate = df.nlargest(10, "Comment_Rate (%)")

print("\n===== TOP 10 VIDEOS BY COMMENT RATE =====")
print(
    top_comment_rate[
        ["Video_Title", "Artist_Channel", "Views",
         "Comments", "Comment_Rate (%)"]
    ].to_string(index=False, formatters={
        "Comment_Rate (%)": "{:.3f}%".format
    })
)

# Overall engagement
print("\n===== OVERALL ENGAGEMENT =====")
print("Videos analyzed:", len(df))
print(f"Average like rate: {df['Like_Rate (%)'].mean():.2f}%")
print(f"Average comment rate: {df['Comment_Rate (%)'].mean():.3f}%")
