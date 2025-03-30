# 23-alpine3.21
FROM node@sha256:c61b6b12a3c96373673cd52d7ecee2314e82bca5d541eecf0bc6aee870c8c6f7

WORKDIR /srv/app

COPY app/package.json .
COPY app/package-lock.json .

RUN npm install

USER 1000:1000

#checkov:skip=CKV_DOCKER_2: No need for (or even a simple way to do) a healthcheck.

CMD ["npm", "run", "watch"]
