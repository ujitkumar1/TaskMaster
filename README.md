## TaskMaster: Simple & Efficient Task Management with Restful API Integration

### Description:

TaskMaster is a task management application that aims to provide a simple and efficient way to organize and manage
tasks. It is designed to help individuals and teams to keep track of their daily tasks, prioritize their workload and
increase their productivity. TaskMaster is a streamlined task management solution that is exclusively focused on
delivering a restful API for managing tasks. It provides users with the ability to create, read, update, and delete
tasks, all through a flexible and easy-to-integrate API.

### Prerequisites:

1. Python Programming language
2. MySql
3. flask
4. flask_restful
5. json

### Installation:

To install the required packages and libraries, run the following command in your current working directory:

command

```
pip install -r requirements.txt
```

This command will install all the necessary dependencies listed in the requirements.txt file, allowing you to run the
project without any issues.

### Usage:

To run the application, execute the following command in the src directory

Command

```
python main.py
```

This will start the application, and you should be able to use it. (or) Directly run the main.py file

Endpoint Working:

CRUD Operations on TODO Items

1. To Create a todo item

   url : http://127.0.0.1:5000/create (POST Request)

   Input --> json_data = {"todo_item" : "Bring Vegetables from market"}

   Output --> "TODO Item Saved:Bring Vegetables from market with todo_id: 1"


2. To View a todo item

   url : http://127.0.0.1:5000/todo/1 (GET Request)

   Output --> "The todo with id: 1, is 'Bring Vegetables from market' and it's incomplete"


3. To Delete a todo item

   url : http://127.0.0.1:5000/todo/1 (DELETE Request)

   Output --> "The todo with id: 2, is 'Bring Vegetables from market' is deleted successfully"


4. To Update a todo item

   url : http://127.0.0.1:5000/todo/1 (PUT Request)

   Input --> json_data = {"todo_item" : "Bring Potatoes from market"}

   Output --> "The todo with id: 1, is updated to 'Bring Potatoes from market'"


5. To Update the Status of Todo Item:

   url : http://127.0.0.1:5000/todo/status/1 (PUT Request)

   Input --> json_data = {"todo_status":true }

   Output --> "The todo with id: 1, status updated to'True'"

### Contact:

Name : Ujit Kumar

Email : ujitkumar1@gmail.com