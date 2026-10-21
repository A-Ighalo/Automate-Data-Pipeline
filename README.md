# iTunes Songs Pipeline

A small data pipeline that pulls an artist's songs from the iTunes Lookup API and saves them as CSV and JSON. It currently tracks the artist Rema (iTunes artist ID `1304716885`).

The project is being built in stages. Stage one, extracting and saving the data with Python, is done. Later stages add cloud storage, dbt models, and scheduled runs on GitHub Actions. See [Planned enhancements](#planned-enhancements).

## How it works

The pipeline lives in [`Itues_pipeline.py`](Itues_pipeline.py) and runs in three steps:

1. **Extract.** `Song.main()` calls the iTunes Lookup API for the artist, asking for up to 200 songs.
2. **Transform.** `Song.TransformData()` drops the artist profile row and keeps only results where `wrapperType` is `"track"`.
3. **Save.** `Song.SaveData()` creates `data_folder/` if needed and writes the songs to both formats.

| File | Contents |
|---|---|
| `data_folder/songs.csv` | One row per song, 35 columns |
| `data_folder/songs.json` | The same songs as a JSON list |

Each run overwrites both files with the latest data from the API.

## Running it locally

Requires Python 3.9 or newer.

```bash
python3 -m venv itunes
source itunes/bin/activate
pip install -r requirements.txt
python Itues_pipeline.py
```

To pull a different artist, change the ID passed to `Song` at the bottom of the script:

```python
song = Song(ArtistId=1304716885)
```

You can find an artist's ID in their Apple Music URL, for example `https://music.apple.com/us/artist/rema/1304716885`.

## Output columns

The CSV keeps every field iTunes returns for a song. The most useful ones are:

| Column | Description |
|---|---|
| `trackId` | Unique ID for the song |
| `trackName` | Song title |
| `artistName` | Credited artists, including features |
| `collectionName` | Album or single the song belongs to |
| `releaseDate` | Release date in UTC |
| `trackTimeMillis` | Song length in milliseconds |
| `trackPrice` | Price in the store's currency |
| `primaryGenreName` | Genre, for example Afrobeats |
| `trackExplicitness` | Whether the song is explicit |
| `previewUrl` | Link to a short audio preview |

## Planned enhancements

The goal is a free, automated pipeline: Python loads raw data into MotherDuck, and dbt cleans and models it.

```
iTunes API  →  Python (extract + load)  →  MotherDuck (raw)  →  dbt (clean, test, model)  →  analytics tables
```

- **Load raw data into MotherDuck.** Store each API response untouched in a free cloud DuckDB database.
- **Add a dbt project.** Clean, deduplicate and test the data, then build `dim_artists` and `fct_tracks` tables.
- **Update dependencies.** Pin `requests`, `duckdb` and `dbt-duckdb` in `requirements.txt`.
- **Automate weekly runs.** Run the loader and `dbt build` every Thursday on GitHub Actions.
- **Add CI checks.** Test the loader and dbt models on every push and pull request.
- **Orchestrate with Airflow.** Add an Airflow DAG that runs the load and dbt steps.
