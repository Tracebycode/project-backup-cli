import sys
from backup.backup_manager import list_backups, save_backup, auto_backup
from backup.initializer import init_project
from backup.restore_manager import restore_backup


# Entry point for the backup package
# This allows users to run commands directly from the command line.

def main():
    if len(sys.argv) < 2:
        print("Usage: python backup.py <command>")
        print("Available commands: init")
        sys.exit(1)

    command = sys.argv[1]

    if command == "init":
        init_project()
    elif command == "list":
        list_backups()
    elif command == "save":
        save_backup()
    elif command == "restore":
        restore_backup()
    elif command == "auto":
        auto_backup()
    else:
        print(f"Unknown command: {command}")
        print("Available commands: init, list, save, restore, auto")
        sys.exit(1)
        
   


if __name__ == "__main__":
    main()
