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
   ```bash
   git clone https://github.com/<your-username>/django-rest-assessment.git
   cd django-rest-assessment
