FROM ubuntu

# Create app directory
WORKDIR /usr/src/app
COPY build ./

RUN apt-get update
RUN apt-get install -y inotify-tools
RUN apt-get install -y vim
RUN apt-get install -y net-tools
RUN apt-get install -y openssh-server
RUN apt-get install -y python
RUN mkdir -p /usr/src/app/src
RUN mkdir -p /usr/src/app/result
RUN chmod 777 ./run.sh

EXPOSE 5000
