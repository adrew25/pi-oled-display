FROM python:3.11

WORKDIR /app

# Install iproute2 (needed for 'ip' command)
RUN apt-get update && apt-get install -y iproute2

COPY display.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "display.py"]

