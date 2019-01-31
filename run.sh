source ./env.sh
docker-compose up -d
. venv/bin/activate
python manage.py run
