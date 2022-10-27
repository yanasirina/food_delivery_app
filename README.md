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
| Таблицы       | Это                | Круто |
| ------------- |:------------------:| -----:|
| столбец 3     | выровнен вправо    | $1600 |
| столбец 2     | выровнен по центру |   $12 |
| зебра-строки  | прикольные         |    $1 |
