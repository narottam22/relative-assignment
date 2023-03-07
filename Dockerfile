ARG base_image

FROM $base_image

COPY ./app /app

RUN pip install --no-cache-dir --upgrade -r /app/req.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]