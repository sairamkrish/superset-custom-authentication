# This will create a container and start the container
# Useful for quick testing superset in isolation
# For running the whole set of applications, use create-container.sh instead

docker run --detach --name superset -p "8088:8088" -v $(pwd)/config:/etc/superset -v $(pwd)/data:/var/lib/superset amancevice/superset:0.25.6

