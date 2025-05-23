# Link Saver

A Django-based web application to save, organize, and manage your favorite links/bookmarks with summaries.  
This project demonstrates secure user authentication, password hashing, and modern Django best practices.

---

## 🚀 Features

- **User Registration & Login:**  
  Secure account creation and authentication using email and password.

- **Password Security:**  
  Passwords are never stored in plain text. Django uses PBKDF2 (with a salt) for secure password hashing.

- **Bookmark Management:**  
  - Save links with titles and descriptions.
  - View, edit, and delete bookmarks.
  - Option to resummarize bookmarks.

- **User Profile Modal:**  
  View account details and log out from anywhere in the app.

- **Responsive UI:**  
  Modern, clean interface for desktop and mobile.

---

## 🛠️ Tech Stack

- **Backend:** Django (Python 3.x)
- **Frontend:** Django Templates, Bootstrap (or your CSS framework)
- **Database:** SQLite3 (default, can be switched to PostgreSQL/MySQL)
- **Authentication:** Django’s built-in user model and auth system
- **Password Hashing:** PBKDF2 with SHA256 (Django’s default)
- **Session Management:** Django sessions
- **Deployment Ready:** Easily deployable to Heroku, PythonAnywhere, or any WSGI server

---

## 🔐 Password Security

- **Django stores passwords as salted hashes** using PBKDF2 (configurable in `settings.py`).
- Passwords are never stored or transmitted in plain text.
- You can verify this by checking the `auth_user` table in the database—passwords start with the algorithm used, e.g., `pbkdf2_sha256$...`.

---

## 📦 Project Structure

link-saver/
├── bookmarks/ # Django app for bookmark logic
├── link_saver/ # Project settings and URLs
├── templates/ # HTML templates
├── static/ # CSS, JS, images
├── db.sqlite3 # Database (default)
├── manage.py
└── venv/ # Virtual environment (should be in .gitignore)




---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [GitHub](https://github.com/)

