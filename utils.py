from rapidfuzz import process

def match_player_name(user_input, player_list):
    """
    Matches user input to the closest player name using fuzzy matching.
    Returns the best match if score > 60, else None.
    """
    match, score, _ = process.extractOne(user_input, player_list)
    return match if score > 60 else None

def estimate_player_worth(stats):
    runs = stats.get("Total Runs", 0)
    sr = stats.get("Strike Rate", 0)
    fours = stats.get("4s", 0)
    sixes = stats.get("6s", 0)

    # Simple scoring formula for estimation
    score = (runs * 0.01) + (sr * 1.5) + (fours * 0.5) + (sixes * 1.0)

    if score >= 400:
        worth = round(score / 100, 2)
        return {"Worthiness": "High", "Estimated Worth (in Cr)": worth}
    elif score >= 250:
        worth = round(score / 120, 2)
        return {"Worthiness": "Medium", "Estimated Worth (in Cr)": worth}
    else:
        worth = round(score / 150, 2)
        return {"Worthiness": "Low", "Estimated Worth (in Cr)": worth}
