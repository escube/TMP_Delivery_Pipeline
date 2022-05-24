FROM python:3-slim AS build-env
COPY . /app
WORKDIR /app

FROM gcr.io/distroless/python3
COPY --from=build-env /app /app
WORKDIR /app/src/questions

ENTRYPOINT ["python3","the_question.py"]
CMD ["wrong answer"]