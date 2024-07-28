FROM python:3.10.10 AS client

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install --timeout 30000 -r/tmp/requirements.txt
RUN pip install --no-cache-dir -r/tmp/requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 3000

CMD ["streamlit", "run", "mains.py", "--server.port=8501"]
