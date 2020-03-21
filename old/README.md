## Running the example.

### 1. Set up Rabbitmq docker.
```bash
sudo docker run -d -p 5672:5672 rabbitmq
```

### 3. Create the venv
```bash
python3 -m venv venv
```
Install prerequisites
```bash
pip3 install -r requirements.txt
```

### 2. Start a celery worker.
You'll need a worker to get things done, run the following command in a separate terminal tab:

(From the project folder)

```bash
celery worker -A celery_worker.celery --loglevel=info 
```

### 3. Start the app.

Open a new terminal tab and start the app:

```bash
python3 run.py
```

### 4. Try it!
On your browser, go to: `http://localhost:5000/flask_celery_howto.txt/it-works!`
