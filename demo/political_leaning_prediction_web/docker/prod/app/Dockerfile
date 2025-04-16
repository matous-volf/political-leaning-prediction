# 1.83.0-bookworm
FROM rust@sha256:a45bf1f5d9af0a23b26703b3500d70af1abff7f984a7abef5a104b42c02a292b AS builder

RUN apt-get update && apt-get install -y --no-install-recommends \
    clang=1:14.0-55.7~deb12u1 \
    nodejs=18.19.0+dfsg-6~deb12u2 \
    npm=9.2.0~ds1-1 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/* \
 && cargo install dioxus-cli --version 0.6.3 \
 && cargo install diesel_cli --version 2.2.7

COPY app /srv/app
WORKDIR /srv/app

RUN npm install \
 && npm run build \
 && dx bundle

# bookworm
FROM debian@sha256:b877a1a3fdf02469440f1768cf69c9771338a875b7add5e80c45b756c92ac20a AS runner

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates=20230311 \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY --from=builder /srv/app/target/dx/political_leaning_prediction_web/release/web /srv/app

RUN chown -R 1000:1000 /srv/app

WORKDIR /srv/app

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost || exit 1

USER 1000:1000

ENV IP="0.0.0.0"
ENV PORT="80"
CMD ["./server"]
