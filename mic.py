import speech_recognition as sr

# List available microphones
for i, microphone_name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone {i}: {microphone_name}")
