import zipfile
from backup.utils import get_project_root, get_backup_dir

def restore_backup():
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
        print("No backups available to restore.")
        return

    print("Available backups:")
    for idx, backup in enumerate(backups, start=1):
        print(f"{idx}. {backup.name}")

    try:
        choice = int(input("Select backup number to restore: "))
        selected_backup = backups[choice - 1]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    confirm = input(
        "This will overwrite current project files. Continue? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Restore cancelled.")
        return

    try:
        with zipfile.ZipFile(selected_backup, "r") as zipf:
            for member in zipf.namelist():
                if member.startswith(".backups"):
                    continue
                zipf.extract(member, project_root)
    except Exception as e:
        print(f"Error during restore: {e}")
        return

    print(f"Restore completed successfully from {selected_backup.name}")
