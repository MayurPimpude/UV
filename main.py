from fastapi import FastAPI
import uvicorn

def main():
    print("Hello from code!")
    uvicorn.run(app,port=8000)

app = FastAPI()

@app.get("/")
async def root():
    return {"message":'Hello chai code'}

if __name__ == "__main__":
    main()
