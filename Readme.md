# Django & Django REST framework test project.

The test project won't be used in any real environment.

Applicant Name: Frank Uchenna
contact email: frankuchenna30@gmail.com

## Initial Project setup

    originally cloned from: https://bitbucket.org/staykeepersdev/bookingengine.git

    completed task can be cloned from: https://github.com/codeOlam/bookingEngineTask

    python -m venv venv
    pip install -r requirements.txt
    python manage.py runserver

    There is a pre-build structure for Hotels/Apartments (could be changed or extended). Database is prefilled with information - **db.sqlite3**.

    - superuser
        - username: **admin**
        - password: **admin**

## Swagger documentation

    - http://localhost:8000/
    - http://localhost:8000/redoc/

## To Create Test Data

    - Go to admin dashboard.
    - Then locate BookingInfos table
    - click to load table.
    - from the data on the table, update the following informations to create a reservation
        - set isBooked: Yes
        - set check_in: date
        - set check_out: date
    - Then go back to admin bashboard home page, click on Reservation to view reservations created.

## Test Case example:

    For covering more test cases we are going to need at least one hotel with 3 Hotel Room Types:

    - First with price=50 (below max_price) with blocked day inside the search criteria for all rooms(could be 1 room)

    - Second with price=60 (below max_price) with blocked day insde the search criteria for one out of few rooms

    - Third with price 200 (above max_price)

## Request example:

    http://localhost:8000/api/v1/units/?max_price=100&check_in=2021-12-09&check_out=2021-12-12

## Response example:

    {
        "items": [
            {
                "listing_type": "Apartment",
                "title": "Luxurious Studio",
                "country": "UK",
                "city": "London",
                "price": "40"

            },
            {
                "listing_type": "Hotel",
                "title": "Hotel Lux 3***",
                "country": "BG",
                "city": "Sofia",
                "price": "60" # This the price of the first Hotel Room Type with a Room without blocked days in the range

            },
            {
                "listing_type": "Apartment",
                "title": "Excellent 2 Bed Apartment Near Tower Bridge",
                "country": "UK",
                "city": "London",
                "price": "90"
            },
        ]
    }
