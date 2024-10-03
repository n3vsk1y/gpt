from g4f.client import Client

client = Client()
messages = [{"role": "user", "content": "Назови лишнее: собака, зебра, стул, кенгуру"}]
chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
)

messages.append({
    "role": "assistant",
    "content": chat_completion.choices[0].message.content
})

messages.append({
    "role": "user",
    "content": "Ты помнишь, что я спросил у тебя в предыдущем вопросе?"
})

chat_completion_1 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

messages.append({
    "role": "assistant",
    "content": chat_completion_1.choices[0].message.content
})

print(messages)











# import g4f
# from g4f import Provider
#
# if __name__ == "__main__" and sys.platform == "win32":
#     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
#
#
# async def chat_with_ai():
#     try:
#         response_gen = g4f.ChatCompletion.create(
#             model=g4f.models.gpt_4o_mini,
#             messages=[{"role": "user", "content": "что ты умеешь?"}]
#         )
#
#         async for response in response_gen:
#             print(response)
#
#     except Exception as e:
#         print(f"Ошибка во время работы ИИ: {e}")
#
#
# asyncio.run(chat_with_ai())















#
# from datetime import datetime
# from time import time
#
#
# def ask(messages_lst: List, model) -> str:
#     response = g4f.ChatCompletion.create(
#         model=model,
#         messages=messages_lst
#     )
#     return response
#
#
# time_dict = dict()
# for model in g4f.models._all_models:
#     try:
#         start = time()
#         answer = ask(
#             messages_lst=[{
#                 'role': 'user',
#                 'content': ''
#             }],
#             model=eval(f'g4f.models.{model.replace('-', '_')}')
#         )
#         time_dict[model] = {
#             'time': time() - start,
#             'answer': answer
#         }
#         print({
#             'time': time() - start,
#             'answer': answer
#         })
#     except Exception as _ex:
#         time_dict[model] = {
#             'time': None,
#             'answer': str(_ex),
#         }
#         print({
#             'time': None,
#             'answer': str(_ex),
#         })
#
# print(time_dict)
# print(sorted(time_dict.items(), key=lambda x: (x[1]['time'] is None, x[1]['time'])))
#
# # msg = []
# # while True:
# #     msg.append({
# #         'role': 'user',
# #         'content': input('user > ')
# #     })
# #     msg.append({
# #         'role': 'assistant',
# #         'content': ask(msg)
# #     })
