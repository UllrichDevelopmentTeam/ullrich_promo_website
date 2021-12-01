"""
Create models to deal with data for the blog application.

If you want to know how Django processes this information, you can read the docs.
(https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types)

To add a new model to the database, enter this command in the console:
python manage.py makemigrations blog
python manage.py migrate blog
"""

# add some bits from other files that may be useful
from django.db import models
from django.conf import settings
from django.utils import timezone
