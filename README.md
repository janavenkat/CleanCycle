# CleanCycle -  Database Server

[![Build Status](https://travis-ci.com/mukul-rathi/CleanCycle.svg?branch=tutorial)](https://travis-ci.com/mukul-rathi/CleanCycle)

This is a database server used for storing sensor data collected by the Cambike team. It is used as an example in the blog post tutorials on setting up a database server with Docker, PostgreSQL and Flask. 

### Technologies used

The Cambike sensor measurements are stored in a PostgreSQL database, whilst the REST endpoint is written using Flask. These are each wrapped in their own Docker containers - to run them, run `docker-compose build` and `docker-compose up`. 

The bootstrap procedure initialises the database with the measurements in any CSV files in the `src/backups` repository (these have not been committed to the repo). 

The database schema can be found in the `src/db_connection.py` file, along with an interface for the common database operations. 

### Testing

The unit tests are in the `src/tests` directory - for each commit pushed to the repo, the Travis CI automatically builds an image from the testing Dockerfile and deploys the container (details of which are in the `docker-tests.yml` file). 

Inside the `test` container, Docker runs `pytest` for the database and endpoint unit tests. These tests also have `Coverage.py` so the overall test coverage for each of the python files can be seen.

To run the tests locally, run `docker-compose -f docker-tests.yml build` followed by `docker-compose -f docker-tests.yml run test` to run the database unit tests = You will need to supply the `POSTGRES_DB`, `POSTGRES_USER` and `POSTGRES_PASSWORD` environment variables in `test.env` in the project directory.

You can visualise the test coverage by clicking `tests/htmlcov/index.html`.

### Production - hosting on AWS

Use an EC2 instance, SSH into and copy across files and install Docker and Docker-Compose on the instance. You'll need to supply a `database.env` file in the root directory, containing the  `POSTGRES_DB`, `POSTGRES_USER` and `POSTGRES_PASSWORD` environment variables. You'll also need to ensure any database backup CSV files are copied across in `src/backups`. 

Then run `docker-compose build` and `docker-compose up` to run the production server. (Endpoint is on port 5000 although this can be changed by altering the forwarded port in the `docker-compose.yml` file.)

At this stage of the project, one EC2 instance should be sufficient, though in future AWS ECS or EKS (Kubernetes) could be used to orchestrate the Docker containers in production. 

### Code Style Guide
The code is written so as to conform to the [Google Python style guide](http://google.github.io/styleguide/pyguide.html). 

YAPF is used in a [pre-commit hook](https://github.com/google/yapf/blob/master/plugins/pre-commit.sh) to ensure consistent formatting. 

To enforce high code quality, Travis CI will run `pylint` as well as `yapf --diff` - these will pass if the code is rated as 10.00/10 for `pylint` and if the code in the commit has been `yapf` formatted. 

