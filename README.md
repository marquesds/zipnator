# zipnator
Service that get a zipcode and saves the address to MySQL

[![Build Status](https://travis-ci.org/marquesds/zipnator.svg?branch=master)](https://travis-ci.org/marquesds/zipnator)
[![Coverage Status](https://coveralls.io/repos/github/marquesds/zipnator/badge.svg?branch=master)](https://coveralls.io/github/marquesds/zipnator?branch=master)

# Setting up
1. Install `MySQL` and `libmysqlclient-dev`
2. Install all requirements: `pip install -r src/config/requirements/{environment}.txt`
3. Set `DJANGO_SETTINGS_MODULE` to `config.settings.{environment}`
4. Create a file called `secrets.json` inside `src/config/settings` folder. You can follow `secrets.template.json` example
5. Run `python src/manage.py migrate`
6. Run `python src/manage.py runserver`
7. Note: You can execute `scripts/setup.sh` to use the custom command `zipnator`
  - You'll can run project's command from any folder e.g. `zipnator runserver`, `zipnator test`, etc

# Testing
- Run: `python src/manage.py test`

# Testing api via curl
- List all: `curl -X GET http://127.0.0.1:8000/api/adresses/`
- Get address by zipcode: `curl -X GET http://127.0.0.1:8000/api/adresses/14020260/`
- Save an address: `curl -X POST --data '{"zipcode": "14020260"}' http://127.0.0.1:8000/api/adresses/`
- Delete an address: `curl -X DELETE http://127.0.0.1:8000/api/adresses/14020260/`
