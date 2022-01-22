1. Jak uruchomić? - z folderu zenoh_router:
   a) odpalić skrypt: sudo ./router.sh
   b) odpalić skrypt: ./app.sh


1. Jak ubić?
   a) pkill python
   b) sudo pkill docker

3. Działanie - w tym przykładzie znaczna większość interakcji podejmowana jest poprzez
   polling routera metodą get zamiast polegania na mechanizmie subskrypcji. Pollujemy
   z interwałem 1s. Jedynie manager subskrybuje na dowolne nowe rejestracje lamp, a następnie
   odpytuje każdy zarejestrowany topic metodą get. Rozwiązanie ma demonstrować działanie
   storage'a w routerze.