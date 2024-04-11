ARG PYTHON_VERSION
FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}

# Switch to non-root user
ARG REMOTE_USER
USER ${REMOTE_USER}

# Set the working directory
WORKDIR /workspaces/recommendation-systems-a-practical-introduction-2703578

# Install required packages
RUN pip install -U pip setuptools wheel && \
    pip install numpy 'Cython<4' 'scipy<1.11.0' && \
    pip install -r requirements.txt

# Install Jupyter Notebook and create a virtual environment kernel
RUN pip install jupyter ipykernel && \
    python -m ipykernel install --user --name=reco

# Expose the Jupyter port
EXPOSE 8888

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser"]

