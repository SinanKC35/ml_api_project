FROM python:3.9-slim

WORKDIR /code

RUN apt-get update && apt-get install -y libgomp1

# Αποτροπή C-level crashes του XGBoost/OpenMP σε περιβάλλον Docker
ENV OMP_NUM_THREADS=1
ENV KMP_DUPLICATE_LIB_OK=TRUE

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app
COPY ./models /code/models

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]