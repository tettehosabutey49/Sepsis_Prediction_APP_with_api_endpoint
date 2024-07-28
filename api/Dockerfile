FROM python:3.10.10 AS api

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --timeout 30000 -r/tmp/requirements.txt
RUN pip install --no-cache-dir -r/tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 80

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]
