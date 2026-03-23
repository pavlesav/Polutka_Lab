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
│   ├── 13_goal_mouth.ipynb                 # Goal-mouth placement analysis (heatmap, penalties, body part, zones)
│   ├── 14_sofascore_ratings.ipynb          # SofaScore ratings: Montenegrin vs foreign players
│   └── 15_open_play_goals.ipynb            # Open play vs set piece goals + team scatter plots
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
| 13 | Goal Mouth | Goal-mouth placement analysis: heatmap, penalties, body part, foot preference zones |
| 14 | SofaScore Ratings | Distribution comparison of match ratings between Montenegrin and foreign players |
| 15 | Open Play Goals | Open play vs set piece vs penalty goals — team breakdowns, conversion scatter plots, xG analysis |

## Data Sources

- **Source**: [Sofascore](https://www.sofascore.com/) API via Selenium
- **League**: Montenegrin First League (1. CFL) — Tournament ID 154
- **Season**: 2025-26

---

## Data Dictionary

Complete reference of all available datasets. Use this when planning new analyses.

### Overview

| File | Location | Rows | Cols | Grain (one row = ) |
|------|----------|------|------|--------------------|
| `league_standings.csv` | processed | 10 | 11 | One team |
| `matches_metadata.csv` | processed | 125 | 17 | One match |
| `match_team_statistics.csv` | processed | 250 | 35 | One team in one match |
| `match_player_statistics.csv` | processed | 4,974 | 72 | One player in one match |
| `player_season_statistics.csv` | processed | 292 | 47 | One player (season totals) |
| `players_metadata.csv` | processed | 329 | 10 | One player |
| `teams_metadata.csv` | processed | 10 | 3 | One team |
| `player_current_teams.json` | processed | 329 | 5 | One player |
| `matches.csv` | raw | 127 | 140 | One match (full SofaScore API dump) |
| Per-match files (×127 dirs) | raw/raw_by_match/ | varies | varies | See below |

### Teams (10)

| team_id | Full Name | Short Name |
|---------|-----------|------------|
| 37956 | FK Arsenal Tivat | Arsenal |
| 5143 | FK Budućnost Podgorica | Budućnost |
| 7581 | FK Bokelj Kotor | Bokelj |
| 6226 | FK Dečić Tuzi | Dečić |
| 6219 | FK Jedinstvo Bijelo Polje | Jedinstvo |
| 24312 | FK Jezero | Jezero |
| 327162 | Mladost DG | Mladost DG |
| 36019 | FK Mornar Bar | Mornar |
| 6216 | OFK Petrovac | Petrovac |
| 6224 | FK Sutjeska Nikšić | Sutjeska |

### Processed Files

#### `league_standings.csv` — 10 rows × 11 cols
League table snapshot.

| Column | Type | Description |
|--------|------|-------------|
| position | int | League position (1–10) |
| team_id | int | Unique team identifier |
| team_name | str | Full team name |
| played | int | Matches played |
| wins | int | Wins |
| draws | int | Draws |
| losses | int | Losses |
| goals_for | int | Goals scored |
| goals_against | int | Goals conceded |
| goal_diff | int | Goal difference |
| points | int | Total points (W×3 + D×1) |

#### `matches_metadata.csv` — 125 rows × 17 cols
One row per match with scores, formations, and timing.

| Column | Type | Description |
|--------|------|-------------|
| match_id | int | Unique match identifier (SofaScore ID) |
| round | int | Season round number |
| match_date | date | YYYY-MM-DD |
| match_datetime | datetime | YYYY-MM-DD HH:MM:SS |
| status | str | Match status (`Ended`) |
| homeTeam_id | int | Home team ID |
| homeTeam_name | str | Home team name |
| homeTeam_formation | str | Formation used (e.g. `4-2-3-1`, `3-4-2-1`) |
| awayTeam_id | int | Away team ID |
| awayTeam_name | str | Away team name |
| awayTeam_formation | str | Away team formation |
| homeScore_period1 | float | Home goals in first half |
| homeScore_period2 | float | Home goals in second half |
| homeScore_total | float | Home total goals |
| awayScore_period1 | float | Away goals in first half |
| awayScore_period2 | float | Away goals in second half |
| awayScore_total | float | Away total goals |

#### `match_team_statistics.csv` — 250 rows × 35 cols
Per-team aggregate stats for each match (2 rows per match).

| Column | Type | Description |
|--------|------|-------------|
| match_id | int | Match identifier |
| team_id | int | Team identifier |
| team_name | str | Team name |
| team_side | str | `home` or `away` |
| accurateCross | float | Accurate crosses |
| accurateLongBalls | float | Accurate long balls |
| accuratePasses | float | Accurate passes |
| accurateThroughBall | float | Accurate through balls |
| aerialDuelsPercentage | float | Aerial duels won (%) |
| ballPossession | float | Ball possession (%) |
| blockedScoringAttempt | float | Blocked scoring attempts |
| cornerKicks | float | Corner kicks |
| dispossessed | float | Times dispossessed |
| dribblesPercentage | float | Dribble success (%) |
| duelWonPercent | float | Overall duel win (%) |
| expectedGoals | float | xG (expected goals) |
| fouls | float | Fouls committed |
| freeKicks | float | Free kicks won |
| goalKicks | float | Goal kicks |
| goalkeeperSaves | float | Goalkeeper saves |
| groundDuelsPercentage | float | Ground duel win (%) |
| hitWoodwork | float | Shots hitting woodwork |
| interceptionWon | float | Interceptions won |
| offsides | float | Offsides |
| passes | float | Total passes attempted |
| redCards | int | Red cards |
| shotsOffGoal | float | Shots off target |
| shotsOnGoal | float | Shots on target |
| throwIns | float | Throw-ins |
| totalClearance | float | Total clearances |
| totalShotsInsideBox | float | Shots from inside the box |
| totalShotsOnGoal | float | Total shots on goal |
| totalShotsOutsideBox | float | Shots from outside the box |
| totalTackle | float | Total tackles |
| yellowCards | int | Yellow cards |

#### `match_player_statistics.csv` — 4,974 rows × 72 cols
Per-player per-match stats. Every player appearance is one row.

| Column | Type | Description |
|--------|------|-------------|
| match_id | int | Match identifier |
| player_id | int | Player identifier |
| player_name | str | Full player name |
| team_id | int | Team the player played for |
| team_name | str | Team name |
| player_current_team_id | int | Current team (may differ if transferred) |
| player_current_team | str | Current team name |
| team_side | str | `home` or `away` |
| position_played | str | Position: `G`, `D`, `M`, `F` |
| shirtNumber | int | Shirt number |
| substitute | bool | `True` = came off bench |
| played | bool | `True` = appeared in match |
| minutesPlayed | float | Minutes played (0–120) |
| rating | float | SofaScore match rating (typically 5.5–10) |
| goals | float | Goals scored |
| goalAssist | float | Assists |
| expectedGoals | float | xG |
| expectedAssists | float | xA |
| totalShots | float | Total shots |
| onTargetScoringAttempt | float | Shots on target |
| shotOffTarget | float | Shots off target |
| bigChanceMissed | float | Big chances missed |
| bigChanceCreated | float | Big chances created |
| keyPass | float | Key passes |
| totalPass | float | Total passes |
| accuratePass | float | Accurate passes |
| totalLongBalls | float | Long ball attempts |
| accurateLongBalls | float | Accurate long balls |
| totalCross | float | Cross attempts |
| accurateCross | float | Accurate crosses |
| accurateOwnHalfPasses | float | Passes in own half (accurate) |
| totalOwnHalfPasses | float | Passes in own half (total) |
| accurateOppositionHalfPasses | float | Passes in opp half (accurate) |
| totalOppositionHalfPasses | float | Passes in opp half (total) |
| totalDribble | float | Dribble attempts |
| successfulDribbles | float | Successful dribbles |
| totalTackle | float | Tackle attempts |
| wonTackle | float | Tackles won |
| totalContest | float | Contests |
| wonContest | float | Contests won |
| duelWon | float | Duels won |
| duelLost | float | Duels lost |
| aerialWon | float | Aerial duels won |
| aerialLost | float | Aerial duels lost |
| interceptionWon | float | Interceptions |
| totalClearance | float | Clearances |
| outfielderBlock | float | Outfielder blocks |
| ballRecovery | float | Ball recoveries |
| possessionLostCtrl | float | Possessions lost (controllable) |
| dispossessed | float | Times dispossessed |
| challengeLost | float | Challenges lost |
| fouls | float | Fouls committed |
| wasFouled | float | Times fouled |
| touches | float | Total touches |
| unsuccessfulTouch | float | Unsuccessful touches |
| totalOffside | float | Offsides |
| hitWoodwork | float | Hit woodwork |
| errorLeadToAShot | float | Errors leading to opponent shot |
| penaltyWon | float | Penalties won |
| penaltyConceded | float | Penalties conceded |
| penaltyMiss | float | Penalties missed |
| penaltySave | float | Penalties saved (GK) |
| penaltyFaced | float | Penalties faced (GK) |
| saves | float | Saves (GK) |
| savedShotsFromInsideTheBox | float | Saves from inside box (GK) |
| goodHighClaim | float | High claims (GK) |
| clearanceOffLine | float | Goal-line clearances |
| crossNotClaimed | float | Crosses not claimed (GK) |
| totalKeeperSweeper | float | Keeper sweeper actions |
| accurateKeeperSweeper | float | Accurate sweeper actions |
| ownGoals | float | Own goals |
| blockedScoringAttempt | float | Blocked shots |

#### `player_season_statistics.csv` — 292 rows × 47 cols
Season-aggregated stats per player. One row per player who appeared in the season.

| Column | Type | Description |
|--------|------|-------------|
| player_id | int | Player identifier |
| name | str | Full name |
| shortName | str | Abbreviated name |
| position | str | `G`, `D`, `M`, `F` |
| team_name | str | Team name |
| country_name | str | Nationality |
| dateOfBirth | date | YYYY-MM-DD |
| team_id | int | Team identifier |
| appearances | int | Total appearances |
| minutes_played | float | Total minutes played |
| goals | float | Goals |
| assists | float | Assists |
| xG | float | Expected goals |
| xA | float | Expected assists |
| total_shots | float | Shots |
| shots_on_target | float | Shots on target |
| key_passes | float | Key passes |
| big_chances_created | float | Big chances created |
| total_passes | float | Total passes |
| accurate_passes | float | Accurate passes |
| total_long_balls | float | Long ball attempts |
| accurate_long_balls | float | Accurate long balls |
| total_crosses | float | Cross attempts |
| accurate_crosses | float | Accurate crosses |
| total_tackles | float | Tackle attempts |
| tackles_won | float | Tackles won |
| interceptions | float | Interceptions |
| clearances | float | Clearances |
| ball_recoveries | float | Ball recoveries |
| blocks | float | Blocks |
| duels_won | float | Duels won |
| duels_lost | float | Duels lost |
| aerial_won | float | Aerials won |
| aerial_lost | float | Aerials lost |
| fouls_committed | float | Fouls committed |
| fouls_won | float | Fouls drawn |
| dribbles_successful | float | Successful dribbles |
| dribbles_total | float | Dribble attempts |
| avg_rating | float | Season average SofaScore rating |
| minutes_per_game | float | Avg minutes per appearance |
| pass_accuracy | float | Pass accuracy (%) |
| shot_accuracy | float | Shot accuracy (%) |
| dribble_success_rate | float | Dribble success (%) |
| duel_success_rate | float | Duel win (%) |
| goals_per_90 | float | Goals per 90 minutes |
| assists_per_90 | float | Assists per 90 minutes |
| has_player_photo | bool | Photo available in player_photos/ |

#### `players_metadata.csv` — 329 rows × 10 cols
Static player biographical info.

| Column | Type | Description |
|--------|------|-------------|
| id | int | Player identifier |
| name | str | Full name |
| shortName | str | Abbreviated name |
| position | str | `G` (Goalkeeper), `D` (Defender), `M` (Midfielder), `F` (Forward) |
| height | float | Height in cm |
| country_name | str | Nationality (15 countries — see below) |
| marketValue | float | Market value in € (some null) |
| dateOfBirth | date | YYYY-MM-DD |
| preferredFoot | str | `Right`, `Left`, or `Both` |
| has_player_photo | bool | Photo available |

**Nationalities:** Argentina, Bosnia & Herzegovina, Brazil, Croatia, Côte d'Ivoire, Ghana, Greece, Japan, Kosovo, Montenegro, Portugal, Russia, Senegal, Serbia, Slovenia

#### `teams_metadata.csv` — 10 rows × 3 cols
Team reference table.

| Column | Type | Description |
|--------|------|-------------|
| team_id | int | Unique team ID |
| team_name | str | Full club name |
| short_name | str | Abbreviated name |

#### `player_current_teams.json` — 329 entries
Player-to-team mapping with transfer tracking.

| Key | Type | Description |
|-----|------|-------------|
| player_id | int | Player identifier (also the JSON key) |
| current_team_id | int | Current team ID |
| current_team_name | str | Current team name (null if retired/released) |
| retired | bool | Whether player is retired |
| preferredFoot | str | `Right`, `Left`, or `Both` |

### Raw Per-Match Files

Each of the **127 match directories** (`data/raw/mt1cfl_2526/raw_by_match/{match_id}/`) contains:

#### `match_shots.csv` — ~15–30 rows per match
Shot-level event data with xG.

| Column | Type | Description |
|--------|------|-------------|
| player | dict/str | Nested JSON: player name, position, jersey, ID, translations |
| isHome | bool | `True` = home team shot |
| shotType | str | `goal`, `save`, `miss`, `block`, `post` |
| goalType | str | `regular` or empty |
| situation | str | `regular`, `penalty`, `free-kick`, `corner`, `set-piece`, `throw-in-set-piece`, `own-goal` |
| playerCoordinates | dict | `{x, y, z}` — pitch position of shooter |
| bodyPart | str | `right-foot`, `left-foot`, `head`, `other` |
| goalMouthLocation | str | Target zone (see values below) |
| goalMouthCoordinates | dict | `{x, y, z}` — goal mouth coordinates |
| xg | float | Expected goals value |
| xgot | float | Expected goals on target |
| id | int | Unique shot event ID |
| time | int | Match minute |
| addedTime | float | Added/stoppage time minutes (if applicable) |
| timeSeconds | int | Total seconds elapsed |
| draw | dict | Shot trajectory: `{start, end, goal, block}` coordinates |
| reversedPeriodTime | int | Time remaining in period |
| reversedPeriodTimeSeconds | int | Seconds remaining |
| periodTimeSeconds | int | Seconds into period |
| incidentType | str | Always `shot` |
| blockCoordinates | dict | Coordinates where shot was blocked (if blocked) |

**goalMouthLocation values:** `close-high`, `close-high-left`, `close-high-right`, `close-left`, `close-right`, `high`, `high-centre`, `high-left`, `high-right`, `left`, `low-centre`, `low-left`, `low-right`, `right`

#### `match_momentum.csv` — ~91–95 rows per match
Minute-by-minute momentum indicator.

| Column | Type | Description |
|--------|------|-------------|
| minute | float | Match minute (0–90+) |
| value | int | Momentum score (positive = home advantage, negative = away) |

#### `avg_positions.csv` — ~20–30 rows per match
Average field positions per player.

| Column | Type | Description |
|--------|------|-------------|
| player | dict/str | Nested JSON with player info |
| averageX | float | Average X position on pitch (0–100) |
| averageY | float | Average Y position on pitch (0–100) |
| pointsCount | int | Number of position samples |
| team | str | `home` or `away` |

#### `player_base_stats.csv` — ~20–25 rows per match
Detailed per-player match stats (similar to `match_player_statistics.csv` but raw).

65 columns including all passing, shooting, duel, defensive, and GK stats plus computed percentages (`pass_accuracy_pct`, `long_ball_accuracy_pct`, `cross_accuracy_pct`, `dribble_success_pct`, `keeper_sweeper_pct`).

#### `player_stats_tabs.csv` — ~200–300 rows per match
Stats in long format (one row per player per metric per category).

| Column | Type | Description |
|--------|------|-------------|
| match_id | int | Match identifier |
| team_id | int | Team ID |
| team_name | str | Team name |
| team_side | str | `home` or `away` |
| player_id | int | Player ID |
| player_name | str | Player name |
| player_position | str | `G`, `D`, `M`, `F` |
| metric_key | str | Stat key (e.g. `goals`, `accuratePass`, `totalTackle`) |
| category | str | `General`, `Attacking`, `Defensive`, `Passing` |
| metric | str | Display name for stat |
| value | float | Stat value |
| secondary | float | Secondary value (e.g. won out of total) |
| denominator | float | Denominator for ratios |
| percentage | float | Calculated percentage |
| display | str | Formatted display string (e.g. `23/26 (88%)`) |

#### `lineups.json`, `statistics.json`, `heatmaps.json`
Raw JSON dumps from SofaScore API — lineup details, full team stats, and player heatmap coordinates.

### Media Files

| Directory | Count | Format | Naming |
|-----------|-------|--------|--------|
| `data/processed/player_photos/` | 224 | PNG | `{player_id}.png` — circular headshots |
| `data/processed/team_logos/` | 10 | PNG | `{team_id}.png` — team crests (RGBA with transparency) |

---

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
