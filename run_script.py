import os


# Automate makemigrations, migrate, and runserver
def run_django_commands():
    print("Running makemigrations...")
    os.system("python manage.py makemigrations")

    print("Running migrate...")
    os.system("python manage.py migrate")

    print("Starting server...")
    os.system("python manage.py runserver")


if __name__ == "__main__":
    run_django_commands()
