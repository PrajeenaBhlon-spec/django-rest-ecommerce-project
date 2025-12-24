# Project Overview

This project was built to practice and strengthen my understanding of Django Rest Framework (DRF) concepts. While the core features are implemented, there is still more functionality planned for future improvements.

### How my project flows:

- When the application starts, the user is first presented with a login page that offers three options: login as admin, login, and register.

- If Login as Admin is selected, the admin must enter a valid email and password. After successful authentication, the admin is redirected to the admin dashboard, where they can add and manage products.

- If a normal user already has an account, they can log in using their credentials and will be redirected to the user page, where they can view available products.

- If the user does not have an account, they can choose the register option to create a new account before logging in.



### Key Features

- Authentication in this project is implemented using JWT (JSON Web Token), which provides a stateless and secure authentication mechanism suitable for APIs.

- To prevent unauthorized access through browser navigation (such as using the back button after logout), cache control is applied using @cache_control, ensuring that protected pages are not cached by the browser.