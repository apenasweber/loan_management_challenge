# Use an official Python runtime as the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /code

# Copy the project files to the working directory
COPY . /code/

# Install the dependencies
RUN pip install -r requirements.txt

# Change the directory to the inner loan_management directory
WORKDIR /code/loan_management

# Run the migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Create the superuser
RUN python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')"

# Change the working directory back to the root of the project
WORKDIR /code/loan_management

# Expose the application port
EXPOSE 8000

# Start the Django development server
CMD ["python", "loan_management/loan_management/manage.py", "runserver", "0.0.0.0:8000"]
