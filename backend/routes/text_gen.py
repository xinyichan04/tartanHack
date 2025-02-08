from flask import Blueprint, jsonify

text_gen_bp = Blueprint("text_gen", __name__)

@text_gen_bp.route("/generate", methods=["POST"])
def generate_text():
    return jsonify({"text": "This is a placeholder meditation text."})
