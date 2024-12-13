# 1. Calculatrice


## Comment build le Dockerfile

```bash
docker build -t calc .
```

## Comment up le docker compose

```bash
docker-compose up --build -d
```

## Comment modifier le port d"écoute

```bash
docker run -d -p 6767:9090 -e CALC_PORT=9090 calc 
```

