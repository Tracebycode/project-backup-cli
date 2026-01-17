from pathlib import Path
from datetime import datetime


def get_project_root():
    """
    Returns the current working directory as project root.
    """
    return Path.cwd()

def get_backup_dir(project_root: Path):
    """
    Returns the .backups directory path.
    """
    return project_root / ".backups"



def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def get_project_name(project_root: Path):
    return project_root.name
