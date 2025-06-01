# Using uv for Python Project Management

This guide provides steps to manage and run Python projects using [uv](https://github.com/astral-sh/uv).

## 📦 Step-by-Step Guide

### 1. Initialize a New Project

```bash
uv init <project-name>
```

uv add <package-name>
uv run <file-name>
uv run --with '<package-name>' <file-name>
uv add --script <file-name> '<package-name>' '<package-name>'

uv init myproject
cd myproject
uv add requests
uv run main.py
uv run --with 'pandas' standalone.py
uv add --script main.py 'numpy' 'matplotlib'
```
