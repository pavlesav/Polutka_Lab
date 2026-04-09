"""
League configurations for Polutka Lab.

Each league is a dict with IDs, names, and API metadata.
Notebooks only need: LEAGUE = 'cg' at the top — all paths derive from that.
"""

LEAGUES = {
    "cg": {
        "name": "1. CFL",
        "country": "Montenegro",
        "tournament_id": 154,
        "season_id": 78078,
        "sofascore_slug": "montenegro/1-cfl/154",
        "team_short_names": {
            37956:  "Arsenal",
            6219:   "Jedinstvo",
            6216:   "Petrovac",
            7581:   "Bokelj",
            6226:   "Dečić",
            327162: "Mladost DG",
            24312:  "Jezero",
            5143:   "Budućnost",
            6224:   "Sutjeska",
            36019:  "Mornar",
        },
    },
    "srb": {
        "name": "Mozzart Bet Superliga",
        "country": "Serbia",
        "tournament_id": 210,
        "season_id": 76909,
        "sofascore_slug": "serbia/mozzart-bet-superliga/210",
        "team_short_names": {
            282203: "Železničar",
            5150:   "Vojvodina",
            5152:   "Partizan",
            5153:   "OFK Beograd",
            25737:  "Radnički Niš",
            5144:   "Javor",
            7674:   "Napredak",
            36967:  "Spartak",
            43981:  "Radnički 1923",
            5149:   "Crvena zvezda",
            308176: "IMT",
            111127: "Radnik",
            263360: "TSC",
            5148:   "Čukarički",
            7771:   "Mladost",
            25736:  "Novi Pazar",
        },
    },
}
