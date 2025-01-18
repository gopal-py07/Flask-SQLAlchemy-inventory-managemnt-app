from app import crete_app # import crete_app method from app moudle as it is __init__.py file

app = crete_app() # call method

if __name__ == '__main__':
    app.run()

""" next Run these commands to initialize and prepare the database:
bash
Copy code
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
"""

"""python wsi.py
"""

