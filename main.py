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


from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello TutLinks.com123"}