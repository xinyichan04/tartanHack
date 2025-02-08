import os
import random
import subprocess
import tomllib

import toml

# def generate_background_noise(noise_type="rain", duration=60):
#     noises = {
#         "rain": "https://example.com/audio/rain.mp3",
#         "waves": "https://example.com/audio/waves.mp3",
#         "fireplace": "https://example.com/audio/fireplace.mp3"
#     }
#     return noises.get(noise_type, "https://example.com/audio/default.mp3")


def read_toml(file_path):
  with open(file_path, 'rb') as f:
    config = tomllib.load(f)
  return config


def write_toml(file_path, data):
  with open(file_path, 'w') as f:
    toml.dump(data, f)


def generate_audio_from_text(
  toml_file=os.path.join(os.getcwd(), "demo.toml"),
  gen_text=None,
  ref_audio=None,
  ref_text=None,
  output_dir="tests",
  output_file="output.wav"
):

  # Ensure the output directory exists
  os.makedirs(output_dir, exist_ok=True)

  config = read_toml(toml_file)

  if gen_text:
    config["gen_text"] = gen_text
  if ref_audio:
    config["ref_audio"] = ref_audio
  if ref_text:
    config["ref_text"] = ref_text

  # Define the command to run the CLI with appropriate parameters
  command = [
    "f5-tts_infer-cli", "-c", toml_file
  ]

  write_toml(toml_file, config)

  # Execute the command
  try:
    subprocess.run(command, check=True)
    print(f"Audio saved to {os.path.join(output_dir, output_file)}")
  except subprocess.CalledProcessError as e:
    print(f"Error during inference: {e}")
