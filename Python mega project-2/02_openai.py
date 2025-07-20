import google.generativeai as genai

# --- Configuration ---
# Replace with your actual Gemini API key before running
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Sample Chat Log  ---
chat_log = '''
[10:01 PM, 7/19/2025] Friend: Bro, kal college ma exam che?
[10:02 PM, 7/19/2025] You: Haa bhai, 10 baje sharp.
[10:02 PM, 7/19/2025] Friend: Sari che, tyari nai thayi pan 😅
[10:03 PM, 7/19/2025] You: Same here, bas luck par che sab kuch
[10:04 PM, 7/19/2025] Friend: Okay bro, good night!
[10:04 PM, 7/19/2025] You: Good night! All the best 🔥
'''

# --- Generate Response ---
response = model.generate_content(command)

# --- Output ---
print(response.text)
