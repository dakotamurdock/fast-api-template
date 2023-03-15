from fastapi import FastAPI
from authentication import router as authentication_router
from accounts import router as accounts_router
from fastapi.middleware.cors import CORSMiddleware

SERVER = 'http://127.0.0.1:8000'

app = FastAPI(docs_url="/docs",
              title="Template",
              version="0.0.1")

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Docs URL": f"{SERVER}/docs"}


app.include_router(authentication_router.router)
app.include_router(accounts_router.router)
