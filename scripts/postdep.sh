apt-get update
apt-get install tk
python manage.py migrate
python manage.py collectstatic --no-input
cp -r static ../../home/site/wwwroot/static
