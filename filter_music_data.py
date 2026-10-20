
import pandas as pd

# Load refined dataset
df = pd.read_csv("indian_music_data_refined.csv")

# Terms indicating potentially unrelated content
exclude_terms = [
    "frozen/sing-along",
    "official trailer",
    "movie trailer",
    "gameplay",
    "reaction video"
]

# Combine title and channel for checking
text = (
    df["Video_Title"].fillna("") + " " +
    df["Artist_Channel"].fillna("")
).str.lower()

# Remove records matching exclusion terms
mask = ~text.apply(
    lambda value: any(term in value for term in exclude_terms)
)

filtered_df = df[mask].copy()

# Save filtered dataset
filtered_df.to_csv(
    "indian_music_data_final.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Original videos:", len(df))
print("Filtered videos:", len(filtered_df))
print("Removed videos:", len(df) - len(filtered_df))

print("\nReview all remaining video titles:")
for i, title in enumerate(filtered_df["Video_Title"], start=1):
    print(f"{i}. {title}")
