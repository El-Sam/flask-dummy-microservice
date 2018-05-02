FROM frolvlad/alpine-python3

MAINTAINER Sam El <sam.elaabidi@gmail.com>

RUN apk add --no-cache \
    postgresql \
    postgresql-dev \
    bash \
    gcc \
    python3-dev \
    linux-headers \
    musl-dev \
    bash-completion && \
    pip3 install --no-cache-dir --upgrade \
    pip \
    uwsgi==2.0.* && \
    rm -r /root/.cache

COPY ./docker/requirements.txt ./docker/requirements_prod.txt /tmp/

ARG PROJECT

RUN pip3 install -r /tmp/requirements_prod.txt &&\
    mkdir -p /app/${PROJECT}

ADD . /app/${PROJECT}/
RUN chown -R daemon:daemon /app/${PROJECT} &&\
    chmod -R 0766 /app/${PROJECT}/

USER daemon

WORKDIR /app/${PROJECT}

CMD ["uwsgi", "docker/uwsgi.ini"]