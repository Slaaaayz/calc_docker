FROM python

WORKDIR /app

COPY serveur.py /app

ENV CALC_PORT=6767

ENTRYPOINT [ "python3", "serveur.py" ]
