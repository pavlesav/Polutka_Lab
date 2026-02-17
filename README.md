# Polutka Lab - Montenegrin First League Football Analytics

A comprehensive football analytics project analyzing the 2025-26 season of Montenegrin First League (1. CFL) using data scraped from Sofascore.

## 📊 Project Overview

This project combines web scraping, data analysis, and visualization to analyze match-level statistics, player performance, and expected goals (xG) metrics for the Montenegrin First League.

### Key Features
- **Automated data collection** from Sofascore API using Selenium
- **Player statistics** including passes, tackles, goals, assists, and ratings
- **Expected Goals (xG) analysis** for teams and matches
- **Match momentum** and shot-level data
- **Visual analytics** with custom graphics and team logos
- **Player profile photos** (209+ players)

## 📁 Project Structure

```
Polutka Lab/
├── README.md                          # This file
├── notebooks/                         # Jupyter notebooks (run in order)
│   ├── 01_scrape.ipynb               # Data collection from Sofascore
│   ├── 02_data_cleaning.ipynb        # Data preprocessing and cleaning
│   ├── 03_xg_over_under.ipynb        # xG analysis and modeling
│   └── 04_image_composition.ipynb    # Visual creation for social media
├── data/
│   ├── raw/                          # Original scraped data (do not modify)
│   │   ├── mt1cfl_2526/             # 2025-26 season data
│   │   │   ├── matches.csv          # Match metadata
│   │   │   └── raw_by_match/        # Per-match detailed data
│   │   │       └── {match_id}/      # Individual match folders
│   │   │           ├── lineups.json             # Player stats
│   │   │           ├── avg_positions.csv        # Position data
│   │   │           ├── match_shots.csv          # Shot-level data with xG
│   │   │           ├── match_momentum.csv       # Match flow
│   │   │           ├── statistics.json          # Team statistics
│   │   │           └── heatmaps.json           # Player heatmaps
│   │   ├── player_photos/           # Player profile images (209 photos)
│   │   └── team_logos/              # Team logo images
│   └── processed/                    # Cleaned and transformed data
│       └── players_metadata.csv     # Aggregated player statistics
└── outputs/
    └── figures/                      # Generated visualizations and graphics
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas numpy jupyter selenium webdriver-manager requests tqdm pillow
```

### Running the Analysis

1. **Data Collection**: Run `01_scrape.ipynb` to fetch latest data from Sofascore
   - Scrapes match statistics, player data, and photos
   - Uses Selenium for bot detection bypass
   - ~100 matches, 285 players

2. **Data Cleaning**: Run `02_data_cleaning.ipynb` to process raw data
   - Cleans and standardizes data formats
   - Creates aggregated player statistics

3. **xG Analysis**: Run `03_xg_over_under.ipynb` for expected goals analysis
   - Team performance vs xG
   - Over/under predictions

4. **Visualization**: Run `04_image_composition.ipynb` to create graphics
   - Social media ready visualizations
   - Custom branded graphics

## 📈 Data Sources

- **Primary Source**: [Sofascore](https://www.sofascore.com/)
- **League**: Montenegrin First League (1. CFL)
- **Season**: 2025-26
- **Tournament ID**: 154

### Available Data

- ✅ Match lineups and player statistics
- ✅ Average player positions
- ✅ Shot-level data with xG values
- ✅ Match momentum graphs
- ✅ Team statistics (possession, passes, etc.)
- ✅ Player heatmaps
- ✅ Player profile photos

## 🔧 Technical Notes

### Web Scraping
- Uses **Selenium WebDriver** with Chrome in headless mode
- Implements rate limiting (0.3-1s between requests)
- Screenshot-based image capture for player photos (bypasses API restrictions)
- Handles JSON and CSV data formats

### Data Structure
- **Raw data**: Never modified, preserved as scraped
- **Processed data**: Cleaned for analysis
- **Assets**: Images and visual resources
- **Outputs**: Generated visualizations

## 📝 License

This project is for educational and analytical purposes. Data is sourced from publicly available information on Sofascore.

## 🤝 Contributing

This is a personal research project. Feel free to fork and adapt for your own analysis.

## 📧 Contact

For questions or collaboration: [Your contact info]

---

**Last Updated**: February 2026  
**League**: 1. CFL (Montenegro)  
**Matches Analyzed**: ~100  
**Players Tracked**: 285
