# Polutka Lab — Montenegrin First League Football Analytics

Football analytics project analyzing the **2025-26 Montenegrin First League (1. CFL)** season. Data scraped from Sofascore, cleaned into structured datasets, and visualized as Instagram-ready posts.

**Season coverage:** 19 rounds · 95+ matches · 10 teams · 285+ players

## Project Structure

```
Polutka Lab/
├── notebooks/                              # Jupyter notebooks (run in order)
│   ├── 00_image_composition.ipynb          # Compose charts onto Instagram backgrounds
│   ├── 01_scrape.ipynb                     # Selenium scraper for Sofascore
│   ├── 02_data_cleaning.ipynb              # Raw → processed data pipeline
│   ├── 03_xg_over_under.ipynb              # Goals vs Expected Goals (xG) scatter
│   ├── 04_team_age_analysis.ipynb          # Age distribution by team (weighted by minutes)
│   ├── 05_ven_diagram.ipynb                # Venn diagrams: attacking & defensive skill overlaps
│   ├── 06_substitute_impact.ipynb          # Goals + assists from bench players
│   ├── 07_formations.ipynb                 # Formation usage frequency on pitch diagrams
│   ├── 08_yellow_cards.ipynb               # Fouls per yellow card ratio
│   ├── 09_stamina.ipynb                    # Stoppage time goals & late-game impact
│   ├── 10_penalties_viz.ipynb              # Penalty statistics & conversion rates
│   ├── 11_home_vs_away.ipynb               # Home vs away performance comparison
│   ├── 12_shot_map.ipynb                   # Shot maps on pitch diagrams with xG
│   └── 13_goal_mouth.ipynb                 # Goal-mouth placement analysis (heatmap, penalties, body part, zones)
├── data/
│   ├── raw/mt1cfl_2526/                    # Original scraped data (do not modify)
│   │   ├── matches.csv                     # Match list with IDs, teams, scores
│   │   └── raw_by_match/{match_id}/        # Per-match folders containing:
│   │       ├── lineups.json                #   Player stats, formations, substitutions
│   │       ├── match_shots.csv             #   Shot-level data with xG values
│   │       ├── avg_positions.csv           #   Average player field positions
│   │       ├── match_momentum.csv          #   Goal/event timeline
│   │       ├── statistics.json             #   Team-level stats
│   │       ├── heatmaps.json               #   Player movement heatmaps
│   │       ├── player_base_stats.csv       #   Per-player match stats
│   │       └── player_stats_tabs.csv       #   Stats by category (attacking, defending, etc.)
│   └── processed/                          # Analysis-ready datasets
│       ├── league_standings.csv            # League table (10 teams)
│       ├── matches_metadata.csv            # Match info, formations, scores, datetime
│       ├── match_player_statistics.csv     # Per-player per-match stats (~2,850 rows)
│       ├── match_team_statistics.csv       # Per-team per-match stats (~190 rows)
│       ├── players_metadata.csv            # Player info: DOB, position, height, nationality
│       ├── player_season_statistics.csv    # Aggregated season stats per player
│       ├── player_current_teams.json       # Player → team assignments
│       ├── teams_metadata.csv              # Team info with short names
│       ├── player_photos/                  # 209 circular player headshots (PNG)
│       └── team_logos/                     # 10 team logos (PNG)
└── outputs/
    ├── figures/                            # Raw chart outputs + template assets
    └── final_posts/                        # Instagram 4:5 ready posts (1080×1350px)
```

## Getting Started

### Prerequisites

```bash
pip install -r requirements.txt
```

### Workflow

1. **Scrape** — Run `01_scrape.ipynb` to collect match data from Sofascore via Selenium (headless Chrome, rate-limited)
2. **Clean** — Run `02_data_cleaning.ipynb` to aggregate raw JSON/CSV into 7 processed datasets
3. **Analyze** — Run any notebook `03`–`10` for specific analyses (each is independent)
4. **Compose** — Run `00_image_composition.ipynb` to overlay charts onto branded Instagram backgrounds

## Analyses

| # | Notebook | What it does |
|---|----------|-------------|
| 03 | xG Over/Under | Scatter plot of goals vs xG — highlights overperformers (green) and underperformers (red) with player photos |
| 04 | Team Age | Stacked bars showing age distribution (U21, 21-24, 25-28, 29+) weighted by minutes played |
| 05 | Venn Diagrams | Multi-skill Venn groupings for attacking (goals/assists/dribbles) and defensive (interceptions/recoveries/clearances) players |
| 06 | Substitute Impact | Goals + assists contributed by substitutes per team |
| 07 | Formations | Top 6 most-used formations visualized on pitch diagrams |
| 08 | Yellow Cards | Fouls per yellow card ratio — identifies which teams get carded most harshly |
| 09 | Stamina | Stoppage time goals (90+), late-game impact on standings, per-team breakdowns |
| 10 | Penalties | Penalties awarded vs conceded, conversion rates, fouls by position, most fouled/aggressive players |
| 11 | Home vs Away | Points per game, goals scored/conceded split by home and away venue |
| 12 | Shot Map | All shots plotted on pitch diagrams — dot size = xG, colour = outcome (goal/save/miss/block) |

## Data Sources

- **Source**: [Sofascore](https://www.sofascore.com/) API via Selenium
- **League**: Montenegrin First League (1. CFL) — Tournament ID 154
- **Season**: 2025-26

## Tech Stack

- **Scraping**: Selenium, webdriver-manager, requests
- **Data**: pandas, numpy
- **Visualization**: matplotlib, seaborn, plotly, mplsoccer
- **Image processing**: Pillow (circular headshots, Instagram post composition)
- **Environment**: Jupyter notebooks

## Future Figure Ideas

1. **Home vs Away Performance** — Compare each team's points, goals, and xG at home vs away. Identify teams that are dominant at home but collapse on the road (or vice versa).

2. **Player Radar Charts** — Spider/radar plots comparing top players across 6-8 metrics (goals, assists, key passes, tackles, interceptions, dribbles). Great for comparing two star players side by side.

3. **Heatmap Composites** — Aggregate the per-match heatmap data you already scrape to create season-long team heatmaps showing where each team concentrates its play.

4. **Goal Sequence Patterns** — Analyze how goals are scored: open play vs set piece vs counter-attack vs penalty. Stacked bar per team showing attacking style profile.

5. **Key Passes & Chance Creation Map** — Plot key passes on a pitch diagram for top creators. You have the positional data — this would be a compelling spatial visualization.

6. **Points Gained from Losing Positions** — Track matches where teams came from behind. Which teams are the best comeback teams? Bar chart with points gained from losing vs winning positions.

7. **Player Minutes Distribution** — Show how each team uses its squad depth: what % of total minutes go to the top 11 vs the rest? Identifies teams that rotate vs those relying on a fixed XI.

8. **Referee Analysis** — Cross-reference yellow cards, fouls, and penalties by referee (if available in stats). Which referees give the most cards per match?

9. **Shot Maps** — You have `match_shots.csv` with xG and coordinates. Aggregate to create shot maps (pitch diagrams with dot size = xG) per team or per top scorer.

10. **Form Curves** — Rolling 5-match average of points, xG difference, or goals per team. Line chart showing which teams are peaking vs slumping at different points in the season.

## Technical Notes

- Selenium uses headless Chrome with rate limiting (0.3-1s between requests)
- Player photos are captured as circular crops via PIL
- All visualizations use a consistent dark theme (#0a0a0a background, #d4af37 gold accents)
- Output posts are sized 1080×1350px (Instagram 4:5 aspect ratio)
- Raw data is preserved as-is and never modified by analysis notebooks
