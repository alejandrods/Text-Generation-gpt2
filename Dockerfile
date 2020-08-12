# Dockerfile
FROM python:3.6-slim-buster

WORKDIR /usr/app

EXPOSE 8080

ADD ./src/requirements.txt ./
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
ADD ./src ./
RUN python download.py
#ADD ./src/gpt2 ./gpt2

CMD ["python", "-u", "app.py"]

#docker tag text-generator-gpt2:latest eu.gcr.io/text-generator-gpt-2/text-generator-gpt2:latest
#docker push eu.gcr.io/text-generator-gpt-2/text-generator-gpt2:latest