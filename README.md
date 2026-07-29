# Sophia AI Voice Assistant with Automation

An intelligent desktop-based AI Voice Assistant built with **Python**, **Eel**, **HTML**, **CSS**, and **JavaScript** that enables users to interact with their computer through natural voice commands. Sophia automates everyday desktop tasks such as opening applications, launching websites, playing YouTube content, and providing spoken responses through an intuitive graphical interface.

Developed as a **Final Year Project** for the Bachelor of Science in Computer Science program at the University of Agriculture, Faisalabad. The project combines voice recognition, desktop automation, database-driven command execution, and an interactive frontend to deliver a seamless user experience. :contentReference[oaicite:0]{index=0}

---

## Features

- Voice-controlled desktop automation
- Open desktop applications using voice commands
- Launch websites instantly through voice input
- Play YouTube videos and music using voice
- Offline Text-to-Speech responses
- SQLite database for storing custom commands
- Interactive and responsive user interface
- Real-time communication between frontend and backend using Eel
- Audio feedback with startup and microphone activation sounds
- Modular project architecture for easy scalability

---

## Technologies Used

### Backend
- Python
- Eel
- SpeechRecognition
- Pyttsx3
- SQLite
- PyWhatKit
- Webbrowser
- OS Module

### Frontend
- HTML5
- CSS3
- JavaScript
- jQuery
- Bootstrap

### Database
- SQLite

---

## Project Structure

```text
Sophia-AI-Voice-Assistant/
│
├── engine/
│   ├── command.py
│   ├── config.py
│   ├── db.py
│   ├── features.py
│   └── ...
│
├── www/
│   ├── assets/
│   │   ├── audio/
│   │   ├── img/
│   │   └── vendore/
│   ├── controller.js
│   ├── index.html
│   ├── main.js
│   └── style.css
│
├── main.py
├── news_sites.py
├── sophia.db
├── requirements.txt
└── README.md
```

---

## How It Works

1. The user speaks a voice command through the microphone.
2. Speech Recognition converts the spoken command into text.
3. The Python backend analyses the command.
4. Sophia searches the SQLite database for matching commands.
5. The requested application, website, or media is executed.
6. The assistant provides both spoken and visual feedback.
7. The system automatically returns to listening mode, ready for the next command. :contentReference[oaicite:1]{index=1}

---

## Installation

### Clone the repository

```bash
git clone https://github.com/alishasaeeddev-bot/Sophia-AI-Voice-Assistant.git
```

### Navigate to the project folder

```bash
cd Sophia-AI-Voice-Assistant
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python main.py
```

---

## Key Functionalities

- Voice Recognition
- Desktop Application Automation
- Website Automation
- YouTube Search & Playback
- Database-Driven Command Management
- Offline Text-to-Speech
- Interactive Animated Interface
- Real-Time User Feedback

---

## System Architecture

Sophia follows a modular architecture consisting of:

- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Communication Layer:** Eel
- **Backend:** Python
- **Database:** SQLite
- **Speech Processing:** SpeechRecognition
- **Voice Output:** Pyttsx3
- **Media Automation:** PyWhatKit

This architecture ensures efficient communication between the user interface and backend logic while maintaining scalability and ease of maintenance. :contentReference[oaicite:2]{index=2}

---

## Future Enhancements

- AI-powered conversational responses
- Weather information
- Calendar integration
- Email automation
- Notes and reminders
- Multi-language support
- User authentication
- Wake-word detection
- Cloud synchronization

---

## Author

**Alisha Saeed**

Bachelor of Science in Computer Science  
University of Agriculture, Faisalabad

- GitHub: https://github.com/alishasaeeddev-bot
- LinkedIn: https://www.linkedin.com/in/alishasaeed

---

## License

This project was developed for educational and research purposes as part of a Final Year Project.

---

## Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
