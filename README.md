# MeTube 🎬

**MeTube** is a quick and simple clone of YouTube, built using Django and Bootstrap—just a lil' project for fun. It mimics core YouTube functionality like video listing and playback, with a clean, responsive UI.

## 🔥 Features

- 🗂️ Video listings with titles & descriptions
- 🎥 Embedded video playback (YouTube/Vimeo or local files)
- 🧭 Simple routing using Django Views
- 💅 Styled using Bootstrap for mobile responsiveness

## 🛠️ Tech Stack

- **Backend:** Django
- **Frontend:** HTML5, Bootstrap 5, a lil’ sprinkle of CSS/JS
- **Database:** SQLite (default Django DB, coz this is chill af)
- **Deployment:** Local (for now... 👀)

## 📦 Getting Started

Clone the repo:

```bash
git clone https://github.com/HrishiShinde/MeTube.git
cd MeTube
```

Create a virtual environment and install dependencies:

```bash
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
```

Run the server:

```
python manage.py migrate
python manage.py runserver
```
