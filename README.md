# Using uv for Python Project Management

This guide provides steps to manage and run Python projects using [uv](https://github.com/astral-sh/uv).

## 📦 Step-by-Step Guide

### 1. Initialize a New Project

```bash
uv init <project-name>
```
### 2. Add a Dependency
```bash
uv add <package-name>
```

### 3. Run a Python File
```bash
uv run <file-name>
```

### 4. Running a Standalone Script with Dependencies
```bash
uv run --with '<package-name>' <file-name>
```

### 5. Add Multiple Dependencies from a Script
```bash
uv add --script <file-name> '<package-name>' '<package-name>'
```

### 6. Example Workflow
```bash

uv init myproject
cd myproject
uv add requests
uv run main.py
uv run --with 'pandas' standalone.py
uv add --script main.py 'numpy' 'matplotlib'
```

## 📁 Project Structure

<project-name>/
├── pyproject.toml  
├── main.py  
└── README.md


## 🛠️ Requirements
Python ≥ 3.8
