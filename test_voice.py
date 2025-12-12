import speech_recognition as sr
import subprocess
import time

# Load apps from apps.txt
def load_apps():
    apps = {}
    with open("apps.txt", "r") as f:
        for line in f:
            app = line.strip()
            if app:
                apps[app.lower()] = app
    return apps

apps = load_apps()

def open_app(app_name):
    try:
        print(f"Opening {app_name}...")
        subprocess.Popen([app_name])
    except FileNotFoundError:
        print(f"❌ ERROR: '{app_name}' command not found.")

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as mic:
        print("\n🎤 Say a command (example: 'open firefox'):")
        audio = r.listen(mic)

    try:
        text = r.recognize_google(audio).lower()
        print("🗣 You said:", text)
        return text
    except:
        print("❌ Could not understand, try again…")
        return ""

def main():
    print("\n🚀 Voice Control Activated")
    print("Say: open brave / open firefox / open terminal / stop\n")

    while True:
        command = listen_command()

        # exit command
        if command in ["stop", "exit", "quit"]:
            print("👋 Exiting voice control.")
            break

        # match app names
        for app in apps:
            if app in command:
                open_app(apps[app])
                break
        else:
            print("⚠ App not found in apps.txt")

        time.sleep(1)

if __name__ == "__main__":
    main()
