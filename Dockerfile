# Dockerfile
FROM python:3.6

WORKDIR /usr/app

EXPOSE 8080

ADD ./src/requirements.txt ./
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install -r requirements.txt
ADD ./src ./
ADD ./src/gpt2 ./gpt2

CMD ["python", "-u", "app.py"]

#docker tag travel_entity_recognition_gcp_deploy_app:latest eu.gcr.io/travel-entity-recognition/travel_entity_recognition_deploy_app:latest
#docker push eu.gcr.io/travel-entity-recognition/travel_entity_recognition_deploy_app:latest