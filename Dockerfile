FROM python:3.12-bullseye
WORKDIR /app
COPY . /app/
RUN pip install --no-cache-dir flask pymysql cryptography
EXPOSE 5002
CMD ["python", "app.py"]
