import os
from sanic import Sanic
from api.config import BaseConfig
from sanic_jwt import Initialize
from api.auth import (
    authenticate, store_refresh_token,
    retrieve_refresh_token, Register,
    retrieve_user
)
from api.api_v1 import api_v1


def create_app():
    app = Sanic(__name__)
    app.config.from_object(BaseConfig)
    app.blueprint(api_v1)

    _views = (
        ('/register', Register),
    )

    Initialize(
        app,
        authenticate=authenticate,
        class_views=_views,
        refresh_token_enabled=True,
        store_refresh_token=store_refresh_token,
        retrieve_refresh_token=retrieve_refresh_token,
        retrieve_user=retrieve_user,
        expiration_delta=BaseConfig.JWT_ACCESS_TOKEN_EXPIRES
    )
    if BaseConfig.ENV == 'development':
        app.run(debug=BaseConfig.DEBUG)
    else:
        app.go_fast(debug=BaseConfig.DEBUG, workers=os.cpu_count())


if __name__ == '__main__':
    create_app()
