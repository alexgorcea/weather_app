# Django Project: Weather Tracker

## Overview
Weather Tracker is a Django-based web application designed to provide real-time weather information and forecasts.
Users can view current weather conditions, search for weather by city, and see future weather forecasts.

## Features
- Real-time weather updates.
- Search functionality for finding weather by city.
- Detailed current weather conditions and future forecasts.
- Responsive design for desktop and mobile devices.

## Technical Details
- **Framework:** Django
- **Database:** SQLite3
- **Languages:** Python, HTML, CSS
- **Files and Folders:**
  - `weather_env/`: Virtual environment.
  - `weather/`: Core application files (models, views, templates, tests).
  - `weather_project/`: Project settings and configuration.
  - `weather/static/`: CSS files for styling.
  - `weather/templates/`: HTML templates for the user interface.
  - `db.sqlite3`: Default database where Django stores data.
  - `manage.py` : Command-line utility that lets you interact with this Django project in various ways

## Getting Started
To run this project locally:
1. Clone the repository.
2. Install Dependencies: `pip install -r requirements.txt`.
3. Start the virtual environment:`weather_env\Scripts\activate`.
4. Run migrations: `python manage.py migrate`.
5. Start the server: `python manage.py runserver`.
