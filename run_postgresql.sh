docker run -d \
 --name  postgres_db \
 -p 6000:5432 \
 -v postgres_vol:/var/lib/postgresql/data \
 -e POSTGRES_DB=contract_database \
 -e POSTGRES_USER=admin_user \
 -e POSTGRES_PASSWORD=admin_password \
 postgres:13.4-alpine3.14 postgres