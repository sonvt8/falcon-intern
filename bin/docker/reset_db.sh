#!/usr/bin/env bash
s=$BASH_SOURCE ; s=$(dirname "$s") ; s=$(cd "$s" && pwd) ; SCRIPT_HOME="$s"  # get SCRIPT_HOME=executed script's path, containing folder, cd & pwd to get container path
APP_HOME="$SCRIPT_HOME/../.."
c=sonvt8_falcon_intern_postgres  # c aka container
docker cp "$APP_HOME/customers.sql" $c:/
docker exec -it $c bash -c "psql -Upostgres -d customer_api -f /customers.sql"