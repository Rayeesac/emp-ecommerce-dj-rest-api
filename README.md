### Employee and Ecommerce Django REST API
----------

Clone Git
----------

git clone https://github.com/Rayeesac/emp-ecommerce-dj-rest-api.git

Run Docker 
----------

```
cd emp-ecommerce-dj-rest-api/ && docker-compose -f docker-compose.yml up -d --build
```

Restore Database
---------

```
cd sql/ && cat emp_ecommerce.sql | docker exec -i postgres psql -U postgres
```

Down and Up Docker
--------

```
cd ../ && docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d
```

API Collection
-------------------

Here is the complete list of URL: http://127.0.0.1:8000/api/

### GET Employee Data

- URL: http://127.0.0.1:8000/api/employee/

- Method: `GET`

#### Example Response

```
[
    {
        "id": 1,
        "full_name": "Tiger Nixon",
        "job_title": "Chartered Accountant",
        "employment_status": "Active",
        "sub_unit": "Accounting"
    },
    {
        "id": 2,
        "full_name": "Jon Doe",
        "job_title": "Sales Executive",
        "employment_status": "Internship",
        "sub_unit": "Sales"
    },
]
```
---

### GET Product Data

- URL: http://127.0.0.1:8000/api/data/products/

- Method: `GET`


#### Example Response

```
[
    {
        "id": 1,
        "sku": "SKUPDT1",
        "name": " Product 1"
    },
    {
        "id": 2,
        "sku": "SKUPDT2",
        "name": " Product 2"
    },
    {
        "id": 3,
        "sku": "SKUPDT3",
        "name": " Product 3"
    },
]
```
---

### POST Order Report

- URL: http://127.0.0.1:8000/api/data/order-report/

- Method: `POST`

- Headers: Content-Type: application/json

- Body: JSON with sample data for the order report

#### Example Request :

```
{
    "skus": ["SKUPDT1", "SKUPDT2"],
    "date_range": {
        "start": "2023-12-14",
        "end": "2023-12-18"
    }
}
```

#### Example Response :

```

[
    {
        "date": "2023-12-16",
        "data": [
            {
                "product": "SKUPDT1",
                "sold_quantity": 1
            },
            {
                "product": "SKUPDT2",
                "sold_quantity": 2
            }
        ]
    },
    {
        "date": "Total",
        "data": [
            {
                "product": "SKUPDT1",
                "sold_quantity": 1
            },
            {
                "product": "SKUPDT2",
                "sold_quantity": 2
            }
        ]
    }
]
```

---