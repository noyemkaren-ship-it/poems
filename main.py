from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates
from shemas.ret import Errors
from api.routers import router

app = FastAPI(title="Miha Kvas")
app.include_router(router)
templates = Jinja2Templates(directory="templates")


@app.get("/poems-page")
async def poems_page(request: Request):
    return templates.TemplateResponse("all_poems.html", {"request": request})

@app.get("/")
async def root():
    return Errors(
        error="Is page empty",
        text="Please leave theese page"
    )

@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/profile/{username}")
async def profile_page(request: Request, username: str):
    return templates.TemplateResponse(
        "profile.html",
        {"request": request, "username": username}
    )

@app.get("/poems")
async def poems_page(request: Request):
    return templates.TemplateResponse("poems.html", {"request": request})

@app.get("/add_poem")
async def add_poem_page(request: Request):
    return templates.TemplateResponse("add_poem.html", {"request": request})

@app.get("/poems/{username}")
async def user_poems_page(request: Request, username: str):
    return templates.TemplateResponse(
        "user_poems.html",
        {"request": request, "username": username}
    )