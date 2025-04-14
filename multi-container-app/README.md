Bilkul bhai! Ab main tujhe exact **code** format mein `README.md` file ka content de raha hoon  jise tu direct GitHub pe paste karega aur **proper display** hoga 

---

###  Final `README.md` Code:

```markdown
#  Multi-Container Flask + MySQL App using Docker Compose

This project shows how to run a simple web app using **Flask (Python)** and **MySQL**, inside Docker containers, using **Docker Compose**.

---

##  Whats Inside?

-  Flask app (web server)
-  MySQL database
-  Both run in containers using Docker Compose

When you visit the app in your browser, it connects to MySQL and shows this message:

```
Hello, Docker!
```

---

##  Folder Structure

```
multi-container-app/
 app.py                # Flask app
 requirements.txt      # Python packages
 Dockerfile            # Builds Flask image
 docker-compose.yml    # Runs Flask + MySQL together
```

---

##  How to Run

### 1 Create all files

Create these files inside a new folder:

- `app.py`
- `requirements.txt`
- `Dockerfile`
- `docker-compose.yml`

---

### 2 `app.py`

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

if __name__ == "__main__":
    app.run(host="0.0.0.0")
```

---

### 3 `requirements.txt`

```
flask
mysql-connector-python
```

---

### 4 `Dockerfile`

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

---

### 5 `docker-compose.yml`

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

---

### 6 Run the app

```bash
docker-compose up -d --build
```

---

##  Open the app

Go to:  
`http://<your-ec2-ip>:5000`  
Example: `http://3.79.16.2:5000`

---

##  Stop containers

```bash
docker-compose down
```

---

##  Done!

Youve built your first multi-container Docker app! 
```

---


