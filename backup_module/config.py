import json
from datetime import datetime
from pathlib import Path

# Default configuration values
DEFAULT_CONFIG = {
    "backup_limit": 4,
    "tool_version": "1.0"
}

# Create a default configuration file
def create_default_config(config_path: Path):
    config = DEFAULT_CONFIG.copy()
    config["created_at"] = datetime.now().isoformat()

    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)
