FROM alpine:latest


RUN apk add --no-cache python3-dev
RUN apk add py3-pip --upgrade py3-pip


WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["run.py"]