# Project Explanation


The entire application Urls is within the app `project`.

There is app setup,  `elevator` .

`elevator` App is for all functioning

`views.py` contains the whole logic of the APIs .
`serializers.py` contains the logic to convert complex data types like queryset to json


# Assumptions
1. Elevator has only one button.
2. Elevator can go up or down.
3. Elevator fulfills the priorities of the requests.
4. If the elevator crosses the floor then priority floor is fulfilled and serves next.


Documentation below.


### Make a virtual enviroment
   
    Recommended python version -----> 3.9.X (The LATEST STABLE RELEASE)
    python -m venv myvenv

### Run the virtual enviroment

    myvenv\Scripts\activate.bat

### Install all dependencies

    pip install  -r requirements.txt

### Migrate

    python manage.py migrate
    
### Run the App
    
    python manage.py runserver

# REST API

The REST API to the  app is described below.

## Install Elevator
   to install the elevator with unique name, base floor, top floor.

### POST Request

`POST  /api/install/install_elevator/`

### body

    {
        "elevator_name": "e1",
        "current_floor": 0,
        "first_floor": 0,
        "last_floor": 10,
        "door": "CLOSE"
    }

### Response

    {
        "message": "Elevator is succesfully installed",
        "data": {
            "id": 6,
            "elevator_name": "e1",
            "maintenance": false,
            "current_floor": 0,
            "first_floor": 0,
            "last_floor": 10,
            "door": "CLOSE"
        }
    }

## update request

`PATCH /api/install/6/`

### body
    {
        "elevator_name": "e1",
        "current_floor": 0,
        "first_floor": 0,
        "last_floor": 9,
        "door": "CLOSE"
    }

    
## delete request

`DELETE  /api/install/5`


### body
    {
        "elevator_name": "e1"
    }



----------------------------------

## Maintainence
   To check the elevator is under maintenance or not and to change the status of maintainence

### GET Request

    GET  /api/maintenance/check_maintenance_status/

#### body

    {
        "elevator_name": "e1"
    }

### Response

    {
        "success": true, 
        "message": "Elevator is working"
    }

### PATCH Request

    PATCH /api/maintenance/set_maintenance/

#### body

    {
        "elevator_name": "e1"
        "maintenance": true
    }

### Response

    {
        "success": true, 
        "data":     {
            "elevator_name": "e1",
            "current_floor": 0,
            "first_floor": 0,
            "last_floor": 9,
            "maintenance": true,
            "door": "CLOSE"
        }

    }

-----------------------------

## Door status
API to open or close the door

### PATCH Request

    PATCH /api/door/open_or_close_door/

#### body

    {
        "elevator_name": "e1"
        "door": "OPEN"
    }

### Response

    {
        "success": true, 
        "data":     {
            "elevator_name": "e1",
            "current_floor": 0,
            "first_floor": 0,
            "last_floor": 9,
            "maintenance": true,
            "door": "OPEN"
        }

    }

---------------------------

## Save the user requests to destinations

### GET Request

    GET /api/userrequests/fetch_all_requests/

#### body

    {
        "elevator_name": "e1"
    }

### Response

    {
        "success": true, 
        "requests": [1,5,10]
    }


### GET Request

    GET /api/userrequests/get_elevator_direction/

#### body

    {
        "elevator_name": "e1"
    }


### Response

    {
        "success": true, 
        "direction": "moving up"
    }


### POST Request

    POST /api/userrequests/save_user_request/

#### body

    {
        "elevator_name": "e1"
        "floor": 8
    }

### Response

    {
        "success": true, 
        "data": {
            "elevator_name": "e1"
            "floor": 8
            },
        "destinations": [1,5,8,10]
    }

----------------------------------

## Elevator functioning
API for elevator functionings like elevator operation, destination reached, current floor status


### POST Request

    POST /api/elevator/next_destinations/

#### body

    {
        "elevator_name": "e1"
    }

### Response

    {
        "success":true,
        "destinations": [1,5,8,10],
        "next_destination": 1,
        "final_destination": 10,
        "current_floor": 0,
        "moving_direction_final_destination": 10,
        "current_direction": "moving up"
    }


### POST Request

    POST /api/elevator/reach_next_destination/

#### body

    {
        "elevator_name": "e1"
    }

### Response

    {
        "success":true, 
        "message": "destination reached successfully",
        "next_destination": 5
    }


### POST Request

    POST /api/elevator/destination_reached/

#### body

    {
        "elevator_name": "e1"
        "current_floor": 1
    }

### Response

    {
        "success":true, 
        "next_destination": [5,8,10],
        "current_floor": 1
    }

### GET Request

    POST /elevator/get_current_floor/

#### body

    {
        "elevator_name": "e1"
    }

### Response

    {
        "success":true, 
        "current_floor": 1
    }


# Video Demonstrating the APP Flows

https://clipchamp.com/watch/Ngkw0XzJJzc

# Postman documentation

https://documenter.getpostman.com/view/20110475/2s93sdZXuq

# Deployed link

https://jumping-minds-project.vercel.app/api/
