import pygame


def play_audio(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(f"audio/audio_clips/{filename}")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        break