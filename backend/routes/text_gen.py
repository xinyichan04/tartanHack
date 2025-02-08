from flask import Blueprint, jsonify, request, session, url_for
from services import deepseek_service, audio_service
import json

text_gen_bp = Blueprint("text_gen", __name__)


@text_gen_bp.route("/submit-preferences", methods = ["POST"])
def submit_pref():
    #wonder if theres faster way to loop through
    meditation_type = request.form.get('meditation-type')
    tone = request.form.get('tone')
    sound = request.form.get('sound')
    med_description = request.form.get('meditation-description')
    print(f"SUBMIT PREF\n{meditation_type, sound, tone, med_description}")
    
    # print(meditation_type)
    session['preferences'] = {
        'meditation_type': meditation_type,
        'tone': tone,
        'sound': sound,
        'description': med_description
    }
    return "submit-pref"

@text_gen_bp.route("/generate", methods =['GET'])
def generate_text():
    preferences = session.get('preferences')
    if not preferences:
        return jsonify({"error": "Preferences not set. Submit preferences first."}), 400
    
    meditation_type = preferences['meditation_type']
    tone = preferences['tone']
    sound = preferences['sound']
    description = preferences['description']
    print(meditation_type,tone,sound,description)

    text = deepseek_service.generate_meditation_text(meditation_type, sound, tone, description)
    
    parsed_data = json.loads(text) 
    message = parsed_data["message"]

    print(message)

    text = message
    output_dir = "static/audio"
    output_file = "generated_audio.wav"

    # Generate the audio
    audio_path = audio_service.generate_audio_from_text(text, output_dir, output_file)

    if audio_path is None:
        return jsonify({"error": "Failed to generate audio."}), 500

    # Get the URL of the file
    audio_url = url_for("static", filename=f"audio/{output_file}", _external=True)
    print(audio_url)

    # return message
    return jsonify({"message": message})



# we want to return this message somewere. 

# @text_gen_bp.route("/generate", methods=["POST"])
# def generate_text():
#     return jsonify({"text": "This is a placeholder meditation text."})
