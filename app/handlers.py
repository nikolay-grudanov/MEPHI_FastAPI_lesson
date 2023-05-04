from fastapi import APIRouter, Body

from forms import UserNameParts

from query import getIp, getTime

router = APIRouter()


@router.get('/')
async def index():
    return {'status': 'Ok'}


@router.get("/users/{username}", name='Hello user')
async def read_user(username: str):
    return {"message": f'Hello {username}'}


@router.post('/users/full-name', name='Full name')
async def login(user_from: UserNameParts = Body(..., embed=True)):
    return {"fullName": f'{user_from.lastName.strip()} {user_from.firstName.strip()} {user_from.middleName.strip()}'}


@router.get('/users/current/ip', name='Получить текущуй ip')
async def current_ip():
    ip = getIp()

    return ip


# @router.get('/users/current/full-time', name='Получить текущие время')
# async def current_fill_time():
#     ip = getIp()

#     full_time = getTime(ip)

#     return full_time
