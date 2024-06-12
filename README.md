# Online Shopping
The goal of this project is to build an web application using Django for handling a online shopping. Users will be able to browse the shopping’s menu, add items to their cart, and submit their orders, add and update products.

On this web app, users can :
- Register, login, browse the menu and items to their cart.

After submission, the items will be remove from the current cart and the site administrator can:
- See a new order on the admin interface that he/she can mark as completed.
- Add or update category and name of product if needed.

## Achievements

* Menu: I created 6 options : cart, products, home, login, register, profile
  
* Adding Items: Using Django Admin, site administrators are able to add, update, and remove items on the product. 
* Registration, Login, Logout: Site users (customers) are able to register for the web application with a name, password, and email address. Customers can then log in and log out of the website.
* Shopping Cart: Once logged in, users see and add items to their virtual “shopping cart.” The contents of the shopping is saved even if a user closes the window, or logs out and logs back in again.

## How to run this application

 Python
- Run `pip install -r requirements.txt` to install Django
- pip install asgiref==3.8.1
- pip install Django==5.0.6
- pip install django-crispy-forms==2.1
- pip install pillow==10.3.0
- pip install sqlparse==0.5.0
- pip install tzdata==2024.1
