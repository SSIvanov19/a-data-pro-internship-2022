python -m spacy download mk_core_news_md
python manage.py migrate
python manage.py collectstatic --no-input
cp -r static ../../home/site/wwwroot/static
