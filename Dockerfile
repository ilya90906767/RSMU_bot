FROM python:3.11

RUN apt-get update && apt-get install -y netcat-openbsd

RUN mkdir /rsmu_bot
WORKDIR /rsmu_bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 465
EXPOSE 587/tcp

RUN find /rsmu_bot/docker -type f -name "*.sh" -exec chmod a+x {} +
