import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

def recognize_speech():
    try:
        # Use the microphone as the audio source
        with sr.Microphone() as source:
            
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
            audio = recognizer.listen(source)
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            return text.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
    except sr.RequestError:
        speak("Sorry, I'm having trouble accessing the speech service.")
    return ""

def assistant():
    speak("Hello, how can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            print(f"You said: {command}")

            # Add your own custom commands here
            if "hello" in command:
                speak("Hello! How can I help you?")
            elif "your name" in command:
                speak("I am your virtual assistant.")
            elif "time" in command:
                from datetime import datetime
                now = datetime.now().strftime("%H:%M")
                speak(f"The current time is {now}.")
            elif "exit" in command or "stop" in command:
                speak("Goodbye!")
                break
            else:
                speak("Sorry, I can't do that yet.")

if __name__ == "__main__":
    assistant()
