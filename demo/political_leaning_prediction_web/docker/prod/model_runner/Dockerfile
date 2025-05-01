# 3.12.8-bookworm
FROM python@sha256:68ca65265c466f4b64f8ddab669e13bcba8d4ba77ec4c26658d36f2b9d1b1cad

WORKDIR /usr/src/model_runner

RUN pip install --no-cache-dir torch==2.6.0 transformers==4.50.3 protobuf==6.30.2 sentencepiece==0.2.0 flask==3.1.0 \
 && mkdir -p /.cache /.local \
 && chown -R 1000:1000 /usr/src/model_runner /.cache /.local

USER 1000:1000

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost:8001/politicalness || exit 1

CMD [ "python", "main.py" ]
