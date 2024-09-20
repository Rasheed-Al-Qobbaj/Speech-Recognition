import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio, language='ar-EG')
            print(message)
    except speech_recognition.RequestError:
        print("Network error")
    except speech_recognition.UnknownValueError:
        print("Unable to recognize speech")
    except speech_recognition.WaitTimeoutError:
        print("Timeout error")
    except KeyboardInterrupt:
        break

