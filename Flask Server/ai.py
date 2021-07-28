import configparser
import openai

config = configparser.ConfigParser()
config.read('key.properties')

openai.api_key = config.get("key", "key")
completion = openai.Completion()

start_sequence = "\nThursday:"
restart_sequence = "\n\nPerson:"


def ask(question, chat_log):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    print(prompt_text)
    response = openai.Completion.create(
        engine="curie",
        prompt=prompt_text,
        temperature=0.8,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.3,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_chat_log(question, answer, chat_log):
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
