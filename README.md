To run superset as docker:
---

## First time
docker run --detach --name superset -p "8088:8088" -v /Users/sairamk/projects/experiments/superset/config:/etc/superset -v /Users/sairamk/projects/experiments/superset/data:/var/lib/superset amancevice/superset

docker exec -it superset superset-init

SQLAlchemy URI :
 `postgresql://purplecow:yourPass@host.docker.internal:5432/purple_cow`

## Start superset

`docker container start superset`

view logs:
`docker logs -f superset`

load examples:
`docker exec -it superset superset load_examples`
