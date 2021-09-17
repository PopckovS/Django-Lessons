FROM python:3

WORKDIR /usr/src/app

#COPY requirements/base.txt .
#COPY requirements/local.txt .

#RUN pip3 install -r requirements/base.txt
#RUN pip3 install -r requirements/local.txt

COPY base.txt .
COPY local.txt .
COPY entrypoint.sh .

RUN pip3 install -r base.txt
RUN pip3 install -r local.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
