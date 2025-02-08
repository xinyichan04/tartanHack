from flask import Blueprint, jsonify

tts_bp = Blueprint("tts", __name__)

@tts_bp.route("/convert", methods=["POST"])
def convert_text():
    return jsonify({"audio_url": "https://example.com/placeholder_audio.mp3"})
