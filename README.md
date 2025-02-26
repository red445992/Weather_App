### Django Weather App
A simple weather application built using Django that fetches real-time weather data from the OpenWeatherMap API. Users can enter a city name to get weather details such as temperature, description, wind speed, and humidity.

## features
* Get real-time weather updates for any city.
* Displays temperature, weather description, wind speed, and humidity.
* Default city is set to Kathmandu if no input is given.
* Handles errors when an invalid city is entered.


## project structure
```
weatherapp/
│── app/                     # Django app
│   ├── migrations/          # Database migrations
│   ├── templates/           # HTML Templates
│   ├── static/              # Static files (CSS, JS, images)
│   ├── views.py             # Backend logic for fetching weather
│   ├── models.py            # Database models (if needed)
│   ├── urls.py              # URL routing
│   └── forms.py             # Forms (if needed)
│── weatherapp/              # Django project settings
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI entry point
│── db.sqlite3               # SQLite database (if used)
│── manage.py                # Django management commands
│── requirements.txt         # Dependencies list
│── README.md                # Project documentation
```



## Setup Instructions

Follow these steps to get the project up and running locally:

### 1. Clone the Repository

Start by cloning the repository to your local machine using the following command:

```bash
git clone https://github.com/red445992/Weather_App.git
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
```
* And activate the env
```bash
.\venv\Scripts\activate

```

### 3. install dependencies
```bash
pip install -r requirements.txt
```
### 4. apply database migrations
```bash
 python manage.py migrate
```
### 5.Create a Superuser (Optional)
```bash
python manage.py createsuperuser
```
### 6. run the development server
```bash
python manage.py runserver
```
