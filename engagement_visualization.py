
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("indian_music_data_final.csv")

# Keep videos with valid positive view counts
df = df[df["Views"] > 0].copy()

# Calculate like rate
df["Like_Rate"] = df["Likes"] / df["Views"] * 100

# ---------------------------------
# Chart 1: Views vs Likes
# ---------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(df["Views"], df["Likes"], alpha=0.6)

ax.set_title("Views vs Likes for Indian Music Videos", fontsize=15)
ax.set_xlabel("Views (log scale)")
ax.set_ylabel("Likes")
ax.set_xscale("log")

ax.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

# ---------------------------------
# Chart 2: Views vs Like Rate
# ---------------------------------
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(df["Views"], df["Like_Rate"], alpha=0.6)

ax.set_title("Video Views vs Like Rate", fontsize=15)
ax.set_xlabel("Views (log scale)")
ax.set_ylabel("Like Rate (%)")
ax.set_xscale("log")

ax.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()
