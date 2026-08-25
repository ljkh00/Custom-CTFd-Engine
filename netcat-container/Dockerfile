FROM python:3.7-slim
RUN apt-get update
RUN apt-get install socat gcc sudo tar make -y 
RUN pip install pycrypto
RUN mkdir /challs
COPY challs/. /challs	
COPY setup.sh /setup.sh
RUN chmod +x /setup.sh
COPY Python-2.7.9.tgz /Python-2.7.9.tgz
RUN tar xzf Python-2.7.9.tgz
WORKDIR Python-2.7.9
RUN ./configure --enable-optimizations
RUN make altinstall
RUN pip install requests

ENTRYPOINT /setup.sh

