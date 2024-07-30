---
title: "Getting Started with Flask: A Beginner's Web Development Framework"
date: 2024-07-25 20:27:12
keywords: "Flask, Web Development, Python, Python Framework, Flask Tutorial, Beginner Programming, Web App Development"
description: "Flask is a micro web framework for Python that is great for beginners and experienced developers alike. This article will guide you through the essential concepts and steps needed to set up and create a simple web application using Flask. You'll learn about Flask's installation, routing, templating, and how to handle requests and forms. By the end of this tutorial, you will have a solid understanding of Flask's key features and how to build a basic web app from scratch. Whether you're new to web development or looking to enhance your skills, this guide is designed to help you start your journey with Flask effectively."
categories:
  - python
  - web development
tags:
  - Flask
  - Python
  - Web Framework
  - Beginner Tutorial
---

### Introduction to Flask

Flask is a lightweight WSGI web application framework in Python. It is classified as a microframework because it does not require particular tools or libraries. Flask is known for its simplicity and flexibility, making it an excellent choice for beginners in web development. Whether you are building a simple blog, a REST API, or a full-fledged web application, Flask provides the core tools you need to get started. In this tutorial, we will delve into the essential features of Flask and walk through the process of creating your first web application.

<!-- more -->

### 1. Installing Flask

Before we start coding, we need to install Flask. Make sure you have Python installed on your machine. You can download it from the official Python website. Once Python is installed, you can install Flask using pip.

```bash
pip install Flask  # Installs Flask via pip
```

After the installation completes, you can verify the installation by running the following command:

```bash
pip show Flask  # Displays information about the Flask package
```

This command should give you details about the Flask version and location where it is installed.

### 2. Creating a Simple Flask Application

Now that we have Flask installed, let’s create our first application. Create a new directory for your project and navigate into it:

```bash
mkdir my_flask_app  # Creates a new directory for the Flask app
cd my_flask_app     # Navigates into the new directory
```

Next, create a new Python file named `app.py`:

```bash
touch app.py  # Creates a new Python file named app.py
```

Open `app.py` in your favorite text editor and write the following code:

```python
from flask import Flask  # Import the Flask class

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/')  # Define the route for the home page
def home():
    return "Hello, Flask!"  # Returns a simple string for the home page

if __name__ == '__main__':
    app.run(debug=True)  # Runs the application in debug mode
```

#### Explanation of the Code
- We import the `Flask` class from the `flask` module.
- An instance of the `Flask` class is created, which represents our web application.
- The `@app.route('/')` decorator tells Flask what URL should call the `home` function. In this case, it is the root URL.
- The `home` function returns a simple string that will be displayed in the browser.
- Finally, we run the application using `app.run()` with `debug=True`, enabling debug mode.

### 3. Running the Flask Application

To run your Flask application, execute the following command in your terminal:

```bash
python app.py  # Executes the Flask application
```

You should see output in your terminal indicating that the server is running, usually at `http://127.0.0.1:5000/`. Open this URL in your web browser, and you should see the message "Hello, Flask!" displayed on the page.

### 4. Understanding Routing in Flask

Routing is one of the key features in Flask. It allows you to bind URL paths to Python functions. You can define multiple routes in your application. For example, let’s add a new route that returns a welcome message:

```python
@app.route('/welcome')  # Define a new route for /welcome
def welcome():
    return "Welcome to my Flask app!"  # Returns a welcome message
```

Now, if you navigate to `http://127.0.0.1:5000/welcome`, it will display "Welcome to my Flask app!".

### 5. Flask Templates

Flask uses Jinja2 as its template engine. Templates allow you to create dynamic HTML pages. First, you should create a folder named `templates` in your project directory and create an HTML file named `index.html` inside it:

```bash
mkdir templates  # Creates a templates directory
touch templates/index.html  # Creates an index.html file
```

In `index.html`, add the following content:

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Flask App</title>
</head>
<body>
    <h1>{{ title }}</h1>  <!-- Use a template variable -->
    <p>Welcome to my Flask application!</p>
</body>
</html>
```

Now, modify your `app.py` to render this template:

```python
from flask import render_template  # Import the render_template function

@app.route('/')  # Default route
def home():
    return render_template('index.html', title='Hello, Flask!')  # Renders the index.html template
```

### 6. Handling Forms

Flask makes it easy to handle web forms. You can use the `request` object to access form data. First, let’s create a form in `index.html` that captures a user's name:

```html
<form action="/greet" method="POST">  <!-- Define form action and method -->
    <input type="text" name="username" placeholder="Enter your name" required />  <!-- Username input field -->
    <input type="submit" value="Greet Me!" />  <!-- Submit button -->
</form>
```

Next, we’ll create a new route in `app.py` to handle the form submission:

```python
from flask import request  # Import the request object

@app.route('/greet', methods=['POST'])  # Define route to handle POST requests
def greet():
    username = request.form['username']  # Access the submitted form data
    return f"Hello, {username}!"  # Returns a greeting
```

### Conclusion

In this article, we covered the basics of Flask, including installation, routing, templates, and handling forms. Flask’s simplicity and flexibility make it an ideal framework for beginners in web development. With just a few lines of code, you can create a functional web application that responds to user input. I encourage you to explore additional features of Flask, such as database integration, user authentication, and deployment options.

As the creator of this blog, I strongly recommend bookmarking our site, [GitCEO](https://gitceo.com). It contains extensive tutorials on cutting-edge computer technologies and programming techniques, making it an invaluable resource for your learning and development journey. Stay updated and enhance your skills by following along with our tutorials, ensuring you have everything you need to succeed in the tech world.