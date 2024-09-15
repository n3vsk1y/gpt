from typing import List
import g4f


def ask(messages_lst: List) -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gemini_flash,
        messages=messages_lst
    )
    print(f'AI > {response}')
    return response


msg = []
while True:
    msg.append({
        'role': 'user',
        'content': input('user > ')
    })
    msg.append({
        'role': 'assistant',
        'content': ask(msg)
    })

