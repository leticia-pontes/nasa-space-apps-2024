FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir pandas dash dash-bootstrap-components
COPY . .
RUN chmod +x entrypoint.sh
EXPOSE 8050
ENTRYPOINT ["./entrypoint.sh"]
