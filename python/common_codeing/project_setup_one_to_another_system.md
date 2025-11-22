### Project setup one pc to another Pc
* First of all we run the command
```python
pip freeze > requirements.txt
```
* And other system follows these step
```python
# Create and activate virtual environment
virtualenv -p python3 env
. ./env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
pip install --default-timeout=100 -r requirements.txt

# Create SQLite databse, run migrations
cd myapp
./manage.py migrate

# Run Django dev server
./manage.py runserver
```