import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()


def speak(text):
    """Make the assistant speak the given text."""
    tts_engine.say(text)
    tts_engine.runAndWait()


def recognize_speech():
    """Listen and recognize speech input from the user."""
    try:
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
        speak("Sorry, I'm having trouble accessing the speech service check your internet connection.")
    except Exception as e:
        speak("An error occurred while trying to use the microphone.")
        print(f"Error: {e}")  # Log the actual error
    return ""


def teach(topic):
    """Provide a simple tutorial based on the topic."""
    tutorials = {
        "python": "Python is a versatile programming language known for its simplicity. It is great for beginners and used in web development, data analysis, and machine learning. To print a message in Python, you can use the print function like this: print('Hello World').",
        "html": "HTML stands for HyperText Markup Language. It is the backbone of all websites. It defines the structure of a webpage. For example, you can create a simple webpage using HTML like this: 'HTML tag, body tag, h1 for a heading, and p for a paragraph'.",
        "javascript": "JavaScript is a programming language used to make websites interactive. It can manipulate HTML elements, validate forms, and create animations. An example is using JavaScript to change a heading's text: document.getElementById('myHeading').innerHTML = 'New Text'.",
        "css": "CSS stands for Cascading Style Sheets. It is used to style HTML elements. For example, you can change the background color of a webpage using CSS like this: 'body { background-color: lightblue; }'.",
        "node": "Node.js is a runtime that allows you to run JavaScript on the server side. It's useful for building fast and scalable server-side applications. A simple example of a server in Node.js is: const http = require('http'); http.createServer((req, res) => { res.write('Hello World!'); res.end(); }).listen(3000);",
    }

    response = tutorials.get(topic, f"Sorry, I don't have a tutorial on {topic} yet.")
    speak(response)
    print(response)


def assistant():
    """Main function to start the assistant and listen for commands."""
    speak("Hello, how can I assist you today?")
    while True:
        command = recognize_speech()
        if command:
            print(f"You said: {command}")

            # Responding to commands
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
            elif "teach me" in command:
                # Extract the topic the user wants to learn about
                topic = command.replace("teach me", "").strip()
                if topic:
                    speak(f"Alright, let's learn about {topic}.")
                    teach(topic)
                else:
                    speak("Please tell me what you want to learn about.")
            else:
                speak("Sorry, I can't do that yet.")


if __name__ == "__main__":
    assistant()
