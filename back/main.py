from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from g4f.client import Client
from typing import List, Dict

app = FastAPI()
client = Client()
sessions: Dict[str, List[Dict]] = {}


class ChatRequest(BaseModel):
    message: str


@app.post("/chat/")
async def chat(chat_request: ChatRequest):
    user_id = "static_user_id"

    if user_id not in sessions:
        sessions[user_id] = []

    sessions[user_id].append({
        'role': 'user',
        'content': chat_request.message
    })

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=sessions[user_id],
        )

        assistant_message = {
            'role': 'assistant',
            'content': completion.choices[0].message.content
        }
        sessions[user_id].append(assistant_message)

        return {"response": assistant_message['content']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка во время работы ИИ: {e}")


@app.post("/reset/")
async def reset_chat():
    user_id = "static_user_id"
    if user_id in sessions:
        del sessions[user_id]
    return {"message": "Диалог сброшен"}












# origins = [
#     "http://localhost:5173",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
#     allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
#                    "Authorization"],
# )
#
#
# class Role(enum.Enum):
#     USER = 'user'
#     ASSISTANT = 'assistant'
#
#
# class Element(BaseModel):
#     id: int
#     role: Role
#     text: str
#
#
# class Question(Element):
#     role: Role = Role.USER.value
#
#
# class Response(BaseModel):
#     role: Role = Role.ASSISTANT.value
#
#
# msg_list = []
#
#
# @app.post('/gpt')
# async def add_element(element: Annotated[Element, Depends()]):
#     msg_list.append(element)
#     return {'ok': True}
