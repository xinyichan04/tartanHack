from flask import Flask, render_template, send_from_directory
from config import Config
from routes.text_gen import text_gen_bp
from routes.tts import tts_bp
from routes.audio_gen import audio_gen_bp
from routes.user import user_bp


# Initialize Flask App
app = Flask(__name__)
app.config.from_object(Config)

# Register Blueprints
app.register_blueprint(text_gen_bp, url_prefix="/api/text")
app.register_blueprint(tts_bp, url_prefix="/api/tts")
app.register_blueprint(audio_gen_bp, url_prefix="/api/audio")
app.register_blueprint(user_bp, url_prefix="/api/user")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<path:path>')
def send_report(path):
    # Using request args for path will expose you to directory traversal attacks
    return send_from_directory('templates', path)

if __name__ == "__main__":
    app.run(debug=True)
