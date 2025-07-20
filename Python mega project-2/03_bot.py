import pyautogui
import time
import pyperclip
import google.generativeai as genai

# --- CONFIGURATION ---
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # Replace with your Gemini API key
YOUR_SENDER_NAME = "<YOUR_NAME>"  # Your name in the chat
last_processed_block = ""

# --- FUNCTIONS ---
def get_last_message_block(chat_log):
    lines = [line.strip() for line in chat_log.strip().splitlines() if line.strip()]
    for line in reversed(lines):
        if ": " in line:
            return line
    return None

def is_new_valid_message(chat_log, your_name):
    global last_processed_block
    last_block = get_last_message_block(chat_log)

    if not last_block:
        return None

    sender, message = last_block.split(": ", 1)
    sender, message = sender.strip(), message.strip()

    if sender.lower() != your_name.lower() and last_block != last_processed_block:
        last_processed_block = last_block
        if len(message) < 2 or message.lower() in ["ok", "by", "hmm", ""]:
            return None
        return message
    return None

def generate_gemini_response(last_message):
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('gemini-1.5-flash-latest')

        prompt = f"""
        You are Bob, a funny Hinglish roaster from India. Roast the message below in Hinglish (max 1 line, funny, creative, non-toxic):

        Message: "{last_message}"
        Roast:
        """
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        if "quota" in str(e).lower():
            print("Quota exceeded. Please upgrade Gemini plan.")
        else:
            print(f"Gemini API Error: {e}")
        return None

# --- MAIN LOOP ---

print("Bot starting in 3 seconds...")
time.sleep(3)

try:
    while True:
        try:
            pyautogui.moveTo(700, 200)
            pyautogui.mouseDown()
            pyautogui.moveTo(1817, 923, duration=1.0)
            pyautogui.mouseUp()
            time.sleep(0.8)

            pyautogui.hotkey('ctrl', 'c')
            time.sleep(0.8)
            pyautogui.click(1500, 1000)

            chat_history = pyperclip.paste()
        except Exception as e:
            time.sleep(5)
            continue

        if not chat_history.strip():
            time.sleep(5)
            continue

        last_msg = is_new_valid_message(chat_history, YOUR_SENDER_NAME)
        if last_msg:
            response = generate_gemini_response(last_msg)

            if response:
                time.sleep(2 + len(response) * 0.1)
                pyautogui.click(1250, 970)
                for char in response:
                    pyautogui.write(char)
                    time.sleep(0.05)
                pyautogui.press('enter')
            else:
                time.sleep(60)
        time.sleep(10)

except KeyboardInterrupt:
    print("Bot stopped.")
except Exception as e:
    print(f"Unexpected Error: {e}")
