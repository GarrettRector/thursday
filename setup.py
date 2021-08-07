inp = input("OpenAI Key > ")
with open("FlaskServer/key.properties", "w") as file:
    file.write(f"[key]=\nkey = {inp}")
print("Setup complete. Would you like to run the chatbot? (Y/N)")
inp = input()
while True:
    match inp.lower():
        case "y":
            # to be completed
            print("Running of chatbot still in developement")
            break
        case "n":
            exit()
        case _:
            print("Invalid answer")
