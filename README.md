# PLACE MANAGEMENT - IT4062 Project

## How to run with .vdi file:
- Open XAMPP by running: ```sudo /opt/lampp/lampp start```
- Open terminal and move to project folder, then run the server:

    ```cd Desktop/place_management``` 

    ```python3 server/server.py```

- Open another terminal and move to project folder, then run the client:

    ```cd Desktop/place_management``` 

    ```python3 client/client.py```

## How to run from scratch
### Prequisities
- Install Python > 3.9
- Install [XAMPP](https://www.apachefriends.org/)
- This is the instruction for running in Linux. For Windows, using `python` instead of `python3` in every command.
### Running steps
- Clone project from Github:

    `git clone https://github.com/LTM-HUST/place-management.git`

- Move to the project:

    `cd place-management`

- Install required Python libraries:

    `pip install -r requirements.txt`

- Open XAMPP (like above) and create database named **place_management**. After that, you can import database in *Import* tab using **place_management_db.sql** or implement empty database by running `python3 server/create_db.py`

- Run the server:

    `python3 server/server.py`

- Open another terminal, move to the project folder and run the client:

    `python3 client/client.py`