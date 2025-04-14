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

1. **Flask** connects to **MySQL** (💻➡️🐬).
2. MySQL sends back the message **"Hello, Docker!"** 📝.
3. **Flask** shows that message in the browser for the user 🚀.

---

## 🛠️ Step-by-Step Explanation 📖

---

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
```

🧠 **What It Does:**  
- Flask runs a simple web app.  
- It connects to MySQL container.  
- Executes a query to get a string.  
- Returns the result in the browser.

---

### 🔹 Step 2: Create `requirements.txt` 📜

```
flask
mysql-connector-python
```

📦 **Why Needed?**  
These are the Python dependencies needed for the Flask app to work and connect to MySQL.

---

### 🔹 Step 3: Write the `Dockerfile` 🐳

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

⚙️ **What It Does:**  
- Uses Python 3.9 base image.  
- Installs required libraries.  
- Copies all project files.  
- Starts the Flask app.

---

### 🔹 Step 4: Create `docker-compose.yml` 📄

```yaml
version: '3'
services:
  db:
    image: mysql:5.7
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: test_db
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      FLASK_ENV: development
    volumes:
      - .:/app

volumes:
  db_data:
```

🔗 **What It Does:**  
- Starts MySQL container named `db`.  
- Builds Flask app from `Dockerfile`.  
- Links both containers so Flask can talk to MySQL.  
- Uses volumes for persistent data.

---

### 🔹 Step 5: Run the App 🚀

```bash
docker-compose up -d --build
```

💡 **What Happens:**  
- Docker builds and starts both containers in detached mode.  
- Flask app runs on port **5000**.  
- MySQL container listens on port **3306**.

---

### 🔹 Step 6: Open in Browser 🌍

Go to:

```
http://<your-ec2-ip>:5000
```

✅ **You Should See:**  
`Hello, Docker!` — straight from MySQL!

---

### 🔹 Step 7: Stop the Containers ⏹️

```bash
docker-compose down
```

🧹 **What It Does:**  
Stops and removes both containers and networks gracefully.

---

## 🎉 You Did It!

You’ve just built your **first multi-container Docker app** using:
- 🐍 **Flask** for web logic  
- 🐬 **MySQL** as the database  
- 🐳 **Docker Compose** to run and connect them  

👏 Now you're ready to scale and deploy like a pro!

---

## 🔥 Next Steps:
- Deploy on **AWS EC2**, **Render**, or **Railway**
- Add features like user input, API routes, or UI
- Scale your app using **Docker Swarm** or **Kubernetes**

---

Made with ❤️ by Asif Shaikh 🚀
