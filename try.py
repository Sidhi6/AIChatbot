from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as genai
from gtts import gTTS
import os
from uuid import uuid4

app = Flask(__name__)

api_key = "AIzaSyCLR7NiaIg4hyX412VY9vbpgzC1XDG5X_s"
genai.configure(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-response', methods=['POST'])

def generate_response():
    try:
        data = request.json
        user_speech = data['speech']
        prompt = (
            "Respond to the current user's response "
            " Do not use asterisks. Give a short and simple response.\n"
            f"Current User's Response: {user_speech}\n"
           
        )
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        ai_text_response = response.text

        tts = gTTS(ai_text_response)
        file_name = f"response_{uuid4()}.mp3"
        file_path = os.path.join("static", file_name)
        tts.save(file_path)

        
        return jsonify({
            "response": ai_text_response,
            "audio_url": f"/static/{file_name}"
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/static/<filename>')
def serve_file(filename):
    return send_file(os.path.join("static", filename))

if __name__ == '__main__':
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)
