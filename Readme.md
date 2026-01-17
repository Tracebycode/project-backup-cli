# 📦 Project Backup CLI

A lightweight, system-level command-line utility for creating and managing local backups of a project during development.

---

## 1. Problem Statement

While working on development projects (especially in VS Code), I often experiment with code changes that can break a previously working state. For small or experimental projects, version control systems like Git are not always initialized or used consistently.

As a result:

* Working versions are lost
* Rolling back changes becomes difficult
* Time is wasted fixing avoidable mistakes

There is a need for a **simple, fast, and local backup mechanism** that works directly at the file-system level without relying on external tools or frameworks.

---

## 2. Solution Overview

This project implements a **command-line backup utility** that enables developers to:

* Explicitly initialize a project for backups (Git-style lifecycle)
* Create timestamped ZIP snapshots of the project
* Automatically retain only the most recent backups
* Restore the project to a previous working state
* Integrate seamlessly with editor workflows such as VS Code

The tool is intentionally minimal and focuses on **clarity, safety, and correctness**, using only standard libraries.

---

## 3. Key Features

* 📁 Local, project-scoped backups
* ⏱ Timestamped ZIP snapshots
* ♻ Automatic retention of the last *N* backups (default: 4)
* 🔄 Safe restore with explicit user confirmation
* 🧰 Simple and predictable CLI commands
* ⚙ No external dependencies or frameworks

---

## 4. Project Structure

```
backtrack/
│
├── backup.py              # CLI entry point
│
├── backup_module/         # Core backup logic
│   ├── __init__.py
│   ├── config.py          # Configuration handling
│   ├── initializer.py     # init command logic
│   ├── backup_manager.py  # save / auto backup logic
│   ├── restore_manager.py # restore logic
│   ├── retention.py       # Backup retention policy
│   └── utils.py           # Shared utilities
│
├── .backups/              # Created after initialization
│   └── config.json
│
└── backup-cli.bat         # Windows CLI wrapper

```

---

## 5. How to Run the Program

### Usage Model (Important)

* The tool operates on the **current working directory**
* The directory where the command is executed is treated as the **project root**
* The backup utility itself can be located anywhere on the system

---

### Option 1: Run Using PATH (Recommended)

For convenience, the backup tool directory can be added to the system `PATH`.
This allows the command to be executed from any project directory.

**Steps (Windows):**

1. Add the tool directory to the `Path` environment variable:

   ```
   C:\Users\ASUS\Desktop\project-backup-cli
   ```
2. Restart the terminal.
3. Navigate to the project you want to back up:

   ```bash
   cd path/to/your/project
   ```
4. Run commands:

   ```bash
   backup-cli init
   backup-cli save
   backup-cli list
   backup-cli restore
   ```

---

### Option 2: Run Using Full Path (No PATH Setup)

If the tool directory is not added to `PATH`, it can be executed using its full path.

```bash
cd path/to/your/project
python C:\Users\ASUS\Desktop\project-backup-cli\backup.py init
```

The current working directory is treated as the project root.

---

## 6. Commands & Usage

### Initialize Project (Required)

```bash
backup-cli init
```

Initializes the project by creating a `.backups/` directory and configuration file.
All other commands require this step.

---

### Create a Manual Backup

```bash
backup-cli save
```

Creates a timestamped ZIP snapshot of the current project state.

---

### Automatic Backup (Editor Integration)

```bash
backup-cli auto
```

Creates a backup without user prompts.
Designed to be used as a **pre-run task** in editors like VS Code.

---

### List Available Backups

```bash
backup-cli list
```

Displays available backups in reverse chronological order.

---

### Restore a Backup

```bash
backup-cli restore
```

Allows the user to select and restore a previous snapshot with overwrite confirmation.

---


## 📸 Sample Output (Screenshots)

The `screenshots/` directory contains sample outputs demonstrating the tool in action, including:

* Project initialization (`init`)
* Backup creation (`save`)
* Listing available backups (`list`)
* Restore flow with confirmation (`restore`)
* Interaction with Git-initialized projects

These screenshots provide visual confirmation of correct behavior and expected CLI output.

```
screenshots/
├── init.png
├── save.png
├── list.png
├── restore.png
```

---
---

## 7. Safety & Design Considerations

* The `.git` directory is explicitly excluded from backup and restore operations to avoid permission issues and prevent corruption of Git internals
* The `.backups/` directory is excluded from Git using `.gitignore`
* Restore operations require explicit user confirmation
* Open editors may need to be refreshed after restoring files to reflect filesystem changes

---

## 8. Design Decisions

### Why a CLI Tool?

* Fast execution
* Easy automation
* Natural fit for developer workflows

### Why a Git-style `init` Lifecycle?

* Makes project state explicit
* Prevents accidental operations
* Follows proven system-tool patterns

### Why ZIP-based Snapshots?

* Single-file backups
* Easy to store and restore
* Fully supported by standard libraries

### Why Only Standard Libraries?

* Ensures portability
* Avoids dependency overhead
* Aligns with internship requirements

---

## 9. Error Handling

* Clear messages for uninitialized projects
* Graceful handling of filesystem and permission errors
* Safe handling of invalid user inputs
* No destructive operations without confirmation

---

## 10. Limitations

* This tool does **not** replace Git or version control systems
* Intended for small to medium-sized projects
* No remote or cloud backup support

---

## 11. Future Improvements

* Configurable backup limits
* Custom exclusion rules
* Incremental backups
* Cross-project backup management

---

## 12. Conclusion

Although my prior experience includes full-stack development, this project was intentionally designed as a **small system-level utility** to demonstrate core software engineering fundamentals:

* Clear problem understanding
* Clean and modular design
* File-system safety
* Explicit lifecycle management
* Practical error handling

---

## Requirements

* Python 3.x
* Works on Windows, Linux, and macOS

---