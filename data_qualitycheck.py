import pandas as pd

df = pd.read_csv("indian_music_data.csv")

# Convert data types
df["Published_Date"] = pd.to_datetime(
    df["Published_Date"],
    errors="coerce",
    utc=True
)

# Display updated data types
print(df.dtypes)

# Check invalid dates
print("Invalid dates:", df["Published_Date"].isna().sum())


# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Check duplicate video IDs
print("\nDuplicate video IDs:")
print(df["Video_ID"].duplicated().sum())

# Check duplicate rows
print("\nDuplicate rows:")
print(df.duplicated().sum())


# Save cleaned dataset
df.to_csv("indian_music_data_cleaned.csv", index=False, encoding="utf-8-sig")

print("\nCleaned dataset saved successfully!")
print("Total videos:", len(df))


