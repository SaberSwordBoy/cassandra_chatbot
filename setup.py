import cx_Freeze

executables = [cx_Freeze.Executable("chatbot.py")]

cx_Freeze.setup(
    name="Project: Cassandra (Virtual Chatbot)",
    options={"build_exe": {"packages": ["pygame", "pyaudio", "speech_recognition", "pyttsx3"],
                           "include_files": ["texttospeech.py", "weather.py", "intents.json"]}},
    executables=executables

)
