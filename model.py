# Plik przechowuje dane startowe programu oraz proste funkcje do zapisu i odczytu danych.
import json  # Importuje modul json, ktory pozwala zapisywac i odczytywac dane z pliku.
import os  # Importuje modul os, ktory pozwala sprawdzac, czy plik istnieje.

DATA_FILE = "data.json"  # Ustawia nazwe pliku, w ktorym aplikacja zapisuje dane.

users = [  # Tworzy liste uzytkownikow, ktorzy moga zalogowac sie do systemu.
    {"login": "admin", "password": "admin"}  # Dodaje podstawowe konto administratora.
]  # Konczy liste uzytkownikow.

companies = [  # Tworzy liste central firm z magazynami.
    {"id": 1, "name": "Firma Alfa", "city": "Warszawa", "address": "ul. Prosta 1", "latitude": 52.2297, "longitude": 21.0122},  # Dodaje centrale pierwszej firmy.
    {"id": 2, "name": "Firma Beta", "city": "Krakow", "address": "ul. Dluga 5", "latitude": 50.0647, "longitude": 19.9450},  # Dodaje centrale drugiej firmy.
    {"id": 3, "name": "Firma Gamma", "city": "Gdansk", "address": "ul. Morska 10", "latitude": 54.3520, "longitude": 18.6466}  # Dodaje centrale trzeciej firmy.
]  # Konczy liste central firm.

warehouses = [  # Tworzy liste magazynow wszystkich firm.
    {"id": 1, "company_id": 1, "name": "Magazyn Alfa 1", "city": "Warszawa", "address": "ul. Towarowa 20", "latitude": 52.2250, "longitude": 20.9890},  # Dodaje magazyn firmy Alfa.
    {"id": 2, "company_id": 1, "name": "Magazyn Alfa 2", "city": "Lodz", "address": "ul. Fabryczna 7", "latitude": 51.7592, "longitude": 19.4560},  # Dodaje drugi magazyn firmy Alfa.
    {"id": 3, "company_id": 2, "name": "Magazyn Beta 1", "city": "Krakow", "address": "ul. Magazynowa 3", "latitude": 50.0610, "longitude": 19.9360},  # Dodaje magazyn firmy Beta.
    {"id": 4, "company_id": 3, "name": "Magazyn Gamma 1", "city": "Gdansk", "address": "ul. Portowa 8", "latitude": 54.3600, "longitude": 18.6500}  # Dodaje magazyn firmy Gamma.
]  # Konczy liste magazynow.

employees = [  # Tworzy liste pracownikow firm.
    {"id": 1, "company_id": 1, "name": "Anna Kowalska", "position": "Kierownik", "city": "Warszawa", "latitude": 52.2300, "longitude": 21.0100},  # Dodaje pracownika firmy Alfa.
    {"id": 2, "company_id": 1, "name": "Jan Nowak", "position": "Magazynier", "city": "Lodz", "latitude": 51.7600, "longitude": 19.4550},  # Dodaje drugiego pracownika firmy Alfa.
    {"id": 3, "company_id": 2, "name": "Ewa Zielinska", "position": "Specjalista", "city": "Krakow", "latitude": 50.0650, "longitude": 19.9440},  # Dodaje pracownika firmy Beta.
    {"id": 4, "company_id": 3, "name": "Piotr Wisniewski", "position": "Logistyk", "city": "Gdansk", "latitude": 54.3510, "longitude": 18.6470}  # Dodaje pracownika firmy Gamma.
]  # Konczy liste pracownikow.

def make_database() -> dict:  # Definiuje funkcje, ktora sklada wszystkie listy w jeden slownik.
    return {"companies": companies, "warehouses": warehouses, "employees": employees}  # Zwraca dane aplikacji w jednej strukturze.

def save_database(database: dict) -> None:  # Definiuje funkcje zapisujaca dane do pliku.
    with open(DATA_FILE, "w", encoding="utf-8") as file:  # Otwiera plik do zapisu z polskim kodowaniem znakow.
        json.dump(database, file, indent=4, ensure_ascii=False)  # Zapisuje dane w czytelnej formie JSON.

def load_database() -> dict:  # Definiuje funkcje odczytujaca dane z pliku.
    if os.path.exists(DATA_FILE):  # Sprawdza, czy plik z danymi juz istnieje.
        with open(DATA_FILE, "r", encoding="utf-8") as file:  # Otwiera istniejacy plik do odczytu.
            return json.load(file)  # Zwraca dane wczytane z pliku JSON.
    database = make_database()  # Tworzy dane startowe, jezeli pliku jeszcze nie ma.
    save_database(database)  # Zapisuje dane startowe do pliku.
    return database  # Zwraca dane startowe do programu.
