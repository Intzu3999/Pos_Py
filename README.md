# ASSESSMENT ANSWER | POS MALAYSIA | Take Home API Testing And Test Automation


### QUESTION 1 ANSWER
1) API to get list of countries: https://www-api.pos.com.my/api/countries [GET request]
2) API to get state by Postcode Number: https://www-api.pos.com.my/api/getStateByPostcode [POST request]
3) API to calculate price: https://www-api.pos.com.my/api/price [POST request]
4) Postman API Collection: https://universal-astronaut-374685.postman.co/workspace/POS-Malaysia~aa424b49-188d-484d-b6e7-f68f559c1714/collection/22868763-9000b678-3623-4da2-be66-4e9a95eab93a?action=share&creator=22868763&active-environment=22868763-23042983-b067-43d6-ae00-f48e8f02346d 
5) Postman Environment: https://universal-astronaut-374685.postman.co/workspace/POS-Malaysia~aa424b49-188d-484d-b6e7-f68f559c1714/environment/22868763-23042983-b067-43d6-ae00-f48e8f02346d?action=share&creator=22868763&active-environment=22868763-23042983-b067-43d6-ae00-f48e8f02346d POS_BASE_URL = https://www-api.pos.com.my/api


### QUESTION 2 ANSWER

### TO SETUP
1) Install python3.exe x64-bit.
Verify success installation of Python (v3 in our case): python --version or python3 --version
![Python install](src/image.png)
2) At root project create new virtual env, naming our virtual env as venv: python -m venv venv
![Python install](src/image-1.png)
3) Start Python's virtual env: venv\Scripts\activate 
![Python install](src/image-2.png)
4) python.exe -m pip install --upgrade pip
5) pip install -r requirements.txt
![Python install](src/image-3.png)
6) playwright install
![Python install](src/image-4.png)
7) At root project, create .env file:
8) to end venv environment: deactivate
9) to run playwright/test, refer instructions below.

### TO RUN TEST
1) python tests/e2e/test_rate_calculator.py
2) python tests/e2e/test_example_page.py

### PLAYWRIGHT CODEGEN
playwright codegen https://url/here


### FOLDER ARCHITECTURE EXPLANATION: MVC
| MVC Role	| Purpose in MVC | Equivalent in this test | Explanation
|----------|----------|----------|----------|
Model (M) | Business logic, data handling | api/ folder (API calls, DB utils) | These handle data, such as fetching or validating from APIs, similar to the Model layer in MVC.
View (V) | UI components, rendering output | pages/ folder (Playwright functions sorted by pages and elements/components) | These represent the UI elements — input fields, buttons, dropdowns — and interact with them.
Controller (C) | Manages flow between M and V | scripts/ folder (test execution flow) | This orchestrates everything — when to click, when to fetch data, how to assert — like a controller.
