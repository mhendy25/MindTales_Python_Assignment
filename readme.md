# Lunch Service

Lunch Service is a Django-based web application that allows users to manage restaurants and their menus. Users can sign up, log in, add restaurants, and vote for their favorite menus.

## Table of Contents

- Installation
- Usage
- Project Structure
- Features

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/mhendy25/MindTales_Python_Assignment.git
   cd lunch_service
   ```

2. Build and start the Docker containers:

   ```sh
   docker-compose up --build
   ```

3. Apply the migrations:

   ```sh
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:

   ```sh
   docker-compose exec web python manage.py createsuperuser
   ```

5. Create a superuser:

   ```sh
   python manage.py createsuperuser
   ```

6. Signup, login, & continue using the app:
   ```sh
   http://0.0.0.0:8000/signup/
   ```

## Usage

1. Open your web browser and navigate to [`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).
2. Sign up for a new account or log in if you already have one.
3. Add new restaurants and menus.
4. Vote for your favorite menus.

## Project Structure

```plaintext
.gitignore                # Git ignore file
lunch_service/
    db.sqlite3            # SQLite database file
    lunch_service/
        __init__.py       # Package initialization
        __pycache__/      # Compiled Python files
        asgi.py           # ASGI configuration
        middleware.py     # Custom middleware
        settings.py       # Django settings
        urls.py           # URL routing
        wsgi.py           # WSGI configuration
    manage.py             # Django management script
    requirements.txt      # Project dependencies
    restaurant/
        __init__.py       # Package initialization
        __pycache__/      # Compiled Python files
        admin.py          # Admin configuration
        apps.py           # App configuration
        forms.py          # Form definitions
        migrations/
            __init__.py   # Package initialization
            __pycache__/  # Compiled Python files
            0001_initial.py  # Initial migration
            0002_rename_rating_menu_voting.py  # Rename rating to voting
            0003_alter_menu_voting.py  # Alter menu voting field
            0004_customuser.py  # Custom user model migration
            0005_delete_customuser.py  # Delete custom user model
        models.py         # Data models
        templates/
            restaurant/
                add_menu.html  # Template for adding a menu
                index.html     # Template for the index page
                login.html     # Template for the login page
                menu.html      # Template for displaying a general menu
                menu1.html     # Template for displaying menu1 for build 1.x
                menu2.html     # Template for displaying menu2 for build 2.x
                results.html   # Template for displaying results
                signup.html    # Template for the signup page
        tests.py          # Unit tests
        urls.py           # URL routing for the restaurant app
        views.py          # View functions
readme.md                # Project documentation
```

## Endpoints (API Documentation)

### User Authentication

- **Sign Up**
  - **URL:** `/signup/`
  - **Method:** `POST`
  - **Form:** `SignUpForm`
- **Log In**
  - **URL:** `/login/`
  - **Method:** `POST`
  - **Form:** `LoginForm`

### Restaurant Management

- **Add Restaurant**
  - **URL:** `/restaurant/`
  - **Method:** `POST`
  - **Form:** `RestaurantForm`
- **View Restaurants**
  - **URL:** `/restaurant/`
  - **Method:** `GET`
  - **Template:** `restaurant/index.html`

### Menu Management

- **View Menu**
  - **URL:** `/{restaurant_id}/menu/`
  - **Method:** `GET`
  - **Template:** `restaurant/menu.html`
- **View Menu with Build Version 1.x**
  - **URL:** `{restaurant_id}/menu1/`
  - **Method:** `GET`
  - **Template:** `restaurant/menu1.html`
- **View Menu with Build Version 2.x**
  - **URL:** `/{restaurant_id}/menu2/`
  - **Method:** `GET`
  - **Template:** `restaurant/menu2.html`

### Voting

- **Vote for Menu**
  - **URL:** `/vote/{menu_id}/`
  - **Method:** `POST`
- **View Top Voted Menus**
  - **URL:** `/top-menus/`
  - **Method:** `GET`
  - **Template:** `restaurant/results.html`

## Models

### Restaurant

- **Name:** `name` (CharField, max_length=255)
- **Location:** `location` (CharField, max_length=255)
- **Phone Number:** `phone_number` (CharField, max_length=255)

### Menu

- **Restaurant:** `restaurant` ForeignKey to Restaurant
- **Name:** `name` CharField, max_length=255
- **Western Cuisine:** `western_cuisine` models.JSONField(default=dict)
- **Arab Cuisine:** `arab_cuisine` models.JSONField(default=dict)
- **Vegeterian Cuisine:** `Vegeterian_cuisine` models.JSONField(default=dict)
- **Date:** `date` models.DateField()
- **Voting:** `voting` (IntegerField)

## Testing

To run the tests, you can use the following command:

```sh
python manage.py test restaurant
```

## Features

- User authentication (sign up, log in)
- Add and manage restaurants
- Add and manage menus
- View menus based on build version
- Vote for menus
- View top voted menus
