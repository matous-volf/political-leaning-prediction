FROM python:3.12.8-bookworm

WORKDIR /usr/src/model_runner

RUN pip install --no-cache-dir torch transformers protobuf sentencepiece deepl flask

RUN mkdir -p /.cache /.local
RUN chown -R 1000:1000 /usr/src/model_runner /.cache /.local

USER 1000:1000

CMD [ "python", "main.py" ]
