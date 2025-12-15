import json
from pathlib import Path

def portfolio_config(request):
    config_path = Path(__file__).resolve().parent.parent / "portfolio.config.json"

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # IMPORTANT: match JSON structure
    return {
        "config": data.get("Config", {})
    }
