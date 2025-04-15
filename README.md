# Django REST Assessment - Abhay Pratap Singh

This project is the solution for the **Artizence Python Django REST API Developer Assessment**. It includes a CRUD API, query optimization, and a take-home mini project for **Order Management**.

## Sections

 Section 1: Theoretical Questions

Answers to theoretical questions are placed in the `Section_1_Answers/` folder.

 Section 2: Coding Tasks

 Task 1: CRUD API (Book Model)

The library app contains the implementation of the **CRUD API** for the **Book** model. The model includes:
- Fields: `id`, `title`, `author`, `published_date`, `isbn`, `price`
- Features:
  - Full CRUD functionality (Create, Retrieve, Update, Delete)
  - Filtering by `author` and `published_date`
  - Pagination using DRF's `PageNumberPagination`
  - Implemented with class-based views (`ModelViewSet`)

 Task 2: Query Optimization

- The **query optimization** task is implemented in the `library` app, where **N+1 query problems** are avoided using **`select_related`** to fetch books along with their author's name.

 Section 3: Take-Home Mini Project - Order Management API

The **`orders`** app contains the **Order Management API**, which includes:
- Models:
  - **Customer**: `name`, `email`
  - **Product**: `name`, `price`
  - **Order**: `customer`, `products (many-to-many)`, `total_amount (calculated)`, `created_at`
- Features:
  - Create and retrieve **customers** and **products**
  - Create **orders** with calculated total amount
  - Retrieve **orders** with customer and product details
  - **JWT Authentication** (SimpleJWT) for securing API endpoints
  - **Custom permission** ensuring only authenticated users can create orders
  - **Swagger documentation** generated using `drf-yasg`

#### Additional Features:
- **Rate limiting**: 10 requests per minute per user using DRF throttling.
  
## Setup Instructions

1. **Clone the repository**:
   
   git clone https://github.com/<your-username>/django-rest-assessment.git
   cd django-rest-assessment
   Set up the virtual environment:


python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Apply migrations:


python manage.py migrate
Run the development server:


python manage.py runserver
Access the Swagger UI: Visit http://127.0.0.1:8000/swagger/ to view and test the API documentation.

API Documentation
Swagger UI is available at /swagger/.

You can test all API endpoints directly from the Swagger interface.

Technologies Used
Django 3.x

Django REST Framework

SimpleJWT for JWT Authentication

DRF-YASG for Swagger API documentation

SQLITE (or SQLite depending on your setup)

Conclusion
This project demonstrates the use of Django REST Framework to implement a CRUD API, rate limiting, JWT authentication, and API documentation. It also optimizes database queries to avoid common performance issues such as N+1 queries.

Feel free to reach out for any questions!

Best regards,
Abhay Pratap Singh
