# TaskForge
**TaskForge** is a simple CLI To-do List Project. We can create, read, edit, delete tasks and perform several operations.

> [!NOTE]
> The work of frontend and complete backend is not finished. It will take a little time as I have to manage other projects and studies too.

## List of Contents
1. [TaskForge](#taskforge)
2. [Description](#description)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Description
**TaskForge** is a to-do CLI Project. We can perform **CRED** (Create, Read, Edit, Delete) operations on tasks. It has colored our, optimized code, and we can export our tasks into **JSON** or **CSV** files. I've created a web app too. We can manage tasks using web app. We can sync our **CLI** tasks with server to stay updated.

## Installation
This is step-by-step guide to install and run the project locally:
### 1. Clone the Repository
```bash
git clone https://github.com/SyntaxCorporation/taskforge.git
cd taskforge
```
### 2. Run Installation Script
```bash
chmod +x install.sh
./install.sh
```

## Usage
These are the simple commands to use **TaskForge**:
```bash
taskforge --version
taskforge --help
```
It has multiple sub-commands:
1. [Add](#add-command)
2. [List](#list-command)
3. [Delete](#delete-command)
4. [Edit](#edit-command)
5. [Done](#done-command)
6. [Undone](#undone-command)
7. [Find](#find-command)
8. [Info](#info-command)
9. [Clear](#clear-command)
10. [Sync](#sync-command)
11. [Export](#export-command)
12. [Import](#import-command)

We can use this command for more details
```bash
taskforge [sub-command] --help
```
For example:
```bash
taskforge add --help
taskforge export --help
```

### Add Command
This sub-command adds a task to the database.
Example:
```bash
taskforge add "Task 1" --tags "Tag 1" "Tag 2" --due 2026-04-01 --note "This tasks needs to be done by me"
```

### List Command
This sub-command lists all tasks. We can apply filter and sort tasks.
Example:
```bash
taskforge list
taskforge list --due-before 2026-01-01 --sort due --reverse
```

### Delete Command
We can delete a specific tasks with the help of its **Task ID** using **Delete** command.
Example:
```bash
taskforge delete 4826
taskforge delete 4736 4729 3626
```

### Edit Command
We can edit task information using **Edit** command.
Example:
```bash
taskforge edit 7369 --title "New Title" --tags "New Tag"
```

### Done Command
We can mark task(s) as done using this command.
Example:
```bash
taskforge done 5838
taskforge done 4747 2858 8562
```

### Undone Command
This command is used to mark task(s) as undone.
Example:
```bash
taskforge undone 5828
taskforge undone 3961 4829 4818
```

### Find Command
It helps in finding a task if you don't the **Task ID**.
Example:
```bash
taskforge find --tags "shopping" "grocery" --due-before 2026-03-4 --status pending
```
### Info Command
It shows the full details of a task or multiple tasks using their **Task ID**.
Example:
```bash
taskforge info 4737
taskforge info 9672 4619 5726
```
### Clear Command
This command clears your all tasks.
Example:
```bash
taskforge clear
# It will not work directly. This feature is implemented to prevent accidental clear.
# Use --confirm option to clear
taskforge clear --confirm
```
### Sync Command
This command synchronises your local **CLI** tasks with server tasks.
#### 1. Pull
This option pulls tasks from server. It only fetches those tasks which are not available in local database or the tasks that are updated using frontend.
Example:
```bash
taskforge sync --pull
```
#### 2. Push
This option pushes local tasks to server. This sends those tasks which are either not present in server database or local database has the updated task.
Example:
```bash
taskforge sync --push
```
#### 3. Match
This option matched tasks on both the local database and server database.
Example:
```bash
taskforge sync --match
```
### Export Command
This command exports the tasks details to a **JSON** or **CSV** file.
Example:
```bash
taskforge export --format json --file ./backup/tasks.json

# '--file' option is used for export path
```
### Import Command
This command is used to import tasks from a exported **JSON** or **CSV** to local database.
Example:
```bash
taskforge import --format json --file ./backup/tasks.json
```

## Features

- Adding tasks
- Editing tasks
- Finding tasks
- Deleting tasks
- Listing tasks
- Importing and Export tasks
- Syncing tasks with Server
- Searching and Sorting tasks
- Manage tasks using frontend

## Contributing

Contributions are welcome and encouraged. This project improves through community input, whether small fixes or substantial enhancements.

### Ways to Contribute
- **Report bugs**
  Clearly describe the issue, expected behavior, and steps to reproduce.

- **Suggest improvements**
  Propose better approaches, optimizations, or new features.

- **Submit pull requests**
  Fix issues, improve documentation, or add functionality.

- **Review code**
  Provide constructive feedback on open pull requests.

- **Enhance documentation**
  Clarify existing content or add missing details.

### Guidelines
- Keep changes focused and well-documented.
- Follow existing code style and structure.
- Write meaningful commit messages.
- Test your changes before submitting.

### Getting Started
1. Fork the repository
2. Create a new branch (`feature/your-feature` or `fix/issue-name`)
3. Make your changes
4. Commit your changes (`git commit -m "Add feature"`)
5. Push to your branch (`git push origin your-branch`)
6. Open a Pull Request with a clear description

---

Every contribution matters. Even small improvements add value.

## License
**TaskForge** is licensed under the Apache-2.0 License. See the [LICENSE](LICENSE) for more information.

## Contact
📧 E-mail: blackhydra.developer@gmail.com
💻 Github: [https://github.com/SyntaxCorporation](https://github.com/SyntaxCorporation )