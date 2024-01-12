from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

#Creates  a dictionary to store the connected users
connected_users = {}

# Initializes fastapi app
app = FastAPI()

# Adds corsmiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=[True],
    allow_methods=["*"],
    allow_headers=["*"]


)

# Home page url
@app.get("/")
def home():
    return {"data": "Home page of chat app"}

# Web socket
@app.websocket("/{user_id}")
async def websocket_endpoint(user_id:str, websocket:WebSocket):
    await websocket.accept() # open the web socket
    #store the web socket to the connected_user dict
    connected_users[user_id] = websocket
    try:
        while True:
            data = await websocket.receive_text() # recieves data
            for user, user_socket in connected_users.items():
                if user != user_id:
                    await user_socket.send_text(data) # avoid to send to same user
    except Exception as e:
        print(str(e))
        del connected_users[user_id]
        await websocket.close()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")
