## AI File Sorter

A Python script that organizes messy folders. Instead of relying on rigid file extensions, this script uses the "Google Gemini 2.0 Flash API" to analyze file names and automatically sort them into logical categories (Images, Documents, Videos, Archives, Code, etc.).

## Features
* **AI Sorting:** Uses GenAI to understand context (e.g., knows that `Q3_Tax_Report` goes to Documents).
* **Interactive Prompt:** Asks the user exactly which folder path they want to sort.
* **Rate Limit Handling:** Built-in pauses to gracefully handle free-tier API speed limits.
* **Error Catching:** `try/except` blocks ensure the script keeps running even if a specific file fails.

##  Tech Stack
* Python 3
* `google-genai` SDK
* `shutil` & `os` for file system manipulation

## Setup & Usage
1. Clone this repository.
2. Create a virtual environment and run `pip install google-genai`.
3. Get a free API key from Google AI Studio.
4. Add your API key to the `API_KEY` variable in `ai_sorter.py`.
5. Run the script: `python3 ai_sorter.py`

## NON-AI

The Offline Version (`sorter.py`)

Alongside the AI sorter, this repository includes a lightning-fast, offline version. 
* **How it works:** Instead of asking an AI, it uses a hardcoded Python `Dictionary` to instantly map file extensions (like `.jpg` or `.pdf`) to their correct folders.
* **Why it's useful:** It requires no internet connection, no API keys, and sorts thousands of files in a fraction of a second.
* **To run it:** Simply type `python3 sorter.py` in your terminal.
