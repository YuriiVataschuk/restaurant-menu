# Restaurant Management System

This is a Django-based restaurant management system that allows users to manage cooks, dishes, and dish types. It provides various views and functionalities for creating, updating, and deleting records, as well as searching and filtering data.

## Installation

1. Clone the repository: `git clone https://github.com/YuriiVataschuk/restaurant-menu.git`
2. Navigate to the project directory: `cd restaurant-management-system`
3. Install the required dependencies: `pip install -r requirements.txt`
4. Run database migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Start the development server: `python manage.py runserver`

## Usage

Once the development server is running, you can access the restaurant management system in your web browser at `http://localhost:8000`.

### Home Page

The home page provides an overview of the restaurant system, displaying the total number of cooks, dishes, and dish types.

### Cooks

- **Cook List**: View a paginated list of all cooks in the system. You can search for cooks by their usernames using the search form.
- **Cook Detail**: View detailed information about a specific cook, including their assigned dishes. You can navigate to a cook's detail page from the cook list.
- **Create Cook**: Create a new cook by providing the required information.
- **Update Cook**: Update the information of an existing cook.
- **Delete Cook**: Delete a cook from the system.

### Dishes

- **Dish List**: View a paginated list of all dishes in the system. You can search for dishes by their names using the search form.
- **Dish Detail**: View detailed information about a specific dish, including the cooks assigned to it. You can navigate to a dish's detail page from the dish list.
- **Create Dish**: Create a new dish by providing the required information.
- **Update Dish**: Update the information of an existing dish.
- **Delete Dish**: Delete a dish from the system.

### Dish Types

- **Dish Type List**: View a paginated list of all dish types in the system. You can search for dish types by their names using the search form.
- **Create Dish Type**: Create a new dish type by providing the required information.
- **Update Dish Type**: Update the information of an existing dish type.
- **Delete Dish Type**: Delete a dish type from the system.

### Assigning Cooks to Dishes

- **Toggle Assign**: Assign or unassign a cook to a dish. This functionality allows cooks to manage the dishes they are responsible for. The toggle button can be found on the dish detail page.


![image](https://github.com/YuriiVataschuk/restaurant-menu/assets/88705381/79d38e88-faca-4599-a148-51c0b8e1a58e)
![image](https://github.com/YuriiVataschuk/restaurant-menu/assets/88705381/b940c2e1-9e3e-4c40-a33a-41c64ddfd9b5)
![image](https://github.com/YuriiVataschuk/restaurant-menu/assets/88705381/0c0c2e26-307f-4cbe-96d7-46dfc4732313)
![image](https://github.com/YuriiVataschuk/restaurant-menu/assets/88705381/230cbc99-c343-4d59-9002-52db7f897753)



