FROM python:3.11-alpine

# Environment variables
ENV POETRY_VERSION=1.4.0

# System deps:
RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

# Copy only requirements to cache them in docker layer
COPY poetry.lock pyproject.toml ./

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Copy project
COPY . .

# Run
CMD ["python", "main.py"]