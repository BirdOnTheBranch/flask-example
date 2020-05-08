&nbsp;

# flask-example

&nbsp;

>Basic example Flask hello world.

&nbsp;

---

## Setup

*Ensure you have Docker installed in your system.*

&nbsp;

**-First we build the docker-compose.**


`$ docker-compose build`  

*You should get an output like this:*

```
...
Step 1/5 : FROM python:3.8-slim-buster
3.8-slim-buster: Pulling from library/python
...

...
---> a1c95d6a940f
Successfully built 
Successfully tagged flask-example_web:latest
...

```

&nbsp;

**-Second run the server sqlite3 in background, and
conect your host at flask-server.**


`$ docker-compose up -d`


*You should get an output like this:*

`Creating flask-example_web_1 ... done`

&nbsp;

---

## Starting the application

-To run the application, open a terminal and call `docker-compose run` using the port `8000`.


`$ docker-compose run web`


*You should get an output like this:*

```
Starting server
 * Serving Flask app "hello" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:8000/ (Press CTRL+C to quit)
```

&nbsp;

**welcome to Flask-example.**