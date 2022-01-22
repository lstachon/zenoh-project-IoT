python3 manager.py &

sleep 2

python3 lamp.py 1 90 &
python3 lamp.py 2 35 &
python3 lamp.py 3 40 &

sleep 2

python3 door.py 1 &
python3 door.py 2 &
python3 door.py 3 &