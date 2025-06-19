# 🧠 Flask CAPTCHA Validation App

A simple web application built with Flask to validate CAPTCHA inputs using `flask-session-captcha` and MongoDB for session storage. This app helps differentiate between human users and bots.

## 📌 Features

- ✅ CAPTCHA generation and validation
- 🔐 Server-side session management with MongoDB
- ⚙️ Easy integration with existing Flask forms
- 🧪 Basic success/failure feedback upon submission

---

## 🏗️ Tech Stack

- **Backend:** Python (Flask)
- **CAPTCHA:** flask-session-captcha
- **Database:** MongoDB (for session storage)
- **Templating:** Jinja2

---

## 📂 Project Structure

flask-captcha-app/
│
├── templates/
│ └── form.html # Frontend form with CAPTCHA
├── app.py # Main application logic
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🚀 Installation

### 1. Clone the Repository

git clone https://github.com/your-username/flask-captcha-app.git
cd flask-captcha-app
2. Create a Virtual Environment (optional but recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -U Flask flask-session-captcha Flask-Sessionstore pymongo
4. Run MongoDB
Ensure MongoDB is running locally on port 27017.

5. Start the Flask App
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

📋 Usage
Open the home page in the browser.

Enter the CAPTCHA as shown in the image.

Submit the form.

View the result:

✅ CAPTCHA Success!

❌ CAPTCHA Failed!

📸 Screenshots
You can add screenshots here to show the UI.

🧩 Dependencies
Flask

Flask-Sessionstore

flask-session-captcha

PyMongo

MongoDB (local or cloud)

💡 Notes
Make sure MongoDB is properly installed and running on localhost:27017.

You can customize CAPTCHA appearance using:

python
Copy
Edit
app.config['CAPTCHA_LENGTH'] = 5
app.config['CAPTCHA_WIDTH'] = 160
app.config['CAPTCHA_HEIGHT'] = 60
📜 License
This project is open-source and available under the MIT License.

yaml
Copy
Edit

---

Let me know if you'd like to add Docker support, Postman collection, or deployment ins
