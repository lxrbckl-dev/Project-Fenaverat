# Project Fenaverat
> A website portfolio crafted to showcase details about yourself, your servers, and your projects. V5. Fall 2025.

---

### Local Development
```bash
# Initiate
python -m venv venv
```
```bash
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```
```bash
# MacOS / Linux
source venv/bin/activate
python -m pip install -r requirements.txt
```

```bash
# Run
python app.py
```


### Local Deployment
```bash
sudo docker build -t fenaverat .
sudo docker run -d -p 8081:8048 fenaverat
```

### Server Deployment
```bash
docker run -d \
  --name fenaverat \
  --restart unless-stopped \
  -p 8048:8048 \
  lxrbckl/project-fenaverat:latest
```

---
### Resources
[`Docker Hub`](https://hub.docker.com/repository/docker/lxrbckl/project-fenaverat/general)