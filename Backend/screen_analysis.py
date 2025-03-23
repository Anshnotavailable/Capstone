import google.generativeai as genai
import cv2
import numpy as np
import mss
import time
import speech_recognition as sr
from PIL import Image
from Backend.TTS_B import speak  # Your custom TTS function
from dotenv import dotenv_values

# Configure Google Gemini AI API
env_vars = dotenv_values(".env")
GEMINI_API_KEY = env_vars.get("GeminiAPIKey")

# Configure Google Gemini AI API
genai.configure(api_key=GEMINI_API_KEY)

def capture_screen():
    """Captures a frame from the screen using MSS."""
    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Capture the primary screen
        screenshot = sct.grab(monitor)
        
        # Convert the screenshot to a numpy array (for OpenCV processing)
        img = np.array(screenshot)
        img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)  # Convert BGRA to RGB
        
        return Image.fromarray(img)  # Convert to PIL Image

def analyze_screen(image):
    """Sends the screen frame to Google's Gemini AI for analysis."""
    model = genai.GenerativeModel("gemini-2.0-flash-exp")
    response = model.generate_content(["Describe what is happening in this screen frame:", image])
    return response.text

def listen_for_command():
    """Listens for a voice command to activate screen analysis."""
    recognizer = sr.Recognizer()
    
    # Use the microphone to listen to commands
    with sr.Microphone() as source:
        print("\n🎤 Say 'Jarvis, analyze screen' to trigger AI... (Waiting for command)")
        
        # Adjust for ambient noise to avoid incorrect recognition
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        try:
            # Listen to the command and set a timeout for waiting
            audio = recognizer.listen(source, timeout=5)
            
            print("[🎤] Listening...")
            command = recognizer.recognize_google(audio).lower()  # Convert speech to text
            print(f"[🗣️] Command recognized: {command}")
            
            return command
        except sr.UnknownValueError:
            print("[⚠️] Could not understand the audio")
            return None
        except sr.RequestError:
            print("[⚠️] Voice recognition service unavailable")
            return None
        except Exception as e:
            print(f"[⚠️] Error during recognition: {e}")
            return None

def main():
    """Waits for a command to analyze the screen."""
    while True:
        command = listen_for_command()
        
        if command and "analyse screen" in command:
            print("\n[📸] Capturing screen...")
            image = capture_screen()

            print("[🤖] Analyzing screen with Google AI...")
            try:
                analysis = analyze_screen(image)
                print("[🗣️] AI Analysis:", analysis)

                # Speak the AI-generated analysis
                speak(analysis)  
            except Exception as e:
                print("[⚠️] Error analyzing screen:", str(e))

        time.sleep(1)  # Small delay to avoid excessive processing

if __name__ == "__main__":
    main()
