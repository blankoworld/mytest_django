# mytest_django
A case where I encount problem with django tests

# Initialize the project

  * create a new user, a new database in your postgreSQL database
  * adapt the mytest/settings.py
  * migrate database with `python manage.py migrate`

# The problem

When you make this command:

    python manage.py test

The system have all Actors in DB for the first test.

But NOT for the second test of the same class.

# Expected

All test can access to data from the initial DB.

# Migrations ?

As we can see here: https://docs.djangoproject.com/en/1.8/topics/testing/overview/#rollback-emulation

we should make serialized_rollback = True in test. But it make an error: https://dpaste.de/3xqq

So I found (thanks to moldy) this: https://code.djangoproject.com/ticket/23727 which explain the problem.
