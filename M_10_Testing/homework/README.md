python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
https://tproger.ru/translations/extending-django-user-model/#var1
python manage.py runserver

https://vc.ru/u/818117-viktor-oblomov/612764-django-predstavleniya-na-osnove-klassov-cbv-protiv-predstavleniy-na-osnove-funkciy-fbv


python manage.py dumpdata shopapp.Product > shopapp/tests/fixtures/products-fixtures.json
python manage.py dumpdata shopapp.Order > shopapp/tests/fixtures/orders-fixtures.json
python manage.py dumpdata auth.Group > shopapp/tests/fixtures/grops-fixtures.json
python manage.py dumpdata auth.User > shopapp/tests/fixtures/users-fixtures.json
python manage.py dumpdata accounts.Profile > shopapp/tests/fixtures/profiles-fixtures.json
python manage.py dumpdata blogs.Post > shopapp/tests/fixtures/posts-fixtures.json
python manage.py dumpdata blogs.PostImage > shopapp/tests/fixtures/posts_images-fixtures.json