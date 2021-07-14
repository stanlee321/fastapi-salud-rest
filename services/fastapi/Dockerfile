#FROM jameswilliams1/python-webdriver:3.8-slim-buster-chrome
FROM python:3.7-slim-buster
WORKDIR /code
RUN apt-get update && apt-get install -y \
curl
COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -U -r /tmp/requirements.txt

COPY . .

RUN chmod +x /code/setup.sh

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]