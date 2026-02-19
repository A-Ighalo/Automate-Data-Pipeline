import kagglehub
import pandas as pd

# Download latest version

path = kagglehub.dataset_download("ashyou09/itunes-music-dataset")

print("Path to dataset files:", path)

# load the dataset
df = pd.read_csv(path + "/itunes_music_dataset.csv")

print(df.head())

# Save the DataFrame as a CSV file in the current directory
df.to_csv("itunes_music_dataset_saved.csv", index=False)
print("DataFrame saved as itunes_music_dataset_saved.csv")

