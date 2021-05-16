FROM python:3.9.2-alpine

ENV PATH="/scripts:${PATH}"

COPY requirements.txt /requirements.txt

# Install build deps, then run `pip install`, then remove unneeded build deps all in a single step.
# Correct the path to your production requirements file, if needed.
RUN set -ex \
    && BUILD_DEPS=" musl-dev python3-dev libffi-dev openssl-dev cargo  zlib-dev \
    ffmpeg postgresql-libs postgresql-dev gcc libc-dev linux-headers jpeg-dev alpine-sdk \
    " \
    && apk add --update --no-cache --virtual .tmp $BUILD_DEPS \
    && apk add --no-cache libpq \
    && pip install --no-cache-dir -r /requirements.txt
#   \
#    && apk del .tmp
#RUN
#RUN apk add
#RUN pip install -r /requirements.txt
#RUN

RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /code/media
RUN mkdir -p /code/static
RUN adduser -D user
RUN chown -R user:user /code
RUN chmod -R 755 /code

USER user

CMD ["entrypoint.sh"]
