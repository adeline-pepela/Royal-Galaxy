# Royal Galaxy

## Description
This is a web application that allows a user to search for a vegetarian recipe with the main ingredient of the dish.

## Author
Adeline Makokha</br>
[Github Account](https://github.com/adeline-pepela)


## User Story
1. User should be able to sign up and login.
2. User can submit a recipe details via form.
3. User can view recipe status.
4. 


## Behaviour Driven Development (BDD)
1. Sign up to the application

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on sign up  | username,password,email | user account is created  | 

2. log into the application 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter details in the log in form   | username, password| Landing page is loaded   | 


3. Add recipe

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on button recipe on the home page | Enter required details| Recipe is submitted  | 


4. Update Profile

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on update button   | Update profile | Submit the profile  |


## Setup/Installation Requirements
1. Create a folder and cd to it.
2. Clone the repository below with the command `git clone <https option url> .`  <br>
    https://github.com/adeline-pepela/Royal-Galaxy  
3. Install dependencies in the requirements.txt file `pip install -r requirements.txt` .
4.  Type code . or atom . based on the text editor you have and work on it.   

## Database
1. Set up Database(postgresql),and put your username and password in the code
2. Make migrations
    python3 manage.py makemigrations
3. Migrate
   python3 manage.py migrate 
       
## Running the Application
1. Run main aplication locally on http://127.0.0.1:8000/ local host<br>    
   * python3.9 manage.py runserver<br>
    Note: python version will vary in future

## Creating Admins
1. Creating Admin Locally<br>
     python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.9.2 - as backend language
* Django4.0.5 - as a Framework
* Bootstrap4 - for responsiveness & styling 
* PostgreSQL - as database
* Heroku - for deploying app

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<adelinemakokha@gmail.com>

## License
[MIT License](https://github.com/adeline-pepela/Royal-Galaxy/blob/master/LICENSE)<br>
Copyright (c) 2022 **Adeline Makokha**