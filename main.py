# import uvicorn
# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def root():
#     a = "a"
#     b = "b" + a
#     return {"hello world": b}


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=5000)


from fastapi import FastAPI, Request
import requests
from starlette.responses import FileResponse
from fastapi.responses import StreamingResponse
from moviepy.editor import *
from pytube import YouTube

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return "test"
    
@app.get("/get_author/{token}")
async def getVidoName(token:str):
    # yt = YouTube(url)
    # return yt.title
    url = 'https://www.youtube.com/watch?v='+token
    yt = YouTube(url)
    return yt.author

@app.get("/getVidoName/{token}")
async def getVidoName(token:str):
    # yt = YouTube(url)
    # return yt.title
    url = 'https://www.youtube.com/watch?v='+token
    yt = YouTube(url)
    return yt.title

@app.get("/get_thumbnail_url/{token}")
async def get_thumbnail_url(token:str, req: Request):
    host = "https://floating-citadel-20088.herokuapp.com"

    """透传 API"""
    url = 'https://www.youtube.com/watch?v='+token
    yt = YouTube(url)
    # yt.streams.first().download()
    tube_url = yt.thumbnail_url

    body = bytes(await req.body()) or None
    # print(body)
    r = requests.request(
        req.method, tube_url,
        headers={
            'Cookie': req.headers.get('cookie') or '',
            'Content-Type': req.headers.get('Content-Type')},
        params=req.query_params, data=body, stream=True,
        allow_redirects=True)
    print(r)
    h = dict(r.headers)
    h.pop('Content-Length', None)
    loc = h.pop('Location', '')
    if loc.startswith(host):
        h['Location'] = loc[len(host):]
    return StreamingResponse(r.raw, headers=h, status_code=r.status_code)



@app.get("/downloadVideo/{token}")
async def downloadVideo(token:str):
    url = 'https://www.youtube.com/watch?v='+token
    yt = YouTube(url)
    # yt.streams.first().download()
    tube_url = yt.streams.first().url

    return tube_url

@app.get("/mp3")
def mp3():
    video = VideoFileClip('./who.3gpp')
    video.audio.write_audiofile('test.mp3')
    return FileResponse('./test.mp3',filename="test.mp3")

@app.get("/music")
def music():
    with open('./who.3gpp', 'r') as f:
        return f.read()

@app.get('/other/{token:str}')
async def other_api(token: str, req: Request):
    host = "https://floating-citadel-20088.herokuapp.com"

    """透传 API"""
    url = 'https://www.youtube.com/watch?v='+token
    yt = YouTube(url)
    # yt.streams.first().download()
    tube_url = yt.streams.first().url

    body = bytes(await req.body()) or None
    # print(body)
    r = requests.request(
        req.method, tube_url,
        headers={
            'Cookie': req.headers.get('cookie') or '',
            'Content-Type': req.headers.get('Content-Type')},
        params=req.query_params, data=body, stream=True,
        allow_redirects=True)
    print(r)
    h = dict(r.headers)
    h.pop('Content-Length', None)
    loc = h.pop('Location', '')
    if loc.startswith(host):
        h['Location'] = loc[len(host):]
    return StreamingResponse(r.raw, headers=h, status_code=r.status_code)