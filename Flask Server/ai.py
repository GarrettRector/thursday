import configparser
import openai

config = configparser.ConfigParser()
config.read('key.properties')
openai.api_key = config.get("key", "key")
completion = openai.Completion()

start_sequence = "\nThursday:"
restart_sequence = "\nPerson:"


def ask(question, chat_log):
    print(question)
    prompt_text = f'{chat_log}{restart_sequence} {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="babbage",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    response = response['choices'][0]['text']
    response = str(response)
    print(response)
    return response


def append_chat_log(question, answer, chat_log):
    with open("chatlog.txt", "w") as file:
        file.write(f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}')
