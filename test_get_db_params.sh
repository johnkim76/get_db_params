#!/bin/bash

#postgresql-demo-apb param names
export POSTGRES_USER='postgresql-demo-user'
export POSTGRES_PASSWORD='postgresql-demo-password'
export POSTGRES_HOST='postgresql-demo-host'
export POSTGRES_DB='postgresql-demo-db'

#rhscl-postgresql-apb param names
export POSTGRESQL_USER='rhscl-user'
export POSTGRESQL_PASSWORD='rhscl-password'
export POSTGRESQL_HOST='rhscl-host'
export POSTGRESQL_DATABASE='rhscl-db'

./get_db_params.py