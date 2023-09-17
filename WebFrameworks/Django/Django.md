# Commands
```
> python -m venv venv
> .\venv\Scripts\activate
```
```
(venv) > py -m pip install Django
(venv) > py -m django --version
(venv) > django-admin startproject mysite
(venv) \(outer_django_dir)> py manage.py runserver {0.0.0.0:}{8080} # IP and Port are optional
(venv) \(outer_django_dir)> py manage.py startapp polls # create a poll app
```
```
(venv) \(outer_django_dir)> py .\manage.py makemigrations polls # Create a migration file for the models. Make sure the migrations are ok
(venv) \(outer_django_dir)> py manage.py sqlmigrate polls 0001 # sqlmigrate command takes migration names and returns their SQL
(venv) \(outer_django_dir)> py manage.py migrate # Creates tables in the database according to models
```
```
(venv) \(outer_django_dir)> py manage.py shell
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```
```
(venv) \(outer_django_dir)> py manage.py createsuperuser
Username: admin
Email address: admin@example.com
Password: **********
Password (again): *********
Superuser created successfully.
```
```
(venv) > python -m pip install --upgrade pip
(venv) > pip freeze > requirements.txt
(venv) > pip install -r requirements.txt
```
{} -> Optional arguments

# Django
### File Directory
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
- The <b>mysite/</b> root directory is a container for your project. Its name doesn't matter to Django; its name can be renamed.
- <b>manage.py:</b> A command line utility that lets you interact wit this Django project in various ways. [Link](https://docs.djangoproject.com/en/4.2/ref/django-admin/)
- The inner <b>mysite/</b> directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
- <b>mysite/\_\_init\_\_.py:</b> An empty file that tells Python that this directory should be considered a Python package.
- <b>mysite/settings.py:</b> Settings/configuration for this Django project. [Link](https://docs.djangoproject.com/en/4.2/topics/settings/)
- <b>mysite/urls.py:</b> The URL declarations for this Django project; a “table of contents” of your Django-powered site. [Link](https://docs.djangoproject.com/en/4.2/topics/http/urls/)
- <b>mysite/asgi.py:</b> An entry-point for ASGI-compatible web servers to serve your project. [Link](https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/)
- <b>mysite/wsgi.py:</b> An entry-point for WSGI-compatible web servers to serve your project. [Link](https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/)

### File directory of an app
```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### Notes
- Each application you write in Django consists of a Python package that follows a certain convention. Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.
- Projects vs Apps
  - An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
- Django follows the DRY Principle.
- Django apps are “pluggable”: You can use an app in multiple projects, and you can distribute apps, because they don’t have to be tied to a given Django installation.