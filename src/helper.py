import speech_recognition as sr
from gtts import gTTS
from dotenv import load_dotenv
import google.generativeai as genai
import os



load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY

def voice_to_text():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        audio= recognizer.listen(source)
    try:
        text=recognizer.recognize_google(audio)
        
        print("you said .. ",text)
    except Exception as e:
        text= "I am unable to here you properly"
        print("There is issue : ",e)
    return text

def Load_llm_Model(text):
    genai.configure(api_key=GOOGLE_API_KEY)
    model= genai.GenerativeModel()
    response=model.generate_content(text)
    print(response.text)
    return response.text


def TextToAudio(text):
    textTospach=gTTS(text=text,lang='en')
    textTospach.save("speech.mp3")
