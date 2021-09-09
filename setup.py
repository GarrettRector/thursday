import app
import client

inp = input("OpenAI Key > ")
with open("FlaskServer/key.properties", "w") as file:
    file.write(f"[key]=\nkey = {inp}")
print("Setup complete. Would you like to run the chatbot? (Y/N)")
inp = input()
while True:
    match inp.lower():
        case "y":
            app.app.run()
            client.main()
        case "n":
            exit()
        case _:
            print("Invalid answer")
