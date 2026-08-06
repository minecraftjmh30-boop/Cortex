import pygame
import random
from pathlib import Path


def audio(file_type):
    files = get_audios(file_type)
    audio_clip = pick_random_audio(files)
    if audio_clip is None:
        return
    else:
        play_audio(audio_clip)

def get_audios(file_type):
    # Specify the directory path based on the file_type
    folder_path = Path(f'audio/audio_clips/{file_type}')

    # Grab only files
    files = [f for f in folder_path.iterdir() if f.is_file()]

    # Pick a random audio from the files
    return files

def pick_random_audio(files):
    if not files:
        print("No audio files found in the directory.")
        return None
    
    file = random.choice(files)
    return file

def play_audio(file_path):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    pygame.mixer.music.load(str(file_path))
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)