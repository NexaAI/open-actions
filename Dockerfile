FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# make sure to use venv
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python3 -m pip install -r requirements.txt

# copy the content
COPY . /app

# Expose the application port
EXPOSE 8080

# For dev
CMD ["python", "main.py"]