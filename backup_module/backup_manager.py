from pathlib import Path
from backup_module.utils import (
    get_project_root,
    get_backup_dir,
    get_timestamp,
    get_project_name,
)
from backup_module.retention import cleanup_old_backups
import zipfile


# List available backups
def list_backups():
    project_root = get_project_root()
    backup_dir = get_backup_dir(project_root)

    if not backup_dir.exists():
        print("Project not initialized.")
        print("Run: python backup.py init")
        return

    backups = sorted(
        backup_dir.glob("*.zip"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    if not backups:
        print("No backups found.")
        return

    print("Available backups:")
    for idx, backup in enumerate(backups, start=1):
        print(f"{idx}. {backup.name}")


#`# Save a new backup`
def save_backup():
    project_root = get_project_root()
    backup_dir = get_backup_dir(project_root)

    if not backup_dir.exists():
        print("Project not initialized.")
        print("Run: python backup.py init")
        return

    timestamp = get_timestamp()
    project_name = get_project_name(project_root)
    zip_name = f"{project_name}_{timestamp}.zip"
    zip_path = backup_dir / zip_name

    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for path in project_root.rglob("*"):
                if ".backups" in path.parts:
                    continue
                if path.is_file():
                    zipf.write(path, path.relative_to(project_root))
    except Exception as e:
        print(f"Error while creating backup: {e}")
        return

    cleanup_old_backups(backup_dir)
    print(f"Backup created successfully: {zip_name}")
    
    
    
    

# Automatic backup function
def auto_backup():
    save_backup()
