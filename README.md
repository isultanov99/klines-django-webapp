# Regional Rail Web App

Django `3.2.9` powered website with interactive map, stations list, routes and more.

## Getting Started

Local setup of project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ cd src/
$ python manage.py migrate
$ python manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

## Features

- Interactive transit map on main page
- Stations list with search through station names
- Station details page with `openstreetmaps` map
- Custom 404 page