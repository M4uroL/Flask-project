# Flask Project

An initial Flask project for managing users, categories, and products, with authentication, administration via Flask-Admin, and MySQL integration.

This repository is under development and is organized as a starting point for learning and evolving a web application with a lightweight MVC architecture, SQLAlchemy models, and dedicated routes for authentication and product CRUD operations.

## Overview

The application is designed as a simple inventory management system, focused on:

- managing users and roles
- adding categories
- adding and updating products
- providing an administrative panel with Flask-Admin
- authentication and password recovery
- MySQL database integration using SQLAlchemy

## Technology Stack

- Python 3
- Flask
- Flask-SQLAlchemy
- Flask-Admin
- MySQL + mysqlclient
- passlib

## Project Structure

```text
.
├── admin/
│   ├── Admin.py          # Administrative panel configuration
│   └── Views.py          # Custom Flask-Admin views
├── controller/
│   ├── Product.py        # Product controller
│   ├── User.py           # User/authentication controller
│   └── Email.py          # Reserved for email sending
├── model/
│   ├── Category.py       # Category model
│   ├── Product.py        # Product model
│   ├── Role.py           # Role model
│   └── User.py           # User model
├── static/
│   └── css/              # Project stylesheets
├── templates/
│   └── ...               # Login, recovery, and administration templates
├── app.py                # Flask application setup and main routes
├── config.py             # Global project and environment configuration
├── run.py                # Application entry point
├── migrate.py            # Reserved for migrations/DDL
├── livro\_flask.sql       # Reserved for the SQL schema
├── json.json             # Example product data payload
├── README.md             # Project documentation
└── requirements.txt      # Not yet created (pending)
