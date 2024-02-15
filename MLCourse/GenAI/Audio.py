import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

audio_file = open("hi.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print("Transcribing hi.mp3:\n")
print(transcript)

print("\nTranslating french.mp3:\n")

audio_file = open("french.mp3", "rb")
transcript = openai.Audio.translate("whisper-1", audio_file)

#Will it actually work?
print(transcript)