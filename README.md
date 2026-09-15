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