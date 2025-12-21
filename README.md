# Project Fenaverat

### Installation
```bash
python -m venv venv
```
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# macOS / Linux
source venv/bin/activate
python -m pip install -r requirements.txt
```

### Run
```bash
python app.py
```

---

### Deployment
```bash
sudo docker build -t fenaverat .
sudo docker run -d -p 8000:8000 fenaverat
```

---