python manage.py makemigrations
python manage.py migrate
python manage.py create_author_and_book
python manage.py runserver

python manage.py dumpdata bookapi.Author > bookapi/tests/fixtures/authors-fixtures.json
python manage.py dumpdata bookapi.Book > bookapi/tests/fixtures/books-fixtures.json



python manage.py test shopapp/tests

sudo apt install gettext

django-admin makemessages --all --ignore=env
django-admin compilemessages --ignore=env
