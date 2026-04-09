# CLAUDE.md - Polutka Lab

## What is this project?

Polutka Lab is a **football (soccer) analytics platform** for the **Montenegrin First League (1. CFL)** and **Serbian Superliga**. It scrapes match data from SofaScore, cleans it into structured datasets, and generates Instagram-ready visualizations (1080x1350px) for a sports analytics social media account.

Current focus: **Montenegro 1. CFL 2025-26 season** (~125 matches, 10 teams, ~300 players). Serbian Superliga support is scaffolded but secondary.

## Tech stack

- **Python 3.x** — all code
- **Jupyter Notebooks** — primary execution environment (19 notebooks in `notebooks/`)
- **pandas / numpy** — data manipulation
- **matplotlib / seaborn / plotly** — visualizations
- **mplsoccer** — pitch diagrams (shot maps, goal mouth)
- **Pillow** — image processing (circular player photos, Instagram post composition)
- **Selenium + webdriver-manager** — headless Chrome web scraping from SofaScore
- **requests** — HTTP calls for player photos and API data
- Dependencies: `requirements.txt`

## Project structure

```
Polutka_Lab/
├── CLAUDE.md                  # This file
├── README.md                  # Detailed project docs with full data dictionary
├── requirements.txt           # Python dependencies
├── .gitignore
│
├── src/                       # Shared Python utilities
│   ├── __init__.py
│   ├── config.py              # League IDs, team names, API metadata
│   └── viz.py                 # Dark theme palette, Instagram composition, radar charts
│
├── notebooks/                 # Numbered analysis pipeline (see below)
│   ├── 01_scrape.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03–19_*.ipynb          # Independent analysis notebooks
│
├── data/
│   ├── raw/{cg,srb}/          # Scraped data (never modified after scraping)
│   │   ├── matches.csv        # Flat SofaScore match dump (~140 columns)
│   │   └── raw_by_match/      # Per-match folders ({match_id}/)
│   │       └── {match_id}/    # avg_positions.csv, heatmaps.json, lineups.json,
│   │                          # match_momentum.csv, match_shots.csv,
│   │                          # player_base_stats.csv, player_stats_tabs.csv,
│   │                          # statistics.json
│   │
│   └── processed/{cg,srb}/    # Cleaned, analysis-ready datasets
│       ├── league_standings.csv
│       ├── matches_metadata.csv
│       ├── match_team_statistics.csv
│       ├── match_player_statistics.csv
│       ├── player_season_statistics.csv
│       ├── players_metadata.csv
│       ├── teams_metadata.csv
│       ├── player_current_teams.json
│       ├── player_photos/     # Circular PNG headshots ({player_id}.png)
│       └── team_logos/        # PNG team crests ({team_id}.png)
│
├── outputs/{cg,srb}/
│   ├── figures/               # Raw chart PNGs (transparent background)
│   └── final_posts/           # Instagram-ready 1080x1350 composed posts
│
├── assets/
│   ├── background.png         # Instagram template background
│   └── pfp.png                # Profile picture/logo
│
└── annotation_match_selection.ipynb  # Ad-hoc: YOLO player detection planning
```

## Data flow (pipeline order)

```
SofaScore (web)
    │  Selenium headless Chrome, rate-limited 0.3–1s
    ▼
[01_scrape.ipynb]  →  data/raw/{league}/raw_by_match/{match_id}/*
    │
    ▼
[02_data_cleaning.ipynb]  →  data/processed/{league}/*.csv + photos + logos
    │
    ▼
[03–19 analysis notebooks]  →  outputs/{league}/figures/*.png
    │  (each notebook is independent; reads from data/processed/)
    ▼
[Instagram composition]  →  outputs/{league}/final_posts/*.png
    (chart PNG + assets/background.png → 1080x1350 branded post)
```

**Execution order:** 01 (scrape) → 02 (clean) → any of 03–19 (independent) → composition step.

## Notebook index

| # | File | Purpose |
|---|------|---------|
| 01 | `scrape.ipynb` | Selenium scraper for SofaScore match data |
| 02 | `data_cleaning.ipynb` | Raw JSON/CSV → 7 processed CSVs + photos |
| 03 | `xg_over_under.ipynb` | Goals vs Expected Goals scatter plot |
| 04 | `team_age_analysis.ipynb` | Age distribution by team |
| 05 | `ven_diagram.ipynb` | Venn diagrams for skill overlaps |
| 06 | `substitute_impact.ipynb` | Substitute/bench player contributions |
| 07 | `formations.ipynb` | Formation usage visualization |
| 08 | `yellow_cards.ipynb` | Fouls per card ratio analysis |
| 09 | `stamina.ipynb` | Stoppage time goals & late-game impact |
| 10 | `penalties_viz.ipynb` | Penalty statistics & conversion rates |
| 11 | `home_vs_away.ipynb` | Home/away performance splits |
| 12 | `shot_map.ipynb` | Shot locations with xG on pitch diagrams |
| 13 | `goal_mouth.ipynb` | Goal-mouth placement heatmap |
| 14 | `sofascore_ratings.ipynb` | Montenegrin vs foreign player ratings |
| 15 | `open_play_goals.ipynb` | Open play vs set piece analysis |
| 16 | `chance_creators_outlier.ipynb` | Chance creation outlier detection |
| 17 | `player_radar_comparison.ipynb` | Percentile radar charts (player comparison) |
| 18 | `forward_radar_comparison.ipynb` | Forward-specific radar comparison |
| 19 | `top5_per_capita.ipynb` | Per-capita nationality statistics |

## Key conventions

### League switching

All notebooks use a single `LEAGUE` variable (e.g., `LEAGUE = 'cg'`) at the top. All data paths, team names, and API IDs derive from this via `src/config.py`. To switch from Montenegro to Serbia, change `LEAGUE = 'srb'`.

### Shared config (`src/config.py`)

- `LEAGUES` dict keyed by `'cg'` (Montenegro) and `'srb'` (Serbia)
- Each entry has: `tournament_id`, `season_id`, `sofascore_slug`, `team_short_names` (SofaScore ID → display name)

### Visual identity (`src/viz.py`)

- **Dark theme palette:** `BG_COLOR='#0a0a0a'`, `GOLD='#d4af37'`, `ACCENT='#f6c453'`, etc.
- **Instagram size:** 1080x1350px (4:5 aspect ratio), always
- `compose_instagram_post()` — overlays transparent chart onto branded background
- `draw_radar()` — percentile radar chart comparing two players (0–100 scale)
- All charts saved with **transparent backgrounds** so they can be composited

### File naming

- **Notebooks:** `{##}_{snake_case}.ipynb`
- **Player photos:** `{player_id}.png` (circular crop)
- **Team logos:** `{team_id}.png`
- **Raw match dirs:** `{sofascore_match_id}/`
- **CSV columns:** snake_case with suffixes like `_total`, `_average`, `_per_90`, `_pct`

### Data conventions

- **Player positions:** single letter — `G` (goalkeeper), `D` (defender), `M` (midfielder), `F` (forward)
- **Date format:** `YYYY-MM-DD` in CSVs
- **IDs:** positive integers from SofaScore API
- **Missing values:** NaN in CSVs, `null` in JSON
- Raw data in `data/raw/` is never modified after scraping

## Key processed datasets

| File | Grain | Key columns |
|------|-------|-------------|
| `matches_metadata.csv` | 1 row per match | match_id, round, homeTeam, awayTeam, scores, formations |
| `match_team_statistics.csv` | 2 rows per match (home/away) | possession, shots, passes, fouls (~35 stats) |
| `match_player_statistics.csv` | 1 row per player-match appearance | ~72 stats: minutes, goals, assists, xG, passes, duels, etc. |
| `player_season_statistics.csv` | 1 row per player-season | ~47 aggregated season totals |
| `players_metadata.csv` | 1 row per player | name, DOB, height, nationality, position |
| `teams_metadata.csv` | 1 row per team | team_id, name, short_name |
| `league_standings.csv` | 1 row per team | points, W/D/L, GF/GA |

## Git workflow

- Single `main` branch, linear history
- Short imperative commit messages
- Large data files (CSVs, PNGs) are tracked in git
- No CI/CD — manual notebook execution

## Running the project

```bash
pip install -r requirements.txt
# Then open notebooks in order: 01 → 02 → any of 03–19
```

Scraping (notebook 01) requires Chrome/Chromium installed for Selenium.
