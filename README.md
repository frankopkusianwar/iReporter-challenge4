[![Maintainability](https://api.codeclimate.com/v1/badges/4ba878ad3885190eb0d1/maintainability)](https://codeclimate.com/github/frankopkusianwar/iReporter-challenge3/maintainability) [![Build Status](https://travis-ci.org/frankopkusianwar/iReporter-challenge3.svg?branch=develop)](https://travis-ci.org/frankopkusianwar/iReporter-challenge3) [![Coverage Status](https://coveralls.io/repos/github/frankopkusianwar/iReporter-challenge3/badge.svg?branch=develop)](https://coveralls.io/github/frankopkusianwar/iReporter-challenge3?branch=develop)

# iReporter 
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention

## Requirements
- python 3.7 -programming language that can be used on any mordern operating system
- Virtual environment -allows you to have an issolated evnvironment for your project where you can install all your dependencies
- Flask -a python framework for that can be used to add functionality to your API endpoints
## Functionality
- `create red-flag record` Enables user to create a red-flag record
- `Get all red-flags` Enables user to view all red-flag records
- `Get all interventions` Enables user to view all intervention records
- `Get single red-flag` Enables user  to get a specific red-flag record
- `Get single intervention` Enables user  to get a specific intervention record
- `update comment` Enables  user to add a comment to a red-flag record 
- `create new user` Enables  users to create accounts
- `create login user` Enables  users to access all the protected endpoints
- `update location` Enables  users to update specific red-flag and intervention location 
- `delete red-flag`Enables users to delete red-flag  records
- `delete intervention`Enables users to delete intervention  records
## Heroku Link
- https://ireporter3-challenge3.herokuapp.com
## Installation
Clone the repository
```
$ https://github.com/frankopkusianwar/iReporter-challenge3.git
$ cd iReporter
```
Install virtualenv and create a virtual envirinment
```
$ pip install virtualenv
$ pip install virtualenvwrapper
$ virtualenv venv
$ source/venv/bin/activate
```
Install all the necessary dependencies
```
pip install -r requirements.txt
```

## Run the application
At the terminal or console type
```
python run.py
```
To run tests run this command at the console/terminal and add the test file name
```
pytest --cov
```
## Versioning
```
This API is versioned using url versioning starting, with the letter 'v'
This is version one"v1" of the API
```
## End Points
|           End Point                      |     Functionality                                   |
|------------------------------------------|-----------------------------------------------------|
|     POST api/v1/red-flags                  |creates a new red-flag record                  |  
|     GET  api/v1/red-flags                  |get all red-flag records                    |   
|     GET  api/v1/red-flags/<red-flag-id>          |get a specific red-flag record                 |  
|     PATCH api/v1/red-flags/<red-flag-id>/comments           |adds a comment to a red-flag record      |
|     PATCH api/v1/red-flags/<red-flag-id>/location             |update red-flag record location|
|     POST api/v1/users                    |registers users                                      |
|     DELETE GET  api/v1/red-flags/<red-flag-id>              |delete red-flag record                                     |
|     GET  api/v1/interventions                  |get all intervention records                    |
|     GET  api/v1/interventions/<red-flag-id>          |get a specific intervention record                 |
|     PATCH api/v1/interventions/<red-flag-id>/comments           |adds a comment to an intervention record       |
|     PATCH api/v1/interventions/<red-flag-id>/location             |update  intervention location|
  

## Authors
- Okiror Frank
## licencing
This app is open source and therefore is free to all users
