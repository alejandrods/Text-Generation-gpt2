# Dockerfile
FROM python:3.6-slim-stretch

WORKDIR /usr/app

EXPOSE 8080

COPY /src/requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN pip install torch==1.6.0+cpu torchvision==0.7.0+cpu -f https://download.pytorch.org/whl/torch_stable.html && rm -rf /var/lib/apt/lists/*
ADD ./src ./

CMD ["python", "-u", "app.py"]

# docker tag text-generator-gpt2:latest eu.gcr.io/text-generator-gpt-2/text-generator-gpt2:latest
# docker push eu.gcr.io/text-generator-gpt-2/text-generator-gpt2:latest