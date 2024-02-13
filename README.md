# Crow Project

**Demo**

Live demo - https://crow-project-app.herokuapp.com/

**About:**

Web appliction that provide:
- User registration and login.
- User password reset.
- Private task manager for each user.
- Products CRUD app, include private / shared product.

**Technolegis:**

Python 3.10, Flask, SQLalchemy (ORM), SQLite and Bootstrap.


**Instalation:**

1. Clone or download the project.

2. Install the requirements packages:

```
pip install requirements.txt
```

3. Run *app.py*
```
python app.py
```

4. At your browser go to - http://10.0.0.2:5000/



**Project Structure:**

```
├───app.py # Main app.py file to be called to start server for web app.
├───requirements.txt # File of pip install statements for your app.
├───migrations # folder created for migrations by calling.
├───venv # Venv files.
├───Dockerfile # Docker setup file 
│
├───Crow_app # Vain project folder 
│   │   data.sqlite
│   │   models.py
│   │   __init__.py
│   │
|   |
|   |───templates # Html files folder.
|   |
|   |
│   ├───static # CSS, JS, Images...
|   |
|   |
│   ├───users
│   │   │   forms.py
│   │   │   views.py
│   │   
│   │   
│   │───tasks     
│   │   │   forms.py         
│   │   │   views.py   
│   │
│   │
│   ├───products
│   │   │   forms.py
│   │   │   views.py
│   │  
│   │   
│   │  



```