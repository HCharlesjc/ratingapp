# Rating App: DevOps Project

# Overview
This project aims to develop a simple web application (Ratingapp) using Python and Django and deploy it on Tomcat running in Docker containers using Jenkins pipeline for automated building and deployment.

# Features
1. Homepage displaying the restaurants.
2. Additional page with functionality (e.g., a reviews page).

# Prerequisites
1. Python 3.12 and Django installed
2. Docker installed
3. Git installed
4. Jenkins installed and configured


# Steps to run Locally
1. Clone the Repository 
   - git clone https://github.com/HCharlesjc/ratingapp.

2. Navigate to project folder
   - cd ratingapp

3. Install Python dependencies
   - pip install -r requirements.txt
    
4. Run Django development server
   - python manage.py runserver

5. Access the Web Application:
   - Open your web browser and go to http://localhost:8000
    

# Jenkins Pipeline Configuration
The Jenkins pipeline automates the build and deployment process of the web application using Docker containers.

Pipeline Stages
- Checkout:Checks out the code from the Git repository.
- Build Docker Image: Builds the Docker image for the web application.
- Push Docker Image: Pushes the Docker image to a Docker registry.
- Deploy to Tomcat (Not done): Deploys the application on Tomcat running in Docker containers.


# Contributors
- Hakeem Charles
- hakeemc72@gmail.com