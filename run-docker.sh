docker run --detach --name superset -p "8088:8088" -v $(pwd)/config:/etc/superset -v $(pwd)/data:/var/lib/superset amancevice/superset:0.25.6

