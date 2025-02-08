import random

def generate_background_noise(noise_type="rain", duration=60):
    noises = {
        "rain": "https://example.com/audio/rain.mp3",
        "waves": "https://example.com/audio/waves.mp3",
        "fireplace": "https://example.com/audio/fireplace.mp3"
    }
    return noises.get(noise_type, "https://example.com/audio/default.mp3")
