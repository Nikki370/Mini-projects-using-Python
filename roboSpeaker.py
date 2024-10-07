
import os
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice").Speak

if __name__ == '__main__':
    print("***** Welcome to roboSpeaker 1.1.1 *****")
    while True:
        x = input("what do you want me to speak:")
        if x == "q":
            os.system(speak("bye bye friend"))
            break
        command = speak(f"{x}")
        os.system(str(command))