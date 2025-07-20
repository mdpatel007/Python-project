# 🧠 Python Mega Project Collection – Beginner to Smart AI Assistant

This repository contains 5 beginner-to-intermediate level Python projects to showcase foundational coding, logic building, and smart AI integration skills.

---

## 🔥 Projects Included

### 1. 🎙️ Jarvis – Python Voice Assistant (AI-Powered)
A smart voice assistant built with Python, Gemini AI API, and speech recognition.

**Features:**
- Takes voice commands
- Gives AI-powered answers using Gemini
- Talks like an assistant (text-to-speech)
- Understands questions like: “What is AI?”, “Open YouTube”, etc.

**Tech Stack:**  
`Python`, `speech_recognition`, `pyttsx3`, `google.generativeai`, `pyaudio`

#### 🔄 How It Works
1. **Listens to your voice** via microphone (`speech_recognition`)
2. **Converts speech to text**
3. **If it's a question** → sends it to Gemini API for a smart response  
   **If it's an action** → opens website, tells time, etc.
4. **Reads the answer out loud** using `pyttsx3`

---

### 2. 🤖 Auto-Reply AI Chatbot (Funny Roast Bot)
A fun project that reads WhatsApp-like chat history from screen, analyzes the last message, and replies with a Hindi/English-style roast using Gemini AI.

**Features:**
- Detects new messages from a specific person
- Copies chat history automatically using `pyautogui`
- Sends the last message to Gemini API
- Generates a Hinglish roast (funny but non-toxic)
- Types and sends the reply automatically

**Tech Stack:**  
`Python`, `pyautogui`, `pyperclip`, `google.generativeai`, `time`

#### 🔄 How It Works
- Selects chat text area using mouse automation
- Copies entire conversation using clipboard
- Checks if the last message is from the target friend
- Sends that message to Gemini API with a roasting prompt
- Types the AI-generated roast like a real human and hits Enter

---


### 3. 🎮 Snake, Water, Gun Game – Python CLI Fun
A terminal-based version of the classic game with simple logic and score tracking.

**Features:**
- Play against the computer
- Score system and replay option
- Beginner-friendly game logic

---

### 4. 🔐 Random Password Generator
Generates strong and customizable passwords based on user preference.

**Features:**
- Choose password length
- Mix of letters, numbers, and symbols
- Simple UI using CLI

---

### 5. 🎯 Number Guessing Game
The computer picks a number and the player tries to guess it in minimum tries.

**Features:**
- Random number generation
- Hint system (Too High / Too Low)
- Counts total guesses

---

## 🚀 How to Run

### Step 1: Clone the repository  
git clone https://github.com/mdpatel007/Python-project.git
cd Python-project

### Step 2: (Optional) Create and activate virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows

### Step 3: Install required packages for Jarvis
pip install -r requirements.txt

### Step 4: Run any project
cd "Python mega project-1 Jarvis"
python client.py
