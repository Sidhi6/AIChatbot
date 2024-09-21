Speech-to-Speech Chatbot
This project is a speech-to-speech chatbot that allows users to ask questions via voice input, process the input using speech recognition, generate a response using a large language model (LLM), and return a voice-based response. The system is built using Flask, Google Gemini LLM, and Google Text-to-Speech (gTTS).
Features
Real-time Speech Recognition: Capture user speech via the Web Speech API and convert it to text.
LLM Response Generation: Use Google’s Gemini model to generate context-aware text responses.
Speech Output: Convert AI-generated text responses back into speech using Google Text-to-Speech.
Flask Backend: Manages communication between the front-end, LLM, and TTS engine.
