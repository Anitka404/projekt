# Projekt systemu do zarządzania magazynami i zapasami towarów

Projekt jest prostą aplikacją GUI w Pythonie. Program korzysta z `tkinter` oraz `tkintermapview`.

## Uruchomienie

1. Otwórz terminal w folderze projektu.
2. Zainstaluj bibliotekę mapy:

```powershell
pip install -r requirements.txt
```

3. Uruchom program:

```powershell
python main.py
```

Możesz też uruchomić plik `uruchom.bat`.

## Logowanie

Login: `admin`

Hasło: `123`

## Dane startowe

W projekcie są przykładowe dane o rzeczywistych firmach logistycznych i magazynowych:

- Raben Logistics Polska,
- Röhlig SUUS Logistics,
- FM Logistic Polska,
- DHL Supply Chain Polska.

## Funkcje

- logowanie do systemu,
- lista central firm z dodawaniem, edycją, usuwaniem i mapą,
- lista magazynów z dodawaniem, edycją, usuwaniem i mapą,
- lista pracowników z dodawaniem, edycją, usuwaniem i mapą,
- filtrowanie po dowolnym widocznym polu, na przykład po nazwie, mieście, adresie albo stanowisku,
- automatyczne uzupełnianie współrzędnych i podgląd znacznika po wpisaniu miasta,
- wyświetlanie magazynów wybranej firmy,
- wyświetlanie pracowników wybranej firmy,
- zapis danych do pliku `data.json`.

## Struktura plików

- `main.py` uruchamia program,
- `model.py` przechowuje dane startowe i zapis JSON,
- `controller.py` zawiera logikę CRUD,
- `gui.py` zawiera okna, tabele, formularze i mapy.
