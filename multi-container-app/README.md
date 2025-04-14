# 🐳 Multi-Container Flask + MySQL App using Docker Compose 🎉

## 📌 What Did We Build?
We created a **cool web app** using:
- 🐍 **Flask (Python)** for the web server  
- 🐬 **MySQL** for the database  
- 🐳 **Docker Compose** to run both in separate **containers** that talk to each other 🤖💬

When someone visits the app, it fetches a message **from MySQL** and displays it. It’s like a tiny **Flask-powered server** with a **database** 💥

---

## ✅ What Does the App Do?

When someone visits your app at `http://<your-ip>:5000`, the app:

1. **Flask** connects to **MySQL** (💻➡️🐬)  
2. MySQL sends back the message **"Hello, Docker!"** 📝  
3. **Flask** shows that message in the browser for the user 🚀

---

## 🛠️ Step-by-Step Explanation 📖

### 🔹 Step 1: Write `app.py` (Flask Code) 👨‍💻

```python
from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host="db",
        user="root",
        password="example",
        database="test_db"
    )
    return connection

@app.route('/')
def hello():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello, Docker!'")
    result = cursor.fetchone()
    conn.close()
    return result[0]
