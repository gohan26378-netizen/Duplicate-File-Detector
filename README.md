# 🔍 Duplicate File Detector

**A Python-based tool that identifies duplicate files using SHA-256 hashing and Hash Maps.**

Find duplicate files, organize file comparisons, and understand how Data Structures and Algorithms can solve real-world storage problems.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Algorithm](https://img.shields.io/badge/Algorithm-SHA--256-orange)
![DSA](https://img.shields.io/badge/Concepts-Hash%20Maps-green)
![Status](https://img.shields.io/badge/Project-Completed-success)

---
 Overview

Duplicate files can unnecessarily consume storage space and make file management difficult.

**Duplicate File Detector** is a lightweight Python application that scans a specified directory, calculates the SHA-256 hash of each file, and groups files that produce matching hash values.

Instead of comparing filenames, the application compares file content through cryptographic hashing.

The project demonstrates the practical application of **Hashing, Hash Maps, Dictionaries, and File Handling** in solving a real-world problem.

 Key Features

- **Directory Scanning:** Scans files within a selected folder, including its subfolders.
- **SHA-256 Hashing:** Generates hash values to identify files with matching content.
- **Hash Map Implementation:** Uses Python dictionaries to efficiently organize files by hash value.
- **Duplicate Grouping:** Groups files that have matching hash values.
- **Duplicate Summary:** Displays the total number of duplicate groups and extra copies.
- **Error Handling:** Handles files that cannot be accessed or read.
- **Non-Destructive:** Identifies duplicates without automatically deleting any files.

 How It Works

The application follows a simple hashing-based approach:

1. The user enters the directory path.
2. The program checks whether the directory exists.
3. Each file is opened in binary mode.
4. The SHA-256 algorithm calculates a hash value for each file.
5. A Python dictionary stores file paths using their hash values as keys.
6. Files associated with the same hash value are grouped as potential duplicates.
7. The program displays the duplicate groups and summary.

 Workflow

```text
       Start
         |
         v
  Enter Folder Path
         |
         v
  Validate Directory
         |
         v
  Scan All Files
         |
         v
 Calculate SHA-256 Hash
         |
         v
 Store Hash in Dictionary
         |
         v
 Find Matching Hashes
         |
         v
 Display Duplicate Groups
         |
         v
        End
```

 Data Structures & Algorithms

This project applies fundamental DSA concepts in a practical implementation.

| Concept | Implementation |
|---|---|
| Hashing | SHA-256 generates a hash for each file. |
| Hash Map | Python dictionary stores file paths against hash values. |
| Lists | Store multiple file paths belonging to the same hash. |
| Iteration | Traverses directories and processes files. |
| File Handling | Reads files in binary mode using Python's `open()`. |

 Why Hashing?

Comparing complete files directly can be expensive, especially when working with large files.

Hashing converts file content into a fixed-length digest. Files with identical content produce matching SHA-256 digests.

This makes hashing useful for grouping potential duplicate files.

 Tech Stack

- **Programming Language:** Python
- **Hashing Algorithm:** SHA-256
- **Libraries:** `hashlib`, `os`
- **Development Environment:** Visual Studio Code
- **Version Control:** Git and GitHub

No external Python packages are required.
Project Structure

```text
Python-Duplicate-File-Detector/
│
├── main.py              # Main application
│
├── detector.py          # Duplicate detection logic
│
├── test_files/          # Sample files for testing
│   ├── file1.txt
│   ├── file2.txt
│   └── file3.txt
│
├── README.md            # Project documentation
│
└── .gitignore           # Git ignored files
```

 Getting Started

Follow these steps to run the project locally.

 Prerequisites

- Python 3.10 or later
- Git (optional, for cloning the repository)

Check your Python installation:

```bash
python --version
```

On Windows, you can also use:

```powershell
py --version
```

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Python-Duplicate-File-Detector.git
```

### 2. Navigate to the Project Directory

```bash
cd Python-Duplicate-File-Detector
```

### 3. Run the Application

On Windows:

```powershell
py main.py
```

On Linux or macOS:

```bash
python3 main.py
```

### 4. Enter the Directory Path

When prompted:

```text
Enter folder path:
```

Enter:

```text
test_files
```

The application will scan the folder and display the detected duplicates.

## 💻 Sample Output

For testing, the project contains three sample files:

| File | Content |
|---|---|
| file1.txt | Hello, this is my DSA project. |
| file2.txt | Hello, this is my DSA project. |
| file3.txt | Python is an interesting language. |

Expected terminal output:

```text
Duplicate files found:

Duplicate Group:
 - test_files\file1.txt
 - test_files\file2.txt

Total duplicate groups: 1
Extra duplicate files: 1
```

**Result:** `file1.txt` and `file2.txt` are identified as duplicates because they contain identical data.

## 📈 Complexity Analysis

Let:

- `N` = Number of files
- `S` = Total number of bytes processed across all files

| Operation | Complexity |
|---|---|
| Hash calculation | O(file size) |
| Processing all files | O(S) |
| Dictionary insertion | O(1) average per file |
| Duplicate grouping | O(N) |
| Overall processing | O(S + N) expected |

The overall processing time depends primarily on the total size of the files being scanned.

## 🔮 Future Enhancements

The following features can extend the functionality of this project:

- [ ] Graphical User Interface using Tkinter.
- [ ] Display duplicate file sizes.
- [ ] Calculate potential storage savings.
- [ ] Filter files by extension.
- [ ] Export duplicate reports in CSV or TXT format.
- [ ] Add a file preview option.
- [ ] Compare file contents byte by byte to verify matching hashes.
- [ ] Add progress tracking for large directories.

## ⚠️ Limitations

- The current application identifies potential duplicates based on matching SHA-256 hashes.
- Hash collisions are theoretically possible, although extremely unlikely.
- A byte-by-byte comparison can provide additional verification.
- The application currently works through a command-line interface.
- It identifies duplicates but does not automatically delete files.

 Learning Outcomes

Through this project, I explored:

- Practical implementation of Hash Maps using Python dictionaries.
- Understanding how hashing algorithms work.
- File handling and directory traversal.
- Applying DSA concepts to a real-world problem.
- Organizing Python applications into multiple modules.
- Building and documenting a project for GitHub.

## 👩‍💻 Author

PRIYANKA PRASAD

Computer Science Engineering Student | AI & Machine Learning Enthusiast

GitHub: [@YOUR-GITHUB-USERNAME](https://github.com/YOUR-GITHUB-USERNAME)

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python and a practical application of Data Structures & Algorithms.**
