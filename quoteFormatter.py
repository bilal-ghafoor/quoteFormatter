import pyperclip
import time

def format_quotes(text):
    # Replace straight quotes with curly quotes using Unicode escape sequences
    text = text.replace('\u201c','"')  # Left double quote
    text = text.replace('\u201d','"')  # Right double quote
    text = text.replace('\u2018',"'")  # Left single quote
    text = text.replace('\u2019',"'")  # Right single quote
    return text

def monitor_clipboard():
    print("Quote formatter is running. Press Ctrl+C to stop.")
    last_content = pyperclip.paste()
    
    try:
        while True:
            current_content = pyperclip.paste()
            if current_content != last_content:
                formatted_content = format_quotes(current_content)
                pyperclip.copy(formatted_content)
                print("Quotes formatted!")
                last_content = formatted_content
            time.sleep(0.5)  # Check every half second
    except KeyboardInterrupt:
        print("\nQuote formatter stopped.")

if __name__ == "__main__":
    monitor_clipboard()