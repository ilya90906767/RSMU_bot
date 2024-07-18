RSMU Bot
========

Project Structure
----------------

The project is structured as follows:

* `rsmu_bot/`: The main project directory
	+ `apps/`: Django apps directory
	+ `media/`: Media files directory
	+ `settings.py`: Django project settings file
* `manage.py`: Django project management script
* `.env`: Environment variables file
* `db.sqlite3`: SQLite database file
* `requirements.txt`: List of dependencies required by the project

Deployment
----------

To deploy the project, follow these steps:

### 1. Create a virtual environment

Run the following command to create a virtual environment:
```python3 -m venv venv```

### 2. Install dependencies

Activate the virtual environment and install the dependencies listed in `requirements.txt`

### 3. Set up environment variables

Activate the virtual environment and run the following command to set up the environment variables:
```export PYTHONPATH=$PYTHONPATH:/your_path/RSMU_bot/rsmu_bot```

Replace `/your_path_to/RSMU_bot/rsmu_bot` with the actual path to your project directory.

### 4. Configure environment variables

Edit the `.env` file to set up the environment variables required by the project.

### 5. Run the bot and server

Run the following commands to start the bot and server:

```python3 manage.py run_bot``` 
```python3 manage.py runserver```

Note: Make sure to replace `/your_path_to/RSMU_bot/rsmu_bot` with the actual path to your project directory in step 3.
