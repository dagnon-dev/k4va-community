FROM python:3.12-slim

WORKDIR /workspace
COPY pyproject.toml README.md ./
COPY k4va ./k4va
RUN pip install --no-cache-dir .

ENTRYPOINT ["k4va"]
