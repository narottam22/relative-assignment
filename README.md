# Steps to run the code


1. Create a network for the interaction between two docker containers

```
bash create_network.sh
```

2. Run the postgres instance. Here postgres will be running inside docker

```
bash run_postgresql.sh
```

3. Now Build the contract app image, Run the following command:

```
python build_app.py create
```

4. After the image is built, run the container using this image. Run the below command:

```
python run_app.py start
```

5. We have exposed port 8989 for the app, so go to localhost:8989/docs for the fastapi swagger dashboard

6. Use the API routes to store and get the information
