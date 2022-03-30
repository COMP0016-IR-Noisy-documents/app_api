# By Thatchawin Leelawat
FROM python:3.9-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# CMD ["flask", "run", "--host=0.0.0.0"]

CMD gunicorn --bind 0.0.0.0:5000 api:app