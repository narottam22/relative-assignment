# Steps to run the code

1. Run the postgres instance. Here postgres will be running inside docker

```
bash run_postgresql.sh
```

2. Now run the Fastapi instance

```
uvicorn main:app --reload
```

3. Go to localhost:8000/docs to see the fastapi swagger dashboard

4. Use the API routes to store and get the information
