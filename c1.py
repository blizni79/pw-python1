# Instrukcja warunkowa if-else:
# Poproś użytkownika o podanie liczby i sprawdź, czy jest ona większa niż 10. Wypisz odpowiedni komunikat.

liczba = int(input("Podaj liczbę: "))
if liczba > 10:
    print("Liczba jest większa niż 10.")
else:
    print("Liczba nie jest większa niż 10.")

# Instrukcja warunkowa elif:
# Poproś użytkownika o podanie wieku i wydrukuj odpowiednią wiadomość na podstawie podanego wieku: "Dziecko", "Młodzież", "Dorosły".

wiek = int(input("Podaj swój wiek: "))
if wiek < 18:
    print("Jesteś dzieckiem.")
elif wiek < 30:
    print("Jesteś młodzieżą.")
else:
    print("Jesteś dorosły.")


# Sprawdzenie wartości prawdziwej/fałszywej:
# Zadeklaruj zmienną "warunek" o wartości True i napisz instrukcję warunkową, która wypisze "Prawda" lub "Fałsz" na podstawie wartości tej zmiennej.

warunek= True

if warunek:
    print("Prawda")
else:
    print("Fałsz")

# Sprawdzenie czy liczba jest parzysta:
# Poproś użytkownika o podanie liczby całkowitej i sprawdź, czy jest ona parzysta. Wypisz odpowiedni komunikat.

liczba = int(input("Podaj liczbę: "))
if liczba % 2 == 0:
    print("Liczba jest parzysta.")
else:
    print("Liczba jest nieparzysta.")

# Operator logiczny AND:
# Poproś użytkownika o podanie swojego wieku i informacji, czy ma prawo jazdy. Następnie sprawdź, czy użytkownik jest pełnoletni i ma prawo jazdy.

wiek = int(input("Podaj swój wiek: "))
prawo_jazdy = input("Czy masz prawo jazdy (Tak/Nie)? ").lower()

if wiek >= 18 and prawo_jazdy == "tak":
    print("Jesteś pełnoletni i masz prawo jazdy.")
else:
    print("Nie jesteś pełnoletni lub nie masz prawo jazdy.")





