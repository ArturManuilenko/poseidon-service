FROM library/nginx:1.19-alpine

COPY ./src/poseidon__balancer/remote /etc/nginx

WORKDIR /docker_app

COPY ./src/poseidon__web/static /docker_app/poseidon__web/static
