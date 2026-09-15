# Cafe & Wifi

A Flask-based web application for discovering and managing cafes suitable for working, studying, or relaxing.

The application provides a cafe directory where users can view information such as location, WiFi availability, power sockets, toilets, call-friendly spaces, available seating, coffee prices, images, and map locations.

Users can also add new cafes through a Bootstrap-styled form, with the information stored in a SQLite database using SQLAlchemy.

---

## Features

- View available cafes in a responsive card-based layout
- Add new cafes through a validated WTForms form
- Store and retrieve cafe information using SQLAlchemy
- SQLite database integration
- Bootstrap 5 responsive interface
- WiFi availability indicators
- Power socket availability indicators
- Toilet availability indicators
- Call-friendly space indicators
- Display available seating
- Display coffee prices
- Link cafes to map locations
- Display cafe images
- Delete cafes from the directory
- Flash messages for successful actions
- Environment variable support
- Deployment configuration with a `Procfile`

---

## Technologies Used

- **Python**
- **Flask**
- **Flask-SQLAlchemy**
- **SQLAlchemy**
- **Flask-WTF**
- **WTForms**
- **Flask-Bootstrap**
- **Bootstrap 5**
- **SQLite**
- **Jinja2**
- **HTML5**
- **CSS3**
- **Gunicorn**

---

## Project Structure

```text
Cafe-Wifi/
│
├── app.py
├── cafes.db
├── requirements.txt
├── Procfile
├── .gitignore
│
└── templates/
    ├── base.html
    ├── header.html
    ├── footer.html
    ├── index.html
    └── add.html

## Application Structure

### `app.py`

Contains the main Flask application, database configuration, SQLAlchemy model, WTForms form, and application routes.

### `cafes.db`

SQLite database containing the cafe records used by the application.

### `templates/`

Contains the Jinja2 templates used to render the application's pages.

| File | Purpose |
|---|---|
| `base.html` | Base template containing the common page structure, Bootstrap resources, and template blocks |
| `header.html` | Navigation bar |
| `footer.html` | Footer and dynamic copyright year |
| `index.html` | Homepage displaying the cafe directory |
| `add.html` | Cafe submission form using Bootstrap-Flask's `render_form()` |

---

## Routes

The application currently contains the following routes:

| Route | Method | Purpose |
|---|---|---|
| `/` | `GET` | Displays all cafes on the homepage |
| `/add` | `GET`, `POST` | Displays and processes the cafe submission form |
| `/delete/<cafe_id>` | `GET` | Deletes a cafe from the database |

### Home Route

The `/` route retrieves all cafes from the database and displays them on the homepage.

### Add Cafe Route

The /add route handles both displaying the form and processing submitted cafe information.

### Delete Route

The delete route retrieves a cafe by its ID, removes it from the database, and redirects back to the homepage.

### Database

The application uses SQLite as its database and SQLAlchemy as the Object-Relational Mapper (ORM).

The SQLAlchemy Cafe model maps to the existing cafe table in the SQLite database.

### Cafe Table

The database contains the following fields:

| Field            | Description                         |
| ---------------- | ----------------------------------- |
| `id`             | Unique cafe identifier              |
| `name`           | Name of the cafe                    |
| `map_url`        | Map/location URL                    |
| `img_url`        | Cafe image URL                      |
| `location`       | Cafe location                       |
| `has_sockets`    | Whether power sockets are available |
| `has_toilet`     | Whether a toilet is available       |
| `has_wifi`       | Whether WiFi is available           |
| `can_take_calls` | Whether calls can be taken          |
| `seats`          | Number of available seats           |
| `coffee_price`   | Price of coffee                     |

## Add Cafe Form

The application uses **Flask-WTF** and **WTForms** to create and validate the cafe submission form.

The form contains:

* Cafe name
* Location
* Coffee price
* Cafe map URL
* Cafe image URL
* WiFi availability
* Socket availability
* Toilet availability
* Call availability
* Number of seats

The form is rendered using Bootstrap-Flask's `render_form()` function.

---

## Bootstrap Integration

Bootstrap 5 is used to create a responsive and consistent user interface.

The project uses:

* Bootstrap navigation bar
* Responsive grid layout
* Cafe cards
* Buttons
* Badges
* Alerts
* Responsive forms
* Bootstrap Icons

Bootstrap-Flask is also used to integrate Bootstrap with Flask-WTF forms.

---

## Environment Variables

The application uses Python's built-in `os` module to retrieve configuration values from environment variables.


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/okwuchukwuchiedozie-stack/Cafe-Wifi.git
```

### 2. Navigate to the Project

```bash
cd Cafe-Wifi
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The application will run using Flask's development server.

Open the local address provided by Flask in your browser to access the application.

---

## Requirements

The project's dependencies are listed in `requirements.txt`.


## Deployment

The project includes a `Procfile` that defines the web process used during deployment.

The deployment process uses **Gunicorn** to serve the Flask application.

### Procfile

```text
web: gunicorn app:app
```


