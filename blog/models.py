"""
Create models to deal with data for the blog application.

If you want to know how Django processes this information, you can read the docs.
(https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types)

To add a new model to the database, enter this command in the console:
python manage.py makemigrations blog
python manage.py migrate blog
"""

# add some bits from other files
from django.db import models
from django.conf import settings
from django.utils import timezone


# models.Model makes this object a Django Model so Django knows 
# it should be saved in the database.
class Post(models.Model):
    """
    The properties herein are fields in a Post for related data.
    Call this class whenever a Post is created, read, updated, or deleted.
    """
    # ForeignKey links tables together.
    # In this case, link Post.author with the AUTH_USER_MODEL
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField defines a field for text WITH a limited number of characters.
    title = models.CharField(max_length=200)
    # TextField defines a field for text WITHOUT a limited number of characters.
    # Sounds ideal for blog content, right?
    text = models.TextField()
    # DateTimeField defines a field for a date and time.
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    """
    The following methods are actions a Post can make.
    The name doesn't matter. What matters is what what's inside... <3
    """
    def publish(self):
        """
        Set the date of publication.
        Publish the post.
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Returns the Post title when a Post is called.
        """
        return self.title