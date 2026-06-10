# Plik przechowuje dane startowe programu oraz proste funkcje do zapisu i odczytu danych.
import json  # Importuje moduł json, który pozwala zapisywać i odczytywać dane z pliku.
import os  # Importuje moduł os, który pozwala sprawdzać, czy plik istnieje.

DATA_FILE = "data.json"  # Ustawia nazwe pliku, w ktorym aplikacja zapisuje dane.

users = [  # Tworzy listę użytkowników, którzy mogą zalogować się do systemu.
    {"login": "admin", "password": "123"}  # Dodaje podstawowe konto administratora.
]  # Kończy listę użytkowników.

companies = [  # Tworzy liste central firm z magazynami.
    {"id": 1, "name": "Raben Logistics Polska", "city": "Robakowo", "address": "ul. Zbożowa 1", "latitude": 52.3170, "longitude": 17.0660},  # Dodaje centralę firmy Raben Logistics Polska.
    {"id": 2, "name": "Röhlig SUUS Logistics", "city": "Warszawa", "address": "ul. Równoległa 4A", "latitude": 52.1690, "longitude": 20.9670},  # Dodaje centralę firmy Röhlig SUUS Logistics.
    {"id": 3, "name": "FM Logistic Polska", "city": "Mszczonów", "address": "ul. Tarczyńska 111", "latitude": 51.9740, "longitude": 20.5200},  # Dodaje centralę firmy FM Logistic Polska.
    {"id": 4, "name": "DHL Supply Chain Polska", "city": "Warszawa", "address": "ul. Osmańska 2", "latitude": 52.1560, "longitude": 21.0040}  # Dodaje centralę firmy DHL Supply Chain Polska.
]  # Konczy liste central firm.

warehouses = [  # Tworzy liste magazynow wszystkich firm.
    {"id": 1, "company_id": 1, "name": "Raben Oddział Robakowo", "city": "Robakowo", "address": "ul. Zbożowa 1", "latitude": 52.3170, "longitude": 17.0660},  # Dodaje magazyn firmy Raben w Robakowie.
    {"id": 2, "company_id": 1, "name": "Raben Oddział Sosnowiec", "city": "Sosnowiec", "address": "ul. Inwestycyjna", "latitude": 50.2860, "longitude": 19.1040},  # Dodaje magazyn firmy Raben w Sosnowcu.
    {"id": 3, "company_id": 2, "name": "SUUS Magazyn Warszawa", "city": "Warszawa", "address": "ul. Równoległa 4A", "latitude": 52.1690, "longitude": 20.9670},  # Dodaje magazyn firmy SUUS w Warszawie.
    {"id": 4, "company_id": 2, "name": "SUUS Magazyn Gdańsk", "city": "Gdańsk", "address": "okolice portu", "latitude": 54.3520, "longitude": 18.6466},  # Dodaje magazyn firmy SUUS w Gdańsku.
    {"id": 5, "company_id": 3, "name": "FM Logistic Platforma Mszczonów", "city": "Mszczonów", "address": "ul. Tarczyńska 111", "latitude": 51.9740, "longitude": 20.5200},  # Dodaje magazyn firmy FM Logistic w Mszczonowie.
    {"id": 6, "company_id": 4, "name": "DHL Supply Chain Warszawa", "city": "Warszawa", "address": "ul. Osmańska 2", "latitude": 52.1560, "longitude": 21.0040}  # Dodaje magazyn firmy DHL Supply Chain w Warszawie.
]  # Konczy liste magazynow.

employees = [  # Tworzy liste pracownikow firm.
    {"id": 1, "company_id": 1, "name": "Anna Kowalska", "position": "Kierownik magazynu", "city": "Robakowo", "latitude": 52.3170, "longitude": 17.0660},  # Dodaje przykładowego pracownika firmy Raben.
    {"id": 2, "company_id": 1, "name": "Jan Wiśniewski", "position": "Magazynier", "city": "Sosnowiec", "latitude": 50.2860, "longitude": 19.1040},  # Dodaje drugiego przykładowego pracownika firmy Raben.
    {"id": 3, "company_id": 2, "name": "Ewa Zielińska", "position": "Specjalista ds. transportu", "city": "Warszawa", "latitude": 52.1690, "longitude": 20.9670},  # Dodaje przykładowego pracownika firmy SUUS.
    {"id": 4, "company_id": 3, "name": "Piotr Nowak", "position": "Logistyk", "city": "Mszczonów", "latitude": 51.9740, "longitude": 20.5200},  # Dodaje przykładowego pracownika firmy FM Logistic.
    {"id": 5, "company_id": 4, "name": "Katarzyna Wójcik", "position": "Koordynator dostaw", "city": "Warszawa", "latitude": 52.1560, "longitude": 21.0040}  # Dodaje przykładowego pracownika firmy DHL Supply Chain.
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
