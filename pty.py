import pyttsx3
import time
from playsound import playsound


# Function to recite a verse using TTS (or play a pre-recorded file for better quality)
def recite_verse(file_path=None, text=None):
    if file_path:
        # Play pre-recorded audio file
        playsound(file_path)
    elif text:
        # Use text-to-speech for recitation if no audio file is provided
        engine = pyttsx3.init()
        engine.setProperty(
            "rate", 130
        )  # Adjust speed to match a typical recitation speed
        engine.setProperty(
            "voice", "com.apple.speech.synthesis.voice.maged"
        )  # Example for a more natural Arabic voice
        engine.say(text)
        engine.runAndWait()


# Function to simulate prayer recitation
def lead_prayer():
    print("Starting with Surah Al-Fatiha...")
    recite_verse(
        file_path="alfatiha.mp3"
    )  # Use a pre-recorded audio file for Surah Al-Fatiha
    time.sleep(2)  # Pause between surahs
    
    print("Allahu Akbar")  # Say Allahu Akbar
    recite_verse(text="Allahu Akbar")
    time.sleep(3)  # Wait for 3 seconds for people to bow

    print("Now reciting Surah Al-Ikhlas...")
    recite_verse(
        file_path="alikhlas.mp3"
    )  # Use a pre-recorded audio file for Surah Al-Ikhlas
    time.sleep(2)  # Pause for effect

    print("Allahu Akbar")  # Say Allahu Akbar
    recite_verse(text="Allahu Akbar")
    time.sleep(3)  # Wait for 3 seconds for people to bow

    print("Going into Ruku'...")
    time.sleep(2)
    recite_verse(text="Subhana Rabbiyal Azim")  # Example Ruku' recitation

    print("Standing up: Sami'Allahu liman Hamidah...")
    recite_verse(text="Sami'Allahu liman Hamidah")  # Example standing up recitation

    # Continue the simulation with more steps of the prayer as desired
    # ...


# Run the prayer simulation
lead_prayer()
