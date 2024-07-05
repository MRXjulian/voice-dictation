import speech_recognition as sr
import keyboard  # Import the keyboard library

r = sr.Recognizer()

print("1. English  2. Spanish")
lan = input('Select language that you want to use: ')

if lan == '1':
    lan_code = 'en-US'  # Language code for English (United States)
elif lan == '2':
    lan_code = 'es-ES'  # Language code for Spanish (Spain)
else:
    print("Invalid selection.")
    exit()

stop_listening = False

def on_key_press(key):
    """
    Callback function for handling key press events.
    Stops the listening loop if the 'q' key is pressed.
    """
    global stop_listening
    if key.name == 'q':  
        stop_listening = True
        print("Stopping listening...")


keyboard.on_press_key('q', on_key_press)

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print('Say something...')

    while not stop_listening:
        try:
            audio = r.listen(source, timeout=None) 
            text = r.recognize_google(audio, language=lan_code)
            print('You said: {}'.format(text))

        except sr.UnknownValueError:
            print("Could not understand what you said")
        except sr.RequestError as e:
            print("Error requesting recognition from Google Speech Recognition service; {0}".format(e))

keyboard.unhook_all()

print("End of the program")


