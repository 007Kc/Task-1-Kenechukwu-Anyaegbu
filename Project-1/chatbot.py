from time import sleep
from datetime import datetime as dt







user_events = ["May 11th - Daniel's birthday party","May 21st - Attend a conference"]

print("""
========= Kc_Personal_Assistant =========
1. Listen to music
2. Check events
3. Add event
4. Delete event
5. Exit
================================
""")


responses = {"Hello":"Hello, how are you doing today\nWhat can I help you with",
             "Hello😀":"Yo🙂, what are we working on today",
             "Hi":"Hi, hope your day is going alright\nHow can I be of assistance today",
             "Listen to music":"Loading music from your spotify playlist....",
             "Check events":"Checking for events.....",
             "Add event":"What event would you like to add: ",
             "Delete an event":"Which event number would you like to delete?",
             "Exit":"Goodbye\nSee you tomorrow for more work",

             }


def typing_effect(text):
    for char in text:
        print(char, end="",flush=True)
        sleep(0.03)
    print()





def get_user_input():
    user_input = input(": ").lower().strip().capitalize()
    return user_input

def Kc_Personal_assistant():
    current_hour = dt.now().hour
    if current_hour < 12:
        greeting = "Good morning"
    elif current_hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    sleep(0.5)
    print(f"{greeting}! Welcome back")

    while True:
        user_input = get_user_input()
        typing_effect(responses.get(user_input,"I don't have the capabilities to respond to this "))
        if user_input == "I want to listen to music":
            user_mood= input("What mood are you in:  ")
            typing_effect("Loading your spotify playlist🎵....")
            sleep(3)
            print(f"Now playing {user_mood} music....")
        if user_input == "Help me check if i have any upcoming events":
            sleep(1)
            typing_effect(f"You have these events coming up🗓️:\n")
            for index,events in enumerate(user_events, start=1):
                print(f"{index}.{events}")
        if user_input == "I want to add an event":
            user_add_event = input("")
            user_events.append(user_add_event)
            typing_effect("Event added✅")
        if user_input == "Delete an event":
            for index,events in enumerate(user_events, start=1):
                print(f"{index}.{events}")
            while True:
                try:
                    delete_index = int(input("Choose event number: "))
                    if 1<= delete_index <= len(user_events):
                        removed = user_events.pop(delete_index-1)
                        print(f"Removed: {removed}")
                        break
                    else:
                        print("Invalid Event number")
                except ValueError:
                    print("Enter a valid number: ")
        if user_input in ["Bye","That's all for today"]:
            quit()





Kc_Personal_assistant()