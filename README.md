# Kaliningrad Regional Rail Web App

`Django 3.2.9` powered website with `LeafletJS` interactive map, stations list, routes and more.
`Bootstrap` framework and `PostreSQL` database is also used.

## Getting Started

The easiest way to try app is [Heroku deployed version](https://https://klines.herokuapp.com/), automatically deployed
from `master` branch.\

Another way is local setup of project environment with [virtualenv](https://virtualenv.pypa.io)
and [pip](https://pip.pypa.io).

```bash
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt

$ python manage.py migrate
$ python manage.py runserver
```

Then visit [http://localhost:8000](http://localhost:8000) to view the app.

## Features

- Interactive transit map on main page
- Two custom `manage.py` scripts `loadstations` and `loadtrains` for importing `.csv` files into PostreSQL DB.
- Stations list with search through station names
- Station details page with `openstreetmaps` map
- Trains list with origin and destination stations, and running days
- Train details page with timetable
- Custom 404 page