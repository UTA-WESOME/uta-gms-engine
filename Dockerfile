FROM python:3.10.8
WORKDIR /uta-gms

RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y build-essential

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./ ./

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
CMD ["bash"]