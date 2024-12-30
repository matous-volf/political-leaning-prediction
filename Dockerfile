FROM python:3.12.8-bookworm

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /.local /.cache/huggingface /.config
RUN chown -R 1000:1000 /usr/src/app /.local /.cache /.config

USER 1000:1000

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost:8000 || exit 1

CMD [ "jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--port=8000" ]
