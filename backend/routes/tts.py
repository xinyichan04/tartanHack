# from flask import Blueprint, jsonify
# from services import audio_service 


# @tts_bp.route("/convert", methods=["POST"])
# def convert_text():
#     # generate text
#     # toml_file_path = os.path.join(os.getcwd(), "demo.toml")
    
#     audio_service.generate_audio_from_text() 

#     # outputs a wav

#     # put in as arg when calling audio_service thing
#     return jsonify({"audio_url": "https://example.com/placeholder_audio.mp3"})


from flask import Blueprint, request, jsonify, send_file, url_for
import os
from services import audio_service

tts_bp = Blueprint("tts", __name__)

# tts_bp = Blueprint("tts", __name__, url_prefix="/tts")

@tts_bp.route("/convert", methods=["POST"])
def convert_text():
    """Converts text to speech and returns the generated audio file."""
    
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' parameter in request."}), 400

    text = data["text"]
    output_dir = "static/audio"
    output_file = "generated_audio.wav"

    # Generate the audio
    audio_path = audio_service.generate_audio_from_text(text, output_dir, output_file)

    if audio_path is None:
        return jsonify({"error": "Failed to generate audio."}), 500

    # Get the URL of the file
    audio_url = url_for("static", filename=f"audio/{output_file}", _external=True)

    return jsonify({"audio_url": audio_url})
