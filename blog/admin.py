"""
Reads metadata from our models to provide a quick, model-centric interface
where trusted users can manage content on our site. Internal use only.

(https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)
"""

# add some bits from other files
from django.contrib import admin
from .models import Post # we created this one in blog.models.py

"""
Register our models with the admin site.
In this case, models register under the blog app.

To create a superuser enter this command:
python manage.py createsuperuser

Admin Page Login Info (ex. http://127.0.0.1:8000/admin/)
user : admin
pass : admin
"""
admin.site.register(Post)