#release: cd jstoolchain
#release: npm install
#release: npm run-script build
#release: cd..
#release: python manage.py inspectdb
#release: python manage.py migrate
#release: python manage.py loaddata db.json
web: gunicorn snipcartwagtaildemo.wsgi:application --log-file -