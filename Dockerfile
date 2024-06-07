FROM python:3
EXPOSE 5001
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN echo '#!/bin/bash \n\n gunicorn --bind :5001 --workers ${WORKERS:-1} --threads ${THREADS:-8} --timeout ${TIMEOUT:-0} --log-level debug -k uvicorn.workers.UvicornWorker app:app "$@"' \
          > /usr/bin/entrypoint.sh \
    && chmod +x /usr/bin/entrypoint.sh 
COPY . /app
RUN useradd -d /home/appuser -m -s /bin/bash appuser && \
    chown -R appuser:appuser /app
USER appuser
WORKDIR /app/ 
ENTRYPOINT ["/usr/bin/entrypoint.sh"]
