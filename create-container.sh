# This helps to just create a container but don't start it
# Useful while running the container from a docker-compose kind of flows
docker create --name superset -p "8088:8088" -v $(pwd)/config:/etc/superset -v $(pwd)/data:/var/lib/superset amancevice/superset:0.25.6
