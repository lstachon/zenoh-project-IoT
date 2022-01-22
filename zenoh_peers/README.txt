1. Jak uruchomić? - z folderu zenoh_peers odpalić skrypt ./app.sh

2. Jak ubić?
   a) pkill python

3. Działanie - procesy odpalane w skrypcie są swoimi rówieśnikami, automatycznie nawiązują ze sobą połączenia
   i słuchają na komunikaty od innych procesów (dzięki użyciu metody subscribe na topicu). Prezentowany tutaj
   mechanizm działa na zasadzie pub/sub. Warto zwrócić uwagę, że do publikowania w Zenohu używana jest ta sama metoda,
   co do umieszczania danych w routerze. Wynika z tego, że gdybyśmy włączyli także router i zdefiniowali w nim
   storage dla tego samego topicu dane byłyby dodatkowo persystowane. Można to sprawdzić wykonując odpowiednie
   restowe query o zawartość storage'a w routerze (w naszym przykładzie curl http://localhost:8000/bank/**).