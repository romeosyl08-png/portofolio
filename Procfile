release: python manage.py migrate
web: gunicorn --chdir portfolio portfolio_project.wsgi:application --log-file -