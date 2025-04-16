FROM python:3.12.8-bookworm

WORKDIR /usr/src/model_runner

RUN pip install --no-cache-dir torch==2.6.0 transformers==4.50.3 protobuf==6.30.2 sentencepiece==0.2.0 flask==3.1.0 \
 && mkdir -p /.cache /.local \
 && chown -R 1000:1000 /usr/src/model_runner /.cache /.local

USER 1000:1000

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost:8001 || exit 1

CMD [ "python", "main.py" ]
