FROM python:3.12.8-bookworm

WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 1000 appuser

RUN mkdir -p /.local /.cache/huggingface /.config /.jupyter /.triton
RUN chown -R appuser:appuser /usr/src/app /.local /.cache /.config /.jupyter /.triton

USER appuser

HEALTHCHECK CMD curl --fail -H "Accept: text/html" http://localhost:8000 || exit 1

ENV PYTHONPATH="/usr/src/app:$PYTHONPATH"
CMD [ "jupyter", "notebook", "--no-browser", "--ip=0.0.0.0", "--port=8000" ]
