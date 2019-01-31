# Sanic-starter [![CircleCI](https://circleci.com/gh/sisobus/sanic-starter.svg?style=svg)](https://circleci.com/gh/sisobus/sanic-starter)

Sanic is a Python web server and web framework that's written to go fast. It allows the usage of the async/await syntax added in Python 3.5, which makes your code non-blocking and speedy.

This repository contains Sanic-SQLAlchemy-Authentication

Backend stack
```
- Sanic: flask-like fast async web framework
- Sanic-jwt: authentication
- alembic: sqlalchemy migration tool
- aredis: async redis client
- bcrypt: password hash lib

- nginx: reverse proxy server
- redis: user session db
```

```
- ./data: postgresql data
- ./redis_data: redis data
```
