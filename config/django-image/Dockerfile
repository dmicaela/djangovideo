FROM python:3.12-bookworm

RUN apt-get update && apt-get install python3-dev libgdal-dev graphviz graphviz-dev -y

WORKDIR /usr/src/app

RUN pip install --upgrade pip && pip install --upgrade setuptools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#el comando django-admin ya estaria instalado, le decimos que empiece
#el proyecto llamado app dentro de la carpeta donde estoy parada .
#RUN django-admin startproject app .

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
