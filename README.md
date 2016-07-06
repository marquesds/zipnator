# zipnator
Service that get a zipcode and saves its related address to MySQL

[![Build Status](https://travis-ci.org/marquesds/zipnator.svg?branch=master)](https://travis-ci.org/marquesds/zipnator)

# Setting up
1. Install `MySQL` and `libmysqlclient-dev`
2. Install all requirements: `pip install -r src/config/requirements/{environment}.txt`
3. Set `DJANGO_SETTINGS_MODULE` to `config.settings.{environment}`
4. Create a file called `secrets.json` inside `src/config/settings` folder. You can follow `secrets.template.json` example
5. Create database `zipnator`
6. Run `python src/manage.py migrate`
7. Run `python src/manage.py runserver`
8. Note: You can execute `scripts/setup.sh` to use the custom command `zipnator`
  - You'll can run project's command from any folder e.g. `zipnator runserver`, `zipnator test`, etc

# Testing
- Run: `python src/manage.py test`

# Testing API via curl
- List all: `curl -X GET http://127.0.0.1:8000/api/adresses/`
- List all with `limit` parameter: `curl -X GET http://127.0.0.1:8000/api/adresses/?limit=10`
- Get address by zipcode: `curl -X GET http://127.0.0.1:8000/api/adresses/14020260/`
- Save an address: `curl -X POST --data '{"zipcode": "14020260"}' http://127.0.0.1:8000/api/adresses/`
- Delete an address: `curl -X DELETE http://127.0.0.1:8000/api/adresses/14020260/`

# Licence
MIT License

Copyright (c) 2016 Lucas Marques

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
