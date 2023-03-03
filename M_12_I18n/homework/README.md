python manage.py makemigrations
python manage.py migrate
python manage.py create_groups
python manage.py create_products
python manage.py create_orders
python manage.py create_posts
python manage.py runserver

python manage.py dumpdata shopapp.Product > shopapp/tests/fixtures/products-fixtures.json
python manage.py dumpdata shopapp.Order > shopapp/tests/fixtures/orders-fixtures.json
python manage.py dumpdata auth.Group > shopapp/tests/fixtures/grops-fixtures.json
python manage.py dumpdata auth.User > shopapp/tests/fixtures/users-fixtures.json
python manage.py dumpdata accounts.Profile > shopapp/tests/fixtures/profiles-fixtures.json
python manage.py dumpdata blogs.Post > shopapp/tests/fixtures/posts-fixtures.json
python manage.py dumpdata blogs.PostImage > shopapp/tests/fixtures/posts_images-fixtures.json


python manage.py test shopapp/tests

sudo apt install gettext

django-admin makemessages --all --ignore=env
django-admin compilemessages --ignore=env
