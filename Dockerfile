FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /my_atm_project
COPY requirements.txt /my_atm_project
RUN pip install -r requirements.txt
COPY . /my_atm_project/
