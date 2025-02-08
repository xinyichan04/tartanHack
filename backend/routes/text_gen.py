from flask import Blueprint, jsonify, request, session, url_for
from services import deepseek_service
import json
import os
import subprocess
import tomllib
import toml

text_gen_bp = Blueprint("text_gen", __name__)

###audio service
    
def read_toml(file_path):
    with open(file_path, 'rb') as f:
        config = tomllib.load(f)
    return config

def write_toml(file_path, data):
    with open(file_path, 'w') as f:
        toml.dump(data, f)
    
def generate_audio_from_text(toml_file,
                             gen_text=None, 
                             ref_audio=None, 
                             ref_text=None, 
                             output_dir="tests", 
                             output_file="output.wav"):
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    config = read_toml(toml_file)
    
    if gen_text:
        config["gen_text"] = gen_text
    if ref_audio:
        config["ref_audio"] = ref_audio
    if ref_text:
        config["ref_text"] = ref_text

    config["output_dir"] = output_dir
    config["output_file"] = output_file
    
    # Define the command to run the CLI with appropriate parameters
    command = [
        "f5-tts_infer-cli", 
        "-c", toml_file
    ]

    write_toml(toml_file, config)

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Audio saved to {os.path.join(output_dir, output_file)}")
    except subprocess.CalledProcessError as e:
        print(f"Error during inference: {e}")

# toml_file_path = os.path.join(os.getcwd(), "demo.toml")

# generate_audio_from_text(toml_file_path, "Sarah watched the whirlpool mesmerized. She couldn't take her eyes off the water swirling around and around. She stuck in small twigs and leaves to watch the whirlpool catch them and then suck them down. It bothered her more than a little bit that this could also be used as a metaphor for her life.", None, None, output_dir="tests", output_file="babygirl.wav")



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

    # text = deepseek_service.generate_meditation_text(meditation_type, sound, tone, description)
    
    # parsed_data = json.loads(text) 
    # message = parsed_data["message"]
    message = "hi"

    print(message)

    text = message
    out_dir = "static/audio"
    out_file = "generated_audio.wav"
    tomlFile = os.path.join(os.getcwd(), "routes/mainDemo.toml")
    # tomlFile = "../mainDemo.toml"

    # Generate the audio
    generate_audio_from_text(tomlFile, gen_text=text, 
                             ref_audio=None, 
                             ref_text=None, 
                             output_dir = out_dir, 
                             output_file = out_file)

    # if audio_path is None:
    #     return jsonify({"error": "Failed to generate audio."}), 500

    # Get the URL of the file

    print("SUcess")

    # audio_url = url_for("static", filename=f"audio/{out_file}", _external=True)
    # print(audio_url)

    # return message
    return jsonify({"message": message})


def read_toml(file_path):
    with open(file_path, 'rb') as f:
        config = tomllib.load(f)
    return config

def write_toml(file_path, data):
    with open(file_path, 'w') as f:
        toml.dump(data, f)
    
def generate_audio_from_text(toml_file,
                             gen_text=None, 
                             ref_audio=None, 
                             ref_text=None, 
                             output_dir="tests", 
                             output_file="output.wav"):
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    config = read_toml(toml_file)
    
    if gen_text:
        config["gen_text"] = gen_text
    if ref_audio:
        config["ref_audio"] = ref_audio
    if ref_text:
        config["ref_text"] = ref_text

    config["output_dir"] = output_dir
    config["output_file"] = output_file
    
    # Define the command to run the CLI with appropriate parameters
    command = [
        "f5-tts_infer-cli", 
        "-c", toml_file
    ]

    write_toml(toml_file, config)

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Audio saved to {os.path.join(output_dir, output_file)}")
    except subprocess.CalledProcessError as e:
        print(f"Error during inference: {e}")

# we want to return this message somewere. 

# @text_gen_bp.route("/generate", methods=["POST"])
# def generate_text():
#     return jsonify({"text": "This is a placeholder meditation text."})
