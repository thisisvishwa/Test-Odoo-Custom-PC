# System Architecture

## Overview

The system architecture of the Custom PC Building Module is designed to provide a comprehensive and user-friendly way for users to build custom PCs on an e-commerce website. The system is built on the Odoo V16 CE platform and uses Python for backend development and Odoo's UI framework for frontend development.

## Backend

The backend of the system is developed using Python. It handles various tasks such as component selection, configuration, customization, pricing, build history, build recommendations, build sharing, build import/export, build analytics, build support, visibility, comparison price, prevent sales of zero priced products, and new menu. The backend code can be found in the `controllers/main.py`, `models/component.py`, and `models/build.py` files.

## Frontend

The frontend of the system is developed using Odoo's UI framework. It includes various pages for users to interact with, such as component selection, configuration, customization, pricing, build history, build recommendations, build sharing, build import/export, build analytics, and build support. The frontend code can be found in the `views/` directory and the `static/src/` directory.

## Database

The system uses Odoo's ORM to define the database schema. The `Component` schema includes fields for name, category, configuration, customization, and price. The `Build` schema includes fields for user ID, components, configuration, customization, price, build history, build recommendations, build sharing, build import/export, build analytics, and build support. The database schema can be found in the `models/component.py` and `models/build.py` files.

## Security

The system implements secure component selection and configuration. It protects against common web vulnerabilities such as SQL injection and cross-site scripting and uses HTTPS for secure communication. The security implementation can be found in the `controllers/main.py` file and the `security/ir.model.access.csv` file.

## Testing

The system is thoroughly tested to ensure it functions as expected. Testing includes unit testing, integration testing, end-to-end testing, performance testing, and security testing. The system is also tested for compatibility across different browsers and devices. The test code can be found in the `tests/test_component.py` and `tests/test_build.py` files.

## Documentation

The system is well-documented, including API documentation, user documentation, system architecture documentation, and security documentation. The documentation can be found in the `doc/` directory.

## Access Rights

The system implements access rights, which are defined as records of the model `ir.model.access`. Each access right is associated with a model, a group (or no group for global access), and a set of permissions: read, write, create, unlink. The access rights can be found in the `security/ir.model.access.csv` file.