from fastapi import APIRouter, HTTPException
from starlette.responses import RedirectResponse

from db.repository import UserRepository, PoemsRepository
from shemas.user import UserS
from shemas.poem import PoemS
import random

router = APIRouter()
user_repo = UserRepository()
poem_repo = PoemsRepository()

@router.post("/register", tags=["Register"])
async def register(user_data: UserS):
    existing = user_repo.get_user(user_data.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    user = user_repo.create_user(
        user_data.username,
        user_data.email,
        user_data.password
    )

    return {"message": "User created", "username": user.username}


@router.post("/login", tags=["Login"])
async def login(user_data: UserS):
    user = user_repo.get_user(user_data.username)
    if not user or user.password != user_data.password or user.email != user_data.email:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return {"message": "Login successful", "username": user.username}
@router.get("/users", tags=["users"])
async def get_users():
    users = user_repo.get_all_users()
    return {"users": [{"username": u.username, "email": u.email} for u in users]}


@router.get("/users/{username}", tags=["users/username"])
async def get_user(username: str):
    user = user_repo.get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"username": user.username, "email": user.email}


@router.post("/poems", tags=["poems"])
async def create_poem(poem_data: PoemS):
    author = user_repo.get_user(poem_data.username)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    poem = poem_repo.create_poem(
        poem_data.name,
        poem_data.username,
        poem_data.text
    )
    return {"name": poem.name, "username": poem.username, "text": poem.text}


@router.get("/poems", tags=["poems"])
async def get_poems():
    poems = poem_repo.get_all_poems()
    shuffled = random.sample(poems, len(poems))  # перемешиваем
    return {"poems": [{"name": p.name, "username": p.username, "text": p.text} for p in shuffled]}


@router.get("/poems/random", tags=["poems"])
async def get_random_poem():
    poems = poem_repo.get_all_poems()
    if not poems:
        raise HTTPException(status_code=404, detail="No poems found")
    poem = random.choice(poems)
    return {"name": poem.name, "username": poem.username, "text": poem.text}


@router.get("/poems/{username}", tags=["poems"])
async def get_poems_by_author(username: str):
    author = user_repo.get_user(username)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    poems = poem_repo.get_poem_by_author(username)
    return {"poems": [{"name": p.name, "username": p.username, "text": p.text} for p in poems]}