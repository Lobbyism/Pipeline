FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org .
COPY vendor ./vendor
COPY main.py .
ENTRYPOINT ["python", "main.py"]