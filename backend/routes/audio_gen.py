from flask import Blueprint, jsonify

audio_gen_bp = Blueprint("audio_gen", __name__)

@audio_gen_bp.route("/generate", methods=["POST"])
def generate_audio():
    return jsonify({"audio_url": "https://example.com/placeholder_background.mp3"})
