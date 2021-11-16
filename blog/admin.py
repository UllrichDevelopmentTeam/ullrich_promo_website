"""
Reads metadata from our models to provide a quick, model-centric interface
where trusted users can manage content on our site. Internal use only.

(https://docs.djangoproject.com/en/2.2/ref/contrib/admin/)
"""

# add some bits from other files
from django.contrib import admin
from .models import Post # we created this one in blog.models.py

"""
Make our model visible on the admin page.
To create a superuser (a user account that has control over everything on the site)
Enter the following command:
python manage.py createsuperuser
"""
admin.site.register(Post)