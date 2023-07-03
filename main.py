from fastapi import FastAPI,UploadFile,Form
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from typing import Annotated

app = FastAPI()

#서버에 올릴때 클래스화 시켜 올려야 한다. 
class Chatting(BaseModel):
    id: str
    content: str

#올려진 내용은 배열로 올라간다.    
chats =[]

@app.post("/chats")
def create_chat(chat:Chatting):
    chats.append(chat)
    return '메세지 저장에 성공했습니다'

@app.get("/chats")
def read_chat():
    return chats
    


@app.post('/items')
def create_item(image:UploadFile,
                title:Annotated[str,Form()],
                price:Annotated[int,Form()],
                description:Annotated[str,Form()],
                place:Annotated[str,Form()]):
    
    print(image,title,price,description,place)
    return '200'


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
