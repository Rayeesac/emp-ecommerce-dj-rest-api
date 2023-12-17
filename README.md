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

---

### GET Product Data

- URL: http://127.0.0.1:8000/api/data/products/

- Method: `GET`

---

### POST Order Report

- URL: http://127.0.0.1:8000/api/data/order-report/

- Method: `POST`

- Headers: Content-Type: application/json

- Body: JSON with sample data for the order report

### Example Body :

```
{
"skus": ["SKUPDT1", "SKUPDT2"],
"date_range": {
    "start": "2023-12-14",
    "end": "2023-12-18"
    }
}
```

---