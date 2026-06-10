# Projekt systemu do zarzadzania magazynami i zapasami towarow

Projekt jest prosta aplikacja GUI w Pythonie. Program korzysta z `tkinter` oraz `tkintermapview`.

## Uruchomienie

1. Otworz terminal w folderze projektu.
2. Zainstaluj biblioteke mapy:

```powershell
pip install -r requirements.txt
```

3. Uruchom program:

```powershell
python main.py
```

## Logowanie

Login: `admin`

Haslo: `123`

## Funkcje

- logowanie do systemu,
- lista central firm z dodawaniem, edycja, usuwaniem i mapa,
- lista magazynow z dodawaniem, edycja, usuwaniem i mapa,
- lista pracownikow z dodawaniem, edycja, usuwaniem i mapa,
- filtrowanie po dowolnym widocznym polu, na przyklad po nazwie, miescie, adresie albo stanowisku,
- wyswietlanie magazynow wybranej firmy,
- wyswietlanie pracownikow wybranej firmy,
- zapis danych do pliku `data.json`.

## Struktura plikow

- `main.py` uruchamia program,
- `model.py` przechowuje dane startowe i zapis JSON,
- `controller.py` zawiera logike CRUD,
- `gui.py` zawiera okna, tabele, formularze i mapy.
