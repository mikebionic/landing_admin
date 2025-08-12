# Landing Admin

This is a Python Flask API with a simple UI to serve as an admin panel for a landing page.
It also provides a REST API for the landing page frontend and supports building landing pages using Flask templating.

**Note:** This is an old project with legacy code & dependencies (2020).

---

## Setup and Configuration

1. **Create migration config**
   Copy `example.migration.json` to `app.migration.json` and customize it as needed.

2. **Create database**
   Create a PostgreSQL database named `landing_admin`.

3. **Static files**
   Place your static web files inside the `/static` directory.

4. **Uploads directory**
   Create an uploads folder inside `/static` by running:

   ```bash
   mkdir -p static/uploads
   ```

---

## Running the Application

Run the Flask app as usual (example):

```bash
export FLASK_APP=app.py
flask run
```
