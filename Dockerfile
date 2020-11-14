FROM python:3.9-slim

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8090

ADD resources resources
ADD sample-sheet sample-sheet
ADD src src

CMD ["python", "src/main.py"]

