import pyautogui
import pyperclip
import time
import google.generativeai as genai
import os
from dotenv import load_dotenv
# Load the environment variables from .env file
load_dotenv()

# Paste your Google AI Studio API key here
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure the library with your key
genai.configure(api_key=API_KEY)  # type: ignore

# Use the fast and efficient Flash model
model = genai.GenerativeModel('gemini-2.5-flash')  # type: ignore

def get_gemini_reply(chat_text):
        """
        Sends the chat history to Gemini and gets a response.
        """
        prompt = f"""
        You are a person named (Your Name) who speaks English, Hindi and Kannada well as English and most of the time You reply in English, but if they chat in kannada You reply in kannada same goes for hindi. You are from India and you are a coder. You analyse chat history and respond like Madhusudhan.
        Output should be the next chat response as (Your Name).
        Here is the recent chat history:
        {chat_text}
        
        Based on the last message, generate a natural, short, and conversational reply.
        IMPORTANT RULES:
        1. Output ONLY the exact text of the reply.
        2. Do NOT include your name at the beginning.
        3. Do NOT include quotation marks around the reply.
        4. Keep it brief.
        """
        
        try:
            api_response = model.generate_content(prompt)
            return api_response.text.strip()
        except Exception as e:
            print(f"Gemini API Error: {e}")
            return "Sorry, I am facing a network issue right now."

def is_last_message_from_sender(chat_log, sender_name="Sender Name"):
    """Checks if the most recent message was sent by the target person."""
    messages = chat_log.strip().split('\n')
    if not messages:
        return False
    
    # Read the lines from the bottom up to find the last actual message
    for line in reversed(messages):
        # Find the last line that starts with a bracket (the timestamp)
        if line.strip().startswith('['):
            # Check the sender's name is in THIS SPECIFIC line
            if sender_name in line:
                return True
            else:
                return False
    return False

# --- AUTOMATION STARTS HERE ---

# time to switch to WhatsApp
time.sleep(1)

# 1. Click WhatsApp icon/chat area
pyautogui.click(948, 745)
time.sleep(1)

while True:

    # 2. Move to your specific Start Point
    pyautogui.moveTo(525, 155)

    # 3. Smoothly drag to the End Point
    pyautogui.dragTo(1322, 644, duration=1.0, button='left')
    time.sleep(0.5) 

    # 4. Copy the text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)

    # 5. Click the start point again to un-highlight the text
    pyautogui.click(525, 155)

    # 6. Store the chat in a variable
    chat_history = pyperclip.paste()
    print(chat_history)

    if is_last_message_from_sender(chat_history):
        print("\n✅ Message from sender detected!")
        print("Copied Chat:\n", chat_history)
        
        # 7. Send the copied chat to Gemini
        response = get_gemini_reply(chat_history)

        print("\nYour AI's Reply:\n", response)

        # --- 8. SEND THE MESSAGE ON WHATSAPP ---
        pyperclip.copy(response)

        # Click the WhatsApp "Type a message" text box
        pyautogui.click(615, 680) 
        time.sleep(0.5)

        # Paste the message
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        # Hit Enter to send!
        pyautogui.press('enter')

        print("✅ Message successfully sent!")
        
        # Wait a few seconds so it doesn't instantly read its own message
        time.sleep(5)
        
    else:
        # If the sender didn't send the last message, just wait and check again
        time.sleep(2)