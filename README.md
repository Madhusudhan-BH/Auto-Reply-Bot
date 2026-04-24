# WhatsApp Auto Reply Bot 💬

## Features
- Automates WhatsApp Web replies
- Reads chat history for context
- AI responses using Gemini
- Targeted replies for specific contacts

## Tech Stack
- Python
- pyautogui & pyperclip
- Google Gemini API (google-genai)
- python-dotenv

## Project Files
- `Bot.py`: The main automation script that handles AI replies and messaging.
- `Get_cursor.py`: A built-in utility script to easily find the exact X, Y screen coordinates needed for `pyautogui` to click correctly on different monitor sizes.

## Setup

1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt

3. Create a `.env` file:
   GEMINI_API_KEY=your_key

## Usage

1. Open WhatsApp Web and log in.
2. Run `python Get_cursor.py` to find the exact screen coordinates of your text box, send button, and chat area. 
3. Update the coordinates inside `Bot.py` to match your screen.
4. Run the main script:
   python Bot.py

## Author
Madhusudhan BH