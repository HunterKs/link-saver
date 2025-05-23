# 🔗 Link Saver

A Django-based web application to save, organize, and manage your favorite links/bookmarks with summaries.

[**Live Demo**](https://link-saver-6h6d.onrender.com)

This project demonstrates secure user authentication, password hashing, modern Django best practices, and a clean, responsive UI.

---

## 🚀 Features

- **User Registration & Login:**  
  Secure account creation and authentication using email and password.

- **Password Security:**  
  Passwords are never stored in plain text. Django uses PBKDF2 (with a salt) for secure password hashing.

- **Bookmark Management:**  
  - Save links with titles and descriptions  
  - View, edit, and delete bookmarks  
  - (Planned) Option to resummarize bookmarks using AI

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
- **Deployment:** [Render](https://render.com) (live at [link-saver-6h6d.onrender.com](https://link-saver-6h6d.onrender.com))

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

## 🔐 Password Security

- Django stores passwords as salted hashes using PBKDF2 (configurable in `settings.py`).
- Passwords are **never** stored or transmitted in plain text.
- You can verify this by checking the `auth_user` table in the database—passwords start with the algorithm used, e.g., `pbkdf2_sha256$...`.

---
## 📸 Screenshots

login_page: ![image](https://github.com/user-attachments/assets/cc6088c8-b654-4734-93e7-edc9e428a7b3)
register_page: ![image](https://github.com/user-attachments/assets/3bac7c42-6fc3-4770-89f3-3f720f47a333)
home_page: ![image](https://github.com/user-attachments/assets/d8d6c46a-6579-44fd-af7b-8b60f5efd1a6)
add_bookmark: ![image](https://github.com/user-attachments/assets/6b7962be-8de2-4bb1-bb6a-eccf921c9220)
user_profile: ![image](https://github.com/user-attachments/assets/15bbc95c-4858-4ea0-b735-f4e26e61c728)
for_more_dummarydetails: just click on the row: ![image](https://github.com/user-attachments/assets/72c0210a-48eb-45d9-a481-97560746ff75)


## 💡 What I'd Do Next / Future Improvements

- **AI Summarization & Resummarize:**  
Integrate advanced AI models (e.g., Hugging Face Transformers, OpenAI, or Jina AI) for smarter, more accurate link summaries.  
Example future code:
import requests
def get_summary(text):
response = requests.post("https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
headers={"Authorization": "Bearer YOUR_TOKEN"},
json={"inputs": text})
return response.json()['summary_text']

- **On-Demand Resummarize:**  
Let users update summaries as web content changes.

- **ML Model Optimization:**  
Use lightweight models or external inference APIs to keep hosting costs low and performance high.

- **Custom Tags & Organization:**  
Add tags, folders, or search to organize bookmarks.

- **Social Features:**  
Share bookmarks with friends or make collections public.

- **Progressive Web App (PWA):**  
Enable offline access and mobile install.

---

## ⏱️ Time Spent

- **Development:7 hours 
- **Testing & Deployment:3 hours

---

## ✅ Submission Checklist

- [x] Public (or private‑invite) GitHub repo
- [x] Live link ([Render](https://link-saver-6h6d.onrender.com))
- [x] Clear README: tech stack, setup, "what I'd do next," and time spent
- [x] 2–5 screenshots or a short GIF (to be added)
- [x] At least a couple of unit / component / widget tests
- [x] Small, logical commit history

---

## 🙏 Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Render](https://render.com/)
- [GitHub](https://github.com/)

---






