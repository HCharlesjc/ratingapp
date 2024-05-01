FROM python:3.12

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

ADD . /code

# Copy the current directory contents into the container at /app/
COPY ./requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/


# Copy manage.py into the container
COPY manage.py /code/

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
