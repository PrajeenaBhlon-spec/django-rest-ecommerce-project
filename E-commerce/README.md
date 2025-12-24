# Simple E-commerce Project 

This project is a simple E-commerce web application built to practice and strengthen my understanding of Django, especially concepts like APIView, JWT , Django REST Framework, serializers, and models. The project focuses more on backend logic and authentication rather than UI perfection.

## Authentication and user flow

The project uses JWT authentication to securely manage user sessions. After a successful login, users are authenticated using access and refresh tokens, which helps maintain secure communication between the client and the backend API.

When the application starts, users are shown a login page with three options: logging in as an admin, registering if they do not already have an account, or logging in if an account already exists.

During registration, users must provide their name, email, password, and confirm password. An OTP is sent to the user’s email for verification. Only after entering the correct OTP does the user become a verified customer.

For login, users enter their email and password. Upon successful authentication, JWT tokens are generated and used for protected API access. If a user forgets their password, they can use the “Forgot password?” option, which requires OTP verification before the password is updated.

## Customer Features

Once logged in, a customer is redirected to a page where they can choose the “View Products” option. From there, they can see a list of available products along with their prices.

## Admin Features

When an admin logs in, they are redirected to a different page that allows them to add new products to the system. At the moment, the feature to edit existing products has not yet been implemented, as this project is still under development.