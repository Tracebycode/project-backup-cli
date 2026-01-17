from backup_module.utils import get_project_root, get_backup_dir
from backup_module.config import create_default_config

def init_project():
    project_root = get_project_root()
    backup_dir = get_backup_dir(project_root)
    config_path = backup_dir / "config.json"

    if backup_dir.exists():
        print("Project already initialized.")
        return

    try:
        backup_dir.mkdir()
        create_default_config(config_path)
    except PermissionError:
        print("Error: Permission denied while creating .backups directory.")
        return
    except Exception as e:
        print(f"Unexpected error: {e}")
        return

    print("Backup system initialized successfully.")
