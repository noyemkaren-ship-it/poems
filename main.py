from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from shemas.ret import Errors
from api.routers import router

app = FastAPI(title="Miha Kvas")
app.include_router(router)
templates = Jinja2Templates(directory="templates")


@app.get("/poems-page", tags=["page"])
async def poems_page(request: Request):
    return templates.TemplateResponse("all_poems.html", {"request": request})



@app.get("/", tags=["page"])
async def root():
    return Errors(
        error="Is page empty",
        text="Please leave theese page and try again"
    )


@app.get("/register", tags=["page"])
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@app.get("/login", tags=["page"])
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get("/profile/{username}", tags=["page"])
async def profile_page(request: Request, username: str):
    current_user = request.cookies.get("username")
    if not current_user:
        return RedirectResponse(url="/login", status_code=303)
    if current_user != username:
        return templates.TemplateResponse(
            "error.html",
            {"request": request, "error": "Это не ваш профиль!"},
            status_code=403
        )

    return templates.TemplateResponse(
        "profile.html",
        {"request": request, "username": username}
    )


@app.get("/poems", tags=["page"])
async def poems_page(request: Request):
    return templates.TemplateResponse("poems.html", {"request": request})


@app.get("/add_poem", tags=["page"])
async def add_poem_page(request: Request):
    current_user = request.cookies.get("username")
    if not current_user:
        return RedirectResponse(url="/login", status_code=303)

    return templates.TemplateResponse(
        "add_poem.html",
        {"request": request}
    )

@app.get("/poems/{username}", tags=["page"])
async def user_poems_page(request: Request, username: str):
    return templates.TemplateResponse(
        "user_poems.html",
        {"request": request, "username": username}
    )

@app.get("/logout", tags=["page"])
async def logout():
    response = RedirectResponse(url="/login", status_code=303)
    response.delete_cookie("username")
    return response
