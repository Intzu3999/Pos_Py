# 🐍 PYTHON PLAYWRIGHT 🎭
Pos_Py - POS MALAYSIA
Take Home API Testing And Test Automation


## WHAT DOES THIS PROJECT DO
1) 

## PYTHON BEST PRACTICE
Python's Naming Convention (PEP 8) are summarized below:

| Element	| Convention | Example |
|----------|----------|----------|
Script/Module names | snake_case | customer_api.py
Functions | snake_case | get_customer_data()
Variables | snake_case | customer_id
Classes | PascalCase | CustomerAPI
Constants | SCREAMING_SNAKE_CASE | MAX_RETRIES
Methods | snake_case | calculate_total()
Private variables | _snake_case	| _internal_data
Name-mangled variables | __snake_case | __private_data
Packages | lowercase | mypackage
Type variables | PascalCase	| T, ResponseType

- PEP 8 Official Guide https://peps.python.org/pep-0008/
- Python Documentation https://docs.python.org/3/tutorial/classes.html#private-variables 
- Playwright Documentation https://playwright.dev/python/docs/api/class-playwright


## TO SETUP
1) Install python3.exe x64-bit.
Verify success installation of Python (v3 in our case): python --version or python3 --version
![alt text](image.png)
2) At root project create new virtual env, naming our virtual env as venv: python -m venv venv
![alt text](image-1.png)
3) Start Python's virtual env: venv\Scripts\activate 
![alt text](image-2.png)
4) python.exe -m pip install --upgrade pip
5) pip install -r requirements.txt
![alt text](image-3.png)
6) playwright install -will include this in a shell script soon
![alt text](image-4.png)
6) to end venv environment: deactivate
7) to run playwright/test, refer instructions below.


## TO RUN TEST
1) python tests/e2e/.py
2) python tests/regression/example_module.py

