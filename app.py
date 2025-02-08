from config import Config
from flask import Flask, render_template, send_file, send_from_directory

from text_gen import text_gen_bp

# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "potato"

# Register Blueprints
app.register_blueprint(text_gen_bp, url_prefix="/api/text")


@app.route('/')
def home():
  return render_template('src/index.html')


@app.route('/<path:path>')
def send_report(path):
  # Using request args for path will expose you to directory traversal attacks
  return send_from_directory('src', path)

@app.route('/output/<path:path>')
def send_audio_output(path):
  # Using request args for path will expose you to directory traversal attacks
  return send_from_directory('output', path)

if __name__ == "__main__":
  app.run(debug=True)
