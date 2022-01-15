sudo docker run --init -p 7447:7447/tcp -p 8000:8000/tcp eclipse/zenoh &
curl -X PUT -H 'content-type:application/properties' -d 'path_expr=/bank/**' http://localhost:8000/@/router/local/plugin/storages/backend/memory/storage/my-storage &

sleep 2

python3 manager.py &

sleep 2

python3 lamp.py 1 90 &
python3 lamp.py 2 35 &
python3 lamp.py 3 40 &

sleep 2

python3 door.py 1 &
python3 door.py 2 &
python3 door.py 3 &