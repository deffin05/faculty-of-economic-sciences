# Faculty of economic sciences

## How to run project

1. Create and activate virtual environment
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Apply migrations
```bash
python manage.py migrate
```
4. Create superuser
```bash
python manage.py createsuperuser
```
5. Run the server
```bash
python manage.py runserver
```
6. Add homepage info in the admin panel