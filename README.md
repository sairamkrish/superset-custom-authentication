To run superset as docker:
---

This repository uses [Dockerized superset](https://hub.docker.com/r/amancevice/superset/). 

## Pre-requisites

 * Docker v18+

## First time

Let's download the docker image, create a container and start the container.

`sh run-docker.sh` - contains the required commands to get you started

Superset needs to initialize the database and create admin user account. Please execute the following command

`docker exec -it superset superset-init`

#### Connecting to dataSources
To visualize the data, we need to connect Superset with our desired database. For example, to connect to a postgres database in host system (let's say for Mac), use following configuration in the config/superset_config.py

SQLAlchemy URI :
 `postgresql://username:yourPass@host.docker.internal:5432/database`

## Start superset

After the first time, the container is already created and it's ready to be used. Simply run the following command to start the container

`docker container start superset`

view logs:
`docker logs -f superset`

load examples:
`docker exec -it superset superset load_examples`
