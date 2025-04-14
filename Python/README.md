#  Dockerized Data Processor (Python + Pandas)

This project demonstrates how to containerize a simple Python script using Docker. The script processes a CSV file using `pandas` and prints summary statistics.

---

##  Project Structure

```
.
 process_data.py  
 requirements.txt  
 Dockerfile  
 data  
     data.csv  
```

---

##  Step 1: Create the Dockerfile

Create a `Dockerfile` in the root directory:

```Dockerfile
FROM python:3.10-slim  
WORKDIR /app  
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  
COPY . .  
CMD ["python", "process_data.py"]
```

---

##  Step 2: Create `requirements.txt`

```txt
pandas  
numpy
```

---

##  Step 3: Create the Python script

```python
import pandas as pd  
df = pd.read_csv('data/data.csv')  
print("Summary statistics:\n")  
print(df.describe())
```

---

##  Step 4: Add Sample CSV

Create `data/data.csv` with the following content:

```csv
name,age,score  
Alice,25,88  
Bob,30,92  
Charlie,22,95
```

---

##  Step 5: Build the Docker Image

```bash
docker build -t data-processor .
```

---

##  Step 6: Run the Container

```bash
docker run --rm -v $(pwd)/data:/app/data data-processor
```

---

##  What This Does

- Reads the CSV from `data/data.csv`  
- Prints summary using `pandas`  
- All inside a lightweight Docker container  

---

##  You're Done!

Youve successfully Dockerized a Python script with external data.  
Now its portable, reproducible, and professional! 

