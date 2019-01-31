from sanic_jwt import BaseEndpoint, exceptions
from sanic.response import json
from sanic.exceptions import abort
from api.models import User
from api.database import scoped_session, RedisSession as aredis
import bcrypt


async def authenticate(request, *args, **kargs):
    email = request.json.get("email", None)
    password = request.json.get("password", None)

    if email is None or password is None:
        raise exceptions.AuthenticationFailed('Missing email or password.')

    with scoped_session() as session:
        user = session.query(User).filter_by(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found.')
        if not bcrypt.checkpw(
                password.encode('utf-8'), user.password.encode('utf-8')):
            raise exceptions.AuthenticationFailed('Password is incorrect.')
        return user.to_dict()


async def store_refresh_token(user_id, refresh_token, *args, **kargs):
    key = f'refresh_token_{user_id}'
    await aredis.set(key, refresh_token)


async def retrieve_refresh_token(request, user_id, *args, **kargs):
    key = f'refresh_token_{user_id}'
    return await aredis.get(key)


async def retrieve_user(request, payload, *args, **kargs):
    if payload:
        user_id = payload.get('user_id', None)
        with scoped_session() as session:
            user = session.query(User).filter_by(id=user_id).first()
            if user:
                return user.to_dict()
    return None


class Register(BaseEndpoint):
    async def post(self, request, *args, **kwargs):
        username = request.json.get('username', None)
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if username is None or email is None or password is None:
            abort(400)

        with scoped_session() as session:
            user = session.query(User).filter_by(email=email).first()
            if user:
                abort(500, 'The email is exists aleady.')
            hashed = bcrypt.hashpw(
                password.encode('utf-8'),
                bcrypt.gensalt()).decode('utf-8')
            print(hashed)
            new_user = User(username, email, hashed)
            session.add(new_user)
        return json({'message': 'register successfully!'})
