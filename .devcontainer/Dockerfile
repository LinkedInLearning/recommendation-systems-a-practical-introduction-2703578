# Use the official Python 3.7 image from Docker Hub
FROM python:3.7

# Set the working directory in the container
WORKDIR /workspace

# Copy the requirements file into the container at /workspace
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -U pip setuptools wheel && \
    pip install numpy 'Cython<4' 'scipy<1.11.0' && \
    pip install -r requirements.txt

# Expose the port for Jupyter Notebook (optional)
EXPOSE 8888
