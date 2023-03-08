<h1 align="center">
<br>
projeto_auth_backend
</h1>

<p align="center">Simple API for user authentication. Developed to apply for a vacancy.</p>

<hr />

## Features

These are the features I used in developing this project.

- **Python** — Open-source and compiled language.
- **FastAPI** — Web framework for building APIs with Python.
- **SQLAlchemy** —  SQL object-relational mapping library in python.
- **Docker Compose** — Docker's container orchestrator.
- **MySQL** — Relational database.

## Dependencies

I have specified in 'requirements.txt' the dependencies used in this project. I tried to put everything in a container but couldn't do it in time. After installing them (using pip), you can go to the next step and run the application.

## Getting started

```bash
# Clone this repository
$ git clone https://github.com/guilhermecostam/projeto_auth_backend.git

# Create your .env file and overwrite
$ cp .env.example .env

# Run docker compose
$ docker-compose up -d

# Now, run the application
$ python3 -m uvicorn app.main:app --reload 
```

## Access to the API
All requests to the API can be found at:

```shell
localhost:8000/docs
```

---

Made with :zap: by Guilherme Costa. [Get in touch!](https://www.linkedin.com/in/guilhermecostam/)