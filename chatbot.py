import random
import time
import json
import weather
import texttospeech
import pyaudio

# Details about the bot
name = "Cassandra"
age = 17
gender = "female"
hobbies = ["ominous prophecy telling", " seeing the future"]

# user details
user_hobbies = []
my_name = "bryce"
using_voice = False
voice_response = True

# intents file
data_file = open("intents.json", "r").read()
intents = json.loads(data_file)

# characters to ignore, fuck you exclamation point
ignore = ['?', '!', "'", ",", ".", "&", "/", '"', ";", "^", "-"]

# for when it doesn't have a response
no_response = ["Sorry, i don't understand!", "Say that again?", "I don't understand that, sorry", "I don't understand?", "I could not understand that!"]
no_name = ["You haven't told me your name yet!", "You haven't told me your name"]


def get_response(text):
    global hobbies
    global my_name
    response_found = False
    user_input = ""

    for char in text:
        if char not in ignore:
            user_input += char

    for intent in intents["intents"]:
        for pattern in intent['patterns']:
            if pattern in user_input or user_input in intent['patterns']:
                if intent['tag'] == "name":
                    response = random.choice(intent['responses']).replace("NAME", name)
                    return response

                elif intent["tag"] == "user_name":
                    if my_name is None:
                        return random.choice(no_name)
                    return random.choice(intent['responses']).replace("YOURNAME", my_name)

                elif intent['tag'] == "hobbies":
                    return "I like " + ",".join(hobbies)

                elif intent['tag'] == 'weather':
                    return weather.get_weather_for_today()

                elif intent['tag'] == "age":
                    return random.choice(intent['responses']).replace("AGE", str(age))

                else:
                    return random.choice(intent["responses"])  # print random response


print("Welcome to the bot")
print("{}: {}".format(name, "Hello!"))

while True:
    if using_voice:
        query = texttospeech.takeCommand()
    else:
        query = input("{}: ".format(my_name)).lower()
    print("{}: {}".format(my_name.title(), query), end=" ")
    print()

    response = get_response(query)
    if response is None:
        print("{}: {}".format(name, random.choice(no_response)))
        print()
        if voice_response:
             texttospeech.speak(random.choice(no_response))
    else:
        print("{}: {}".format(name, response))
        if voice_response:
            texttospeech.speak(response)
        print()
