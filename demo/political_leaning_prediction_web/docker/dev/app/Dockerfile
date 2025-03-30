# 1.83.0-bookworm
FROM rust@sha256:a45bf1f5d9af0a23b26703b3500d70af1abff7f984a7abef5a104b42c02a292b

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang=1:14.0-55.7~deb12u1 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && cargo install dioxus-cli --version 0.6.3 \
 && cargo install diesel_cli --version 2.2.7

COPY app /srv/app
WORKDIR /srv/app

RUN mkdir -p /.local/share/dioxus \
 && chown -R 1000:1000 /srv/app /usr/local/cargo /.local/share/dioxus

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost:8000 || exit 1

USER 1000:1000

CMD ["dx", "serve", "--addr", "0.0.0.0", "--port", "8000"]
