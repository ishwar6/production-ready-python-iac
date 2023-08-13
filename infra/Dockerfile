FROM --platform=linux/amd64 python:3.10.8
LABEL maintainer="Ishwar"

ENV PYTHONUNBUFFERED 1
COPY /req.txt /tmp/req.txt
COPY /api /api
WORKDIR /api
EXPOSE 9000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/req.txt && \
    rm -rf /tmp && \
    adduser --disabled-password --no-create-home django-user

ENV PATH="/scripts:/py/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin:/:"${PATH}
RUN chown django-user:django-user -R /api/


USER root
COPY ./infra/gunicorn/gunicorn-entrypoint.sh /gunicorn-entrypoint.sh
RUN chmod +x /gunicorn-entrypoint.sh
RUN mkdir -p /vol/static
RUN chown -R django-user:django-user /vol/static
RUN chmod -R 755 /vol/static
RUN /py/bin/python manage.py collectstatic --no-input
RUN mkdir -p /var/log/gunicorn && chown -R django-user:django-user /var/log/gunicorn && chmod -R 755 /var/log/gunicorn

USER django-user
VOLUME /vol/static

CMD ["/gunicorn-entrypoint.sh"]

#Dockerimage code ---BUILD (docker build -f location/of/dockerfile .--> docker image ---RUN docker run -p ports:expose image_name> container (docker ps: all running container; docker ps -a)