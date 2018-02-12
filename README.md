# Running the app

1. Create a virtual environment with virtualenv/venv3 in the parent directory.

2. Activate the virtual environment.

3. Install the required packages:

```
     $ pip install -r requirements.txt
```

4. Run start_server.sh (creates the database and runs the local server):

```
     $ ./start_server.sh
```
The app is run with active debugger, to switch it off go to run.py and change *debug* to False.

The app can be viewed at http://127.0.0.1:8080.

