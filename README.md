# Automate Data Pipeline

A small, automated data pipeline that downloads the [iTunes Music Dataset](https://www.kaggle.com/datasets/ashyou09/itunes-music-dataset) from Kaggle on a weekly schedule and commits a fresh copy to this repository using GitHub Actions.

## How it works

1. **Extract** – `AutomateRun.py` uses [`kagglehub`](https://github.com/Kaggle/kagglehub) to download the latest version of the `ashyou09/itunes-music-dataset` dataset.
2. **Load** – the CSV is read into a pandas DataFrame and a preview is printed to the log.
3. **Save** – the data is written to `itunes_music_dataset_saved.csv` in the repository root.
4. **Commit** – the GitHub Actions workflow commits any changes and pushes them back to `main`.

## Repository structure

```
.
├── .github/workflows/actions.yaml   # Scheduled GitHub Actions workflow
├── AutomateRun.py                   # Download + save script
├── itunes_music_dataset_saved.csv   # Latest copy of the dataset
└── requirements.txt                 # Python dependencies
```

## Dataset

`itunes_music_dataset_saved.csv` contains roughly 4,900 tracks with the following columns:

`track_id`, `track_name`, `artist_name`, `collection_name`, `album_artist`, `genre`, `rating`, `track_price`, `collection_price`, `release_date`, `track_time_millis`, `country`, `currency`, `preview_url`, `artwork_url`

## Automation schedule

The workflow in `.github/workflows/actions.yaml` runs:

- **Every Thursday at 09:30 UTC** (`cron: '30 9 * * 4'`)
- **On demand** – from the **Actions** tab, select *run AutomateRun.py* and click **Run workflow**.

## Running locally

Requires Python 3.9+.

```bash
git clone https://github.com/A-Ighalo/Automate-Data-Pipeline.git
cd Automate-Data-Pipeline
pip install -r requirements.txt
python AutomateRun.py
```

The script writes `itunes_music_dataset_saved.csv` to the current directory. If Kaggle requires authentication for your environment, set up your credentials as described in the [kagglehub docs](https://github.com/Kaggle/kagglehub#authenticate).
