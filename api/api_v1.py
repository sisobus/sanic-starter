from sanic import Blueprint
from sanic.response import json
from sanic_jwt.decorators import protected

api_v1 = Blueprint('v1', url_prefix='/api', version='v1')


@api_v1.route('/', methods=['GET', 'POST'])
async def api_v1_root(request):
    return json({'message': 'api v1 root'})


@api_v1.route('/protected', methods=['GET', 'POST'])
@protected()
async def protected(request):
    payload = request.app.auth.extract_payload(request)
    print(payload)
    return json({'message': 'protected'})
