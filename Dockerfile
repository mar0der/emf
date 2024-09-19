FROM python:3.9

# Install vim and other necessary packages
RUN apt-get update && apt-get install -y \
    vim \
    curl \
    libpq-dev \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

# Command to run the application
CMD ["python", "-m", "app"]
#CMD ["/bin/bash"]