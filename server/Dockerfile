FROM ubuntu

# Create app directory
WORKDIR /usr/src/app
COPY build ./

RUN apt-get update
RUN apt-get install -y inotify-tools
RUN apt-get install -y gcc
RUN apt-get install -y net-tools
RUN apt-get install -y vim
RUN apt-get install -y openssh-server
#JRE8
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean
RUN mkdir -p /usr/src/app/src
RUN chmod 777 ./run.sh

#EXPOSE 5001
