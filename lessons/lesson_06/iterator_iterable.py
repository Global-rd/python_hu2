#ITERABLE: egy objektum amely képes egyesével visszadni az elemeit (pl: list, string)
#ITERATOR: egy speciális objektum amely egyszerre egy elemet ad vissza egy iterable-ből, az iter() functionnel hozzuk létre, és next() functiont hívjuk meg
#ITERATION: elemenként haladás folyamata, egy elemről a másikra való eljutást nevezzük iterációnak
#LOOP: automatizálja az iteration folyamatát

#PÉLDA

#ITERABLE: Spotify (vagy bármilyen) lejátszási lista, benne a kedvenc zenéinkkel
#ITERATOR: mi magunk, akik egy zeneszámról a másikra tudunk kattintani a next gombbal. tudjuk, hogy most melyik szám szól, és képesek vagyunk a következőre ugrani
#ITERATION: következő számra való ugrás a next gombbal
#LOOP: automatikus lejátszás anélkül, hogy mi magunk megnyomnánk a next gombot, egészen addig amíg van zene a listában

#ITERABLE
playlist = ["I'm a barbie girl", "8 óra munka", "Heavy is the crown", "I got options"]
#ITERATOR
it = iter(playlist)
print(type(it))
#ITERATION
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#miért jó nekünk egy iterator?
#nem töltődik be az egész collection a memóriába, mindig az aktuális elemet tároljuk és dolgozunk vele (lazy evaluation)
# -> LOOP
