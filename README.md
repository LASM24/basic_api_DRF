# Basic DRF API Example
## Introduction
This is an example of a CRUD API created with Django REST Framework (DRF). It serves as a practice project to explore fundamental concepts of DRF and to delve into the configuration and deployment of APIs using Render.

<br>

## Description
The API provides endpoints to manage projects. Each project consists of a title, description, technology, and creation timestamp. It offers basic CRUD (Create, Read, Update, Delete) operations for projects.

<br>

## How to Use
### Clone the Repository
To use this API, you can clone the repository to your local machine using the following command:

```bash
git clone https://github.com/LASM24/basic_api_DRF.git
```

<br>


### Build and Run
After cloning the repository, navigate into the project directory and execute the `build.sh` script to set up the environment and migrate the database:

```bash
cd basic_api_DRF
./build.sh
```

This script installs the required dependencies, collects static files, and performs database migrations.

<br>

### Accessing the API
Once the build process is complete, you can access the API by running the Django development server. By default, the API will be available at `http://localhost:8000/api/projects/`.

<br>

## Live API
You can access the live version of this API deployed on Render at [Basic DRF API](https://basic-api-drf.onrender.com).

<br>

## About the Author
This project was created by [LASM24](https://github.com/LASM24). Feel free to check out their GitHub profile for more projects and contributions.

