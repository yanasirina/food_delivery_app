# Food delivery REST API
This app allows people to order groceries online

## Installation
Firstly, create virtual environment.
```
python3 -m venv venv
```
Then activate it.<br>
For Windows:
```
venv\Scripts\activate.bat
```
For Linux or MacOS:
```
source venv/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```

## Telegram bot
This project has it's own telegram bot to communicate with delivery men.<br>
It has 4 commands:
| name        | description                |
| ------------|:------------------:|
| /start      | Sends a welcome message to courier with ID<br>This ID should be sent to a manager |
| /start_day  | A command to start a working day<br>After pressing this button, courier will start<br>getting messages with new orders |
| /end_day    | A command to finish a working day<br>After pressing this button, courier will finish<br>getting messages with new orders |
| /end_order  | Pressing this button means that courier has<br>finished a delivery and he or she is ready<br> to get messages with new orders |

## Creating a telegram bot for the project
You can create a telegram bot using <a href='https://t.me/BotFather'>BotFather</a><br>
After creating it, BotFather should return you a token for your future tg bot

## Variable environment
Create .env file for variable environment in main directory<br>
Add in .env file next variables:
<li>SECRET_KEY - random secret key for your project (str)</li>
<li>DEBUG - 'True' if you want to use your project in Debug Mode, else 'False' (bool)</li>
<li>TOKEN - telegram bot token, that you got from BotFather (str)</li>
<li>ADMIN_ID - telegram chat id with admin, bot will send it to you after running it, for now you can put 12345 (int)</li>

## Migations
Don't forget to migrate the project
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

## Running the project
The last step: running it all

```
python3 manage.py runserver
```
```
python3 manage.py runbot
```

## REST API 
**Congrats!**<br>
Now you can use the project!
Here are commands for REST API:
#### For all users:
| name       |      type           | description |
| ------------- |:------------------:| -----:|
| /auth/login/ | POST | sends a token to an existing user |
| /auth/register/ | POST | signs up a new user and sends a token to them |
| /core/categories/ | GET | shows categories of items |
| /core/categories/{id}/ | GET | detail information about category |
| /core/categories/{id}/items/ | GET | shows items in a chosen category |
| /core/items/ | GET | shows all items (only items in stock) |
| /core/items/{id} | GET | detail information about item (only items in stock) |

#### For authenticated users:
| name       |      type           | description |
| ------------- |:------------------:| -----:|
| /auth/user/ | GET | shows detail information about user |
| /auth/user/ | PUT, PATCH | updates detail information about user |
| /orders/user_finished_orders/ | GET | shows all user's finished orders |
| /orders/user_finished_orders/{id} | GET | detail information about finished order |
| /orders/user_orders/ | GET | shows all user's not finished orders |
| /orders/user_orders/ | POST | creates a new order of user |
| /orders/user_orders/{id} | GET | detail information about not finished order |
| /orders/user_orders/{id} | PUT, PATCH | update detail information about not finished order |
| /orders/user_orders/{id} | DELETE | delete not completed order |
| /orders/user_orders/{id}/to_order/ | PATCH | marks order as completed,<br>sends an information about order to one of couriers |

#### For admin users:
| name       |      type           | description |
| ------------- |:------------------:| -----:|
| /auth/user_list/ | GET | shows all users |
| /core/admin_categories/ | POST | creates a new category |
| /core/admin_categories/{id} | PUT, PATCH | updates a category |
| /core/admin_categories/ | DELETE | deletes a category |
| /core/admin_items/ | GET | shows all items (including items out of stock) |
| /core/admin_items/ | POST | creates a new item |
| /core/admin_items/{id} | GET | detail information about item (including items out of stock) |
| /core/admin_items/ | PUT, PATCH | updates an item |
| /core/admin_items/ | DELETE | deletes an item |
| /core/admin_items/{id}/set_in_stock/ | PATCH | marks item as 'in stock' |
| /core/admin_items/{id}/unset_in_stock/ | PATCH | unmarks item as 'in stock' |
| /employees/couriers/ | GET | shows all delivery men |
| /employees/couriers/ | POST | registers a new delivery man |
| /employees/couriers/{id} | GET | detail information about a delivery man |
| /employees/couriers/{id} | PUT, PATCH | updates information about a delivery man |
| /employees/couriers/{id} | DELETE | deletes a delivery man |
| /orders/all_orders/ | GET | shows all orders |
| /orders/all_orders/{id} | GET | shows detail information about an order |




