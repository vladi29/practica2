FROM python

COPY . usr/src/app

WORKDIR /usr/src/app

RUN pip install -r requirements.txt

CMD [ "python", "./P3.py" ]