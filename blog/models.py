"""
These are models (tables) for the mysqlite database.
Since we are building a blog, the tables must hold data related to the blog.
If you want to know how Django processes this information, you can read the docs.
(https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types)

You can add a new model to the database in the console window with the command:
python manage.py makemigrations blog
python manage.py migrate blog

The good news is that Django handles most of the database stuff in the background.
We only need to define fields and actions here in the models.py module.
"""

# add some bits from other files
from django.db import models
from django.conf import settings
from django.utils import timezone


# models.Model makes this object a Model/Table object in the msqlite database
# Think of this as a spreadsheet table. You can create many posts (each row is a post).
class Post(models.Model):
    """
    The following properties are fields in the Post model.
    This class will be called whenever a Post is created.
    """
    # ForeignKey links to another model (which is a table in the database)
    # In other words, ForeignKey links tables together.
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField defines the field (column) type as text WITH a limited number of characters
    title = models.CharField(max_length=200)
    # TextField defines the field (column) type as text WITHOUT a limited number of characters
    text = models.TextField()
    # DateTimeField defines the field (column) type as a date and time
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    """
    The following methods are actions a Post can make.
    The name doesn't matter. What matters is what what's inside! <3
    """
    def publish(self):
        """
        Publishes the post.
        You can call publish(...)
        """
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """
        Returns a text (string) with a Post title.
        """
        return self.title
