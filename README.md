
**Quote Formatter**

A simple script that monitors the clipboard and formats straight quotes to curly quotes in real-time.

**Features**

* Replaces straight quotes with curly quotes using Unicode escape sequences
* Monitors the clipboard for changes and formats quotes automatically
* Supports left and right double quotes, as well as left and right single quotes
* Runs continuously until stopped with Ctrl+C

**Usage**

1. Save this script as a Python file (e.g. `quote_formatter.py`)
2. Run the script using Python (e.g. `python quote_formatter.py`)
3. The script will start monitoring the clipboard and formatting quotes
4. To stop the script, press Ctrl+C

**Requirements**

* Python 3
* `pyperclip` library (install with `pip install pyperclip`)

**How it Works**

The script uses the `pyperclip` library to monitor the clipboard and retrieve the current contents. It then checks if the contents have changed since the last check, and if so, formats the quotes using the `format_quotes` function. The formatted contents are then copied back to the clipboard.

**Note**

This script will continue to run until stopped with Ctrl+C. If you want to run the script in the background, you can use a tool like `screen` or `nohup` to keep it running.