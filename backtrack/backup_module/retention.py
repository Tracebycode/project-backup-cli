def cleanup_old_backups(backup_dir, limit=4):
    backups = sorted(
        backup_dir.glob("*.zip"),
        key=lambda p: p.stat().st_mtime,
        reverse=True
    )

    for old_backup in backups[limit:]:
        old_backup.unlink()
