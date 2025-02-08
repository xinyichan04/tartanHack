import os

from flask import Blueprint, app, jsonify, request, session, url_for

import audio_service

text_gen_bp = Blueprint("text_gen", __name__)


@text_gen_bp.route("/submit-preferences", methods=["POST"])
def submit_pref():
  data = request.get_json()

  session['preferences'] = {
    'environment': data.get("environment"),
    'goal': data.get("goal"),
    'gender': data.get("gender")
  }
  return "Saved to session!"


@text_gen_bp.route("/generate", methods=['GET'])
def generate_text():
  preferences = session.get('preferences')
  if not preferences:
    return jsonify({
      "error": "Preferences not set. Submit preferences first."
    }), 400

  env = preferences['environment']
  goal = preferences['goal']
  gender = preferences['gender']
  print(env, goal, gender)

  message = f"Selected environment: {env}. Selected goal: {goal}. Selected gender: {gender}."

  # Generate the audio
  audio_path = audio_service.generate_audio_from_text(
    toml_file=os.path.join(os.getcwd(), "demo.toml"), gen_text=message
  )
  print(audio_path)
  if audio_path is None:
    return jsonify({
      "error": "Failed to generate audio."
    }), 500

  # return message
  return jsonify({
    "message": message
  })
