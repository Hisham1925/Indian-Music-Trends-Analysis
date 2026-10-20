
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# Load dataset
df = pd.read_csv("indian_music_data_final.csv")

df["Published_Date"] = pd.to_datetime(
    df["Published_Date"], utc=True
)

# ---------------------------------
# Chart 1: Top 10 Videos by Views
# ---------------------------------
top_videos = df.nlargest(10, "Views").sort_values("Views")

fig, ax = plt.subplots(figsize=(14, 8))

bars = ax.barh(
    top_videos["Video_Title"],
    top_videos["Views"]
)

ax.set_title("Top 10 Music Videos by Views", fontsize=16, pad=15)
ax.set_xlabel("Views")
ax.set_ylabel("Video Title")
ax.xaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f"{x:,.0f}")
)

ax.bar_label(
    bars,
    labels=[f"{v:,.0f}" for v in top_videos["Views"]],
    padding=5,
    fontsize=9
)

ax.set_xlim(0, top_videos["Views"].max() * 1.18)
ax.grid(axis="x", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()


# ---------------------------------
# Chart 2: Top 10 Channels by Views
# ---------------------------------
top_channels = (
    df.groupby("Artist_Channel")["Views"]
    .sum()
    .nlargest(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(14, 7))

bars = ax.barh(top_channels.index, top_channels.values)

ax.set_title(
    "Top 10 Channels by Total Views in Collected Videos",
    fontsize=16,
    pad=15
)
ax.set_xlabel("Total Views")
ax.set_ylabel("Channel")
ax.xaxis.set_major_formatter(
    ticker.FuncFormatter(lambda x, _: f"{x:,.0f}")
)

ax.bar_label(
    bars,
    labels=[f"{v:,.0f}" for v in top_channels.values],
    padding=5,
    fontsize=9
)

ax.set_xlim(0, top_channels.max() * 1.18)
ax.grid(axis="x", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)
plt.tight_layout()
plt.show()




# ---------------------------------
# Chart 3: Videos Published by Year
# Line Chart
# ---------------------------------
yearly_videos = (
    df.groupby(df["Published_Date"].dt.year)
    .size()
)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    yearly_videos.index,
    yearly_videos.values,
    marker="o",
    linewidth=2,
    markersize=7
)

ax.set_title(
    "Music Video Publishing Trend by Year",
    fontsize=16,
    pad=15
)
ax.set_xlabel("Publication Year")
ax.set_ylabel("Number of Videos")

# Display every year as a whole-number tick
ax.set_xticks(yearly_videos.index)

# Add data labels above each point
for year, count in yearly_videos.items():
    ax.annotate(
        f"{count:,}",
        (year, count),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center",
        fontsize=10
    )

ax.yaxis.set_major_locator(
    ticker.MaxNLocator(integer=True)
)

ax.set_ylim(bottom=0, top=yearly_videos.max() * 1.15)
ax.grid(axis="both", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()
