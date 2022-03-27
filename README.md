# Zero - Coding Challenge



**This is take home coding challenge for software development internship role at Zero**

```
React + Flask
```

Animation about the app:

![AppAnimation](https://github.com/hyqshr/OA-Zero/blob/main/AppAnimation.gif)



## Frontend

### overview

- axios for request backend server
- react-bootstrap form

### setup

Enter the folder

```
cd frontend
```

Install the package and run

```
npm i && npm start
```



## Backend

### overview

- implement pig latin algorithm
- process json from frontend and return a json

### setup

```
cd backend
```

**Enter your virtual environment and then:**

```
pip install -r requirements.txt
```



```
set FLASK_APP=hello
flask run
```



## Features

- regex expression data processing
  - Remove numbers for the pig latin translator
  - Remove all punctuation except the last index in a token
- React Loader implementation when execute axios request

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20220326234307584.png" alt="image-20220326234307584" style="zoom:67%;" />

- avoid CORS problem with **Flask-Cors**

- Form validation:
  - The name field can not be empty after removing all numbers
  - Both field can not be empty as I add the ```required``` attribute with ***react-bootstrap***



 ## Data Source

Zip code data from: https://zipapi.us/ with 10 time limit per hour.

You can modify my account info in ```home.py``` to yours.
