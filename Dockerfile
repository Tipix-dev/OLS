FROM ubuntu:20.04

COPY . /app
WORKDIR /app

RUN apt install wget tar make
RUN curl -sSL https://raw.githubusercontent.com/artemkolba321-spec/OLS/main/install.sh | bash

CMD [ "bash", "-l" ]
