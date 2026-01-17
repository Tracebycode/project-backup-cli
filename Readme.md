# 📦 Project Backup CLI

A lightweight system-level command-line utility to create and manage local backups of a project during development.

---

## 1. Problem Statement

While working on development projects (especially in VS Code), I often experiment with code changes that can break a previously working state. For small or experimental projects, version control systems like Git are not always initialized or used consistently.

As a result:

* I forget to save working versions
* Reverting changes becomes difficult
* I lose time fixing avoidable mistakes

There is a need for a **simple, local, and fast backup mechanism** that works directly at the file-system level without requiring external tools or frameworks.

---

## 2. Solution Overview

This project provides a **command-line backup utility** that allows developers to:

* Initialize a project for backups (similar to `git init`)
* Create timestamped ZIP snapshots of the project
* Automatically retain only the most recent backups
* Restore the project to a previous working state
* Integrate easily with VS Code run workflows

The tool is intentionally kept minimal, uses only standard libraries, and focuses on **clarity, safety, and correctness**.

---

## 3. Key Features

* 📁 Project-level backups stored locally
* ⏱ Timestamped ZIP snapshots
* ♻ Automatic retention of last *N* backups (default: 4)
* 🔄 Safe restore with user confirmation
* 🧰 Simple CLI commands
* ⚙ No external dependencies or frameworks

---

## 4. Project Structure

```
project-backup-cli/
│
├── backup.py              # CLI entry point
│
├── backup/                # Core logic
│   ├── __init__.py
│   ├── config.py          # Configuration handling
│   ├── initializer.py     # init command
│   ├── backup_manager.py  # save / auto backups
│   ├── restore_manager.py # restore logic
│   ├── retention.py       # cleanup old backups
│   └── utils.py           # shared utilities
│
├── .backups/              # Created after initialization
│   └── config.json
│
├── screenshots/           # Sample outputs
├── sample_output.txt
└── README.md
```

---

## 5. Commands & Usage

### 1️⃣ Initialize Project (Required)

Initializes the project for backups.

```bash
python backup.py init
```

This creates a `.backups/` directory and a configuration file.
All other commands require this step.

---

### 2️⃣ Create a Manual Backup

```bash
python backup.py save
```

Creates a timestamped ZIP backup of the project.

---

### 3️⃣ Automatic Backup (VS Code Integration)

```bash
python backup.py auto
```

Designed to be used as a **pre-run task** in VS Code to automatically back up the project before execution.

---

### 4️⃣ List Available Backups

```bash
python backup.py list
```

Displays all available backups in reverse chronological order.

---

### 5️⃣ Restore a Backup

```bash
python backup.py restore
```

Allows the user to select and restore a previous backup with overwrite confirmation.

---
### Usage

```md
The tool is executed from the project directory that needs to be backed up.
The backup utility itself can be located anywhere on the system.
```

### Safety

```md
The `.git` directory is excluded from backups and restore operations to avoid
permission issues and prevent corruption of Git internals.

After restoring files, open editors may need to be refreshed to reflect
filesystem changes.
```

### Auto Backup

```md
`auto` creates a backup without prompts and is intended for editor pre-run hooks.
```

---

## 6. Design Decisions

### Why a CLI Tool?

* Fast execution
* Easy automation
* Fits naturally into developer workflows

---

### Why `init` Command (Git-style)?

* Makes project state explicit
* Prevents accidental backups
* Follows proven system-tool design patterns

---

### Why Store Backups Inside the Project?

* Keeps backups isolated per project
* Simplifies restore logic
* Avoids global state and permission issues

---

### Why ZIP-based Backups?

* Single-file snapshot
* Easy to store, move, and restore
* Fully supported by standard libraries

---

### Why Only Standard Libraries?

* Ensures portability
* Avoids dependency complexity
* Aligns with internship requirements

---

## 7. Error Handling & Safety

* `.backups/` directory is excluded from backups to prevent recursion
* Restore operation requires user confirmation
* Permission and file-system errors are handled gracefully
* Invalid commands provide clear usage guidance

---

## 8. Limitations

* This tool does **not** replace Git or full version control systems
* Designed for small to medium-sized projects
* No remote or cloud backup support

---

## 9. Future Improvements

* Configurable backup limit via CLI flags
* Selective file/folder exclusion
* Incremental backups
* Cross-project global management

---

## 10. Conclusion

Although my previous experience includes full-stack projects, this utility was intentionally designed as a **small system-level tool** to demonstrate core software engineering fundamentals such as:

* Clear problem understanding
* Modular architecture
* File-system safety
* Explicit lifecycle management
* Clean and readable code

---

## Requirements

* Python 3.x
* Works on Windows, Linux, and macOS

---
