docker run --init -p 7447:7447/tcp -p 8000:8000/tcp eclipse/zenoh &

sleep 4 &&

curl -X PUT -H 'content-type:application/properties' -d 'path_expr=/bank/**' http://localhost:8000/@/router/local/plugin/storages/backend/memory/storage/my-storage
