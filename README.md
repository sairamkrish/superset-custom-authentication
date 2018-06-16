Apache Superset Custom Authentication
---

Apache Superset is an amazing open source platform. This repository provides reference implementations to help customize Superset's Authentication flow.

## Pre-requisites

 * Docker v18+

#### Docker installation on AWS EC2

Please refer [Amazon EC2 docs - Docker section](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html), for any latest change. On a high level, following command should help

````
sudo yum update
sudo yum install -y docker
sudo usermod -a -G docker ec2-user
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` | sudo tee /usr/local/bin/docker-compose > /dev/null
sudo chmod +x /usr/local/bin/docker-compose
sudo service docker start
sudo chkconfig docker on
````

## First time

Let's download the [superset docker image](https://hub.docker.com/r/amancevice/superset/), create a container and start the container.

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

## Upgrading docker images

```
# Pull desired version
docker pull amancevice/superset

# Remove the current container
docker rm -f superset-old

# Deploy a new container ...
docker run --detach --name superset-new [options] amancevice/superset

# Upgrade the DB
docker exec superset-new superset db upgrade
```