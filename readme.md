# Enhanced Flask CAPTCHA Validation App with Docker Support

Here's an improved version of your Flask CAPTCHA validation app documentation, now including Docker support and some additional enhancements:

## 🧠 Flask CAPTCHA Validation App

A secure web application built with Flask to validate CAPTCHA inputs using flask-session-captcha with MongoDB for session storage. Effectively differentiates between human users and bots.

### 📌 Features
- ✅ CAPTCHA generation and validation
- 🔐 Server-side session management with MongoDB
- ⚙️ Easy integration with existing Flask forms
- 🧪 Clear success/failure feedback upon submission
- 🐳 Docker support for easy deployment
- 🌐 Configurable CAPTCHA settings

### 🏗️ Tech Stack
- **Backend**: Python (Flask)
- **CAPTCHA**: flask-session-captcha
- **Database**: MongoDB (for session storage)
- **Templating**: Jinja2
- **Containerization**: Docker

### 📂 Project Structure
```
flask-captcha-app/
│
├── templates/
│   └── form.html          # Frontend form with CAPTCHA
├── static/                # (Optional) For CSS/JS
│   └── styles.css
├── app.py                 # Main application logic
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🚀 Installation

### Option 1: Traditional Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/flask-captcha-app.git
   cd flask-captcha-app
   ```

2. **Create a Virtual Environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run MongoDB**
   Ensure MongoDB is running locally on port 27017 or configure a remote connection.

5. **Start the Flask App**
   ```bash
   python app.py
   ```
   Visit: http://localhost:5000

### Option 2: Docker Installation
1. **Build and Run with Docker Compose**
   ```bash
   docker-compose up --build
   ```
   This will start both the Flask app and MongoDB in containers.

2. **Access the Application**
   Visit: http://localhost:5000

## 📋 Usage
1. Open the home page in your browser
2. Enter the CAPTCHA as shown in the image
3. Submit the form
4. View the result:
   - ✅ CAPTCHA Success!
   - ❌ CAPTCHA Failed!

## ⚙️ Configuration
Customize CAPTCHA appearance in `app.py`:
```python
app.config['CAPTCHA_LENGTH'] = 5          # Number of characters
app.config['CAPTCHA_WIDTH'] = 160         # Image width
app.config['CAPTCHA_HEIGHT'] = 60         # Image height
app.config['CAPTCHA_DIFFICULTY'] = 'high' # Options: 'easy', 'medium', 'high'
```

## 🧩 Dependencies
- Flask
- Flask-Sessionstore
- flask-session-captcha
- PyMongo
- MongoDB (local or cloud)

## 💡 Notes
- For production use, consider:
  - Adding rate limiting
  - Using environment variables for secrets
  - Implementing HTTPS
- The Docker setup includes a MongoDB container for development
- Custom styling can be added in `static/styles.css`

## 📜 License
This project is open-source and available under the MIT License.

