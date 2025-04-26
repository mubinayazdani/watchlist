🎬 Movie Watchlist
A simple Flask web app for managing your favorite movies.
Add, edit, and delete movies from your personal watchlist!

🚀 Features
Add new movies with title, genre, year, rating, and watched status ✅

Edit movie details ✏️

Delete movies from your list 🗑️

Responsive and modern UI with Bootstrap 🌐

Flash messages for feedback 🔔

🛠️ Built With
Python 🐍

Flask ⚡

Flask-WTF (Forms) 📄

SQLite (Lightweight Database) 🗄️

Bootstrap 5 🎨

📸 Screenshots
(You can add some screenshots here later if you want!)

📦 Installation
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/your-username/watchlist.git
cd watchlist

# 2. Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate

# 3. Install the dependencies
pip install -r requirements.txt

# 4. Run the application
python app.py
The app will be available at http://localhost:5000

⚙️ Deployment
You can easily deploy this app on platforms like:

Render

Railway

Heroku (with some tweaks)

Make sure to set the correct Start Command when deploying:

bash
Copy
Edit
gunicorn app:app
🧹 Project Structure
arduino
Copy
Edit
watchlist/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   └── edit_movie.html
│
├── static/
│   └── (Optional: CSS / images)
│
├── app.py
├── config.py
├── forms.py
├── models.py
├── requirements.txt
└── README.md
