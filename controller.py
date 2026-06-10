# Plik zawiera funkcje obslugujace logike programu, czyli dodawanie, edycje, usuwanie i filtrowanie danych.
from model import load_database, save_database, users  # Importuje funkcje zapisu, odczytu oraz liste uzytkownikow.

database = load_database()  # Wczytuje dane aplikacji przy starcie programu.

city_coordinates = {  # Tworzy slownik miast i ich wspolrzednych.
    "warszawa": [52.2297, 21.0122],  # Dodaje wspolrzedne Warszawy.
    "krakow": [50.0647, 19.9450],  # Dodaje wspolrzedne Krakowa.
    "gdansk": [54.3520, 18.6466],  # Dodaje wspolrzedne Gdanska.
    "lodz": [51.7592, 19.4560],  # Dodaje wspolrzedne Lodzi.
    "wroclaw": [51.1079, 17.0385],  # Dodaje wspolrzedne Wroclawia.
    "poznan": [52.4064, 16.9252],  # Dodaje wspolrzedne Poznania.
    "bialystok": [53.1325, 23.1688],  # Dodaje wspolrzedne Bialegostoku.
    "lublin": [51.2465, 22.5684],  # Dodaje wspolrzedne Lublina.
    "rzeszow": [50.0413, 21.9990],  # Dodaje wspolrzedne Rzeszowa.
    "szczecin": [53.4285, 14.5528],  # Dodaje wspolrzedne Szczecina.
    "bydgoszcz": [53.1235, 18.0084],  # Dodaje wspolrzedne Bydgoszczy.
    "torun": [53.0138, 18.5984],  # Dodaje wspolrzedne Torunia.
    "katowice": [50.2649, 19.0238],  # Dodaje wspolrzedne Katowic.
    "olsztyn": [53.7784, 20.4801],  # Dodaje wspolrzedne Olsztyna.
    "opole": [50.6751, 17.9213],  # Dodaje wspolrzedne Opola.
    "kielce": [50.8661, 20.6286]  # Dodaje wspolrzedne Kielc.
}  # Konczy slownik miast.

def normalize_city(city: str) -> str:  # Definiuje funkcje upraszczajaca nazwe miasta do porownania.
    city_text = city.lower().strip()  # Zamienia miasto na male litery i usuwa spacje z poczatku oraz konca.
    replacements = {"ą": "a", "ć": "c", "ę": "e", "ł": "l", "ń": "n", "ó": "o", "ś": "s", "ż": "z", "ź": "z"}  # Tworzy slownik polskich znakow do zamiany.
    for old_letter, new_letter in replacements.items():  # Przechodzi po parach znakow do zamiany.
        city_text = city_text.replace(old_letter, new_letter)  # Zamienia polski znak na prostsza litere.
    return city_text  # Zwraca uproszczona nazwe miasta.

def get_coordinates_for_city(city: str) -> list:  # Definiuje funkcje pobierajaca wspolrzedne miasta.
    city_key = normalize_city(city)  # Upraszcza nazwe miasta do klucza w slowniku.
    if city_key in city_coordinates:  # Sprawdza, czy miasto istnieje w slowniku.
        return city_coordinates[city_key]  # Zwraca wspolrzedne znalezionego miasta.
    return None  # Zwraca brak danych, gdy miasta nie ma w slowniku.

def login_user(login: str, password: str) -> bool:  # Definiuje funkcje sprawdzajaca logowanie.
    for user in users:  # Przechodzi po wszystkich zapisanych uzytkownikach.
        if user["login"] == login and user["password"] == password:  # Sprawdza, czy login i haslo sa poprawne.
            return True  # Zwraca prawde, gdy uzytkownik zostal znaleziony.
    return False  # Zwraca falsz, gdy dane logowania sa niepoprawne.

def get_new_id(items: list) -> int:  # Definiuje funkcje wyliczajaca nowe id dla listy.
    new_id = 1  # Ustawia poczatkowa wartosc id.
    for item in items:  # Przechodzi po elementach listy.
        if item["id"] >= new_id:  # Sprawdza, czy znalezione id jest wieksze lub rowne obecnemu.
            new_id = item["id"] + 1  # Ustawia nastepne wolne id.
    return new_id  # Zwraca nowe id.

def save_changes() -> None:  # Definiuje funkcje zapisujaca aktualny stan danych.
    save_database(database)  # Wywoluje zapis danych do pliku JSON.

def get_companies() -> list:  # Definiuje funkcje zwracajaca wszystkie centrale firm.
    return database["companies"]  # Zwraca liste central firm.

def get_warehouses() -> list:  # Definiuje funkcje zwracajaca wszystkie magazyny.
    return database["warehouses"]  # Zwraca liste magazynow.

def get_employees() -> list:  # Definiuje funkcje zwracajaca wszystkich pracownikow.
    return database["employees"]  # Zwraca liste pracownikow.

def add_company(name: str, city: str, address: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje dodajaca centrale firmy.
    company = {"id": get_new_id(database["companies"]), "name": name, "city": city, "address": address, "latitude": latitude, "longitude": longitude}  # Tworzy slownik nowej centrali.
    database["companies"].append(company)  # Dodaje centrale do listy firm.
    save_changes()  # Zapisuje zmiany do pliku.

def update_company(company_id: int, name: str, city: str, address: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje edytujaca centrale firmy.
    for company in database["companies"]:  # Przechodzi po wszystkich centralach firm.
        if company["id"] == company_id:  # Sprawdza, czy id centrali pasuje do edytowanego rekordu.
            company["name"] = name  # Zmienia nazwe firmy.
            company["city"] = city  # Zmienia miasto firmy.
            company["address"] = address  # Zmienia adres firmy.
            company["latitude"] = latitude  # Zmienia szerokosc geograficzna.
            company["longitude"] = longitude  # Zmienia dlugosc geograficzna.
    save_changes()  # Zapisuje zmiany do pliku.

def delete_company(company_id: int) -> None:  # Definiuje funkcje usuwajaca centrale firmy.
    for company in database["companies"][:]:  # Przechodzi po kopii listy firm, aby mozna bylo bezpiecznie usuwac.
        if company["id"] == company_id:  # Sprawdza, czy id firmy pasuje do usuwanego rekordu.
            database["companies"].remove(company)  # Usuwa firme z listy.
    for warehouse in database["warehouses"][:]:  # Przechodzi po kopii listy magazynow.
        if warehouse["company_id"] == company_id:  # Sprawdza, czy magazyn nalezy do usuwanej firmy.
            database["warehouses"].remove(warehouse)  # Usuwa magazyn usuwanej firmy.
    for employee in database["employees"][:]:  # Przechodzi po kopii listy pracownikow.
        if employee["company_id"] == company_id:  # Sprawdza, czy pracownik nalezy do usuwanej firmy.
            database["employees"].remove(employee)  # Usuwa pracownika usuwanej firmy.
    save_changes()  # Zapisuje zmiany do pliku.

def add_warehouse(company_id: int, name: str, city: str, address: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje dodajaca magazyn.
    warehouse = {"id": get_new_id(database["warehouses"]), "company_id": company_id, "name": name, "city": city, "address": address, "latitude": latitude, "longitude": longitude}  # Tworzy slownik nowego magazynu.
    database["warehouses"].append(warehouse)  # Dodaje magazyn do listy.
    save_changes()  # Zapisuje zmiany do pliku.

def update_warehouse(warehouse_id: int, company_id: int, name: str, city: str, address: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje edytujaca magazyn.
    for warehouse in database["warehouses"]:  # Przechodzi po wszystkich magazynach.
        if warehouse["id"] == warehouse_id:  # Sprawdza, czy id magazynu pasuje do edytowanego rekordu.
            warehouse["company_id"] = company_id  # Zmienia id firmy przypisanej do magazynu.
            warehouse["name"] = name  # Zmienia nazwe magazynu.
            warehouse["city"] = city  # Zmienia miasto magazynu.
            warehouse["address"] = address  # Zmienia adres magazynu.
            warehouse["latitude"] = latitude  # Zmienia szerokosc geograficzna.
            warehouse["longitude"] = longitude  # Zmienia dlugosc geograficzna.
    save_changes()  # Zapisuje zmiany do pliku.

def delete_warehouse(warehouse_id: int) -> None:  # Definiuje funkcje usuwajaca magazyn.
    for warehouse in database["warehouses"][:]:  # Przechodzi po kopii listy magazynow.
        if warehouse["id"] == warehouse_id:  # Sprawdza, czy id magazynu pasuje do usuwanego rekordu.
            database["warehouses"].remove(warehouse)  # Usuwa magazyn z listy.
    save_changes()  # Zapisuje zmiany do pliku.

def add_employee(company_id: int, name: str, position: str, city: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje dodajaca pracownika.
    employee = {"id": get_new_id(database["employees"]), "company_id": company_id, "name": name, "position": position, "city": city, "latitude": latitude, "longitude": longitude}  # Tworzy slownik nowego pracownika.
    database["employees"].append(employee)  # Dodaje pracownika do listy.
    save_changes()  # Zapisuje zmiany do pliku.

def update_employee(employee_id: int, company_id: int, name: str, position: str, city: str, latitude: float, longitude: float) -> None:  # Definiuje funkcje edytujaca pracownika.
    for employee in database["employees"]:  # Przechodzi po wszystkich pracownikach.
        if employee["id"] == employee_id:  # Sprawdza, czy id pracownika pasuje do edytowanego rekordu.
            employee["company_id"] = company_id  # Zmienia id firmy pracownika.
            employee["name"] = name  # Zmienia imie i nazwisko pracownika.
            employee["position"] = position  # Zmienia stanowisko pracownika.
            employee["city"] = city  # Zmienia miasto pracownika.
            employee["latitude"] = latitude  # Zmienia szerokosc geograficzna.
            employee["longitude"] = longitude  # Zmienia dlugosc geograficzna.
    save_changes()  # Zapisuje zmiany do pliku.

def delete_employee(employee_id: int) -> None:  # Definiuje funkcje usuwajaca pracownika.
    for employee in database["employees"][:]:  # Przechodzi po kopii listy pracownikow.
        if employee["id"] == employee_id:  # Sprawdza, czy id pracownika pasuje do usuwanego rekordu.
            database["employees"].remove(employee)  # Usuwa pracownika z listy.
    save_changes()  # Zapisuje zmiany do pliku.

def filter_items(items: list, text: str) -> list:  # Definiuje funkcje filtrujaca liste po dowolnym polu rekordu.
    results = []  # Tworzy pusta liste wynikow.
    text = text.lower()  # Zamienia tekst filtra na male litery.
    if text == "":  # Sprawdza, czy filtr jest pusty.
        return items  # Zwraca cala liste, gdy uzytkownik nic nie wpisal.
    for item in items:  # Przechodzi po elementach listy.
        for value in item.values():  # Przechodzi po wszystkich wartosciach wybranego rekordu.
            value_text = str(value).lower()  # Zamienia wartosc rekordu na tekst malymi literami.
            if text in value_text:  # Sprawdza, czy filtr pasuje do tej wartosci.
                results.append(item)  # Dodaje pasujacy element do wynikow.
                break  # Przerywa sprawdzanie tego rekordu, aby nie dodac go drugi raz.
    return results  # Zwraca przefiltrowana liste.

def get_company_ids_by_filter(text: str) -> list:  # Definiuje funkcje zwracajaca id firm pasujacych do filtra.
    companies = filter_items(database["companies"], text)  # Filtruje firmy po wpisanym tekscie.
    company_ids = []  # Tworzy pusta liste id firm.
    for company in companies:  # Przechodzi po pasujacych firmach.
        company_ids.append(company["id"])  # Dodaje id pasujacej firmy do listy.
    return company_ids  # Zwraca liste id pasujacych firm.

def get_warehouses_for_companies(company_ids: list) -> list:  # Definiuje funkcje zwracajaca magazyny kilku firm.
    results = []  # Tworzy pusta liste wynikow.
    for warehouse in database["warehouses"]:  # Przechodzi po wszystkich magazynach.
        if warehouse["company_id"] in company_ids:  # Sprawdza, czy magazyn nalezy do jednej z wybranych firm.
            results.append(warehouse)  # Dodaje magazyn do wynikow.
    return results  # Zwraca liste magazynow pasujacych firm.

def get_employees_for_companies(company_ids: list) -> list:  # Definiuje funkcje zwracajaca pracownikow kilku firm.
    results = []  # Tworzy pusta liste wynikow.
    for employee in database["employees"]:  # Przechodzi po wszystkich pracownikach.
        if employee["company_id"] in company_ids:  # Sprawdza, czy pracownik nalezy do jednej z wybranych firm.
            results.append(employee)  # Dodaje pracownika do wynikow.
    return results  # Zwraca liste pracownikow pasujacych firm.

def get_warehouses_for_company(company_id: int) -> list:  # Definiuje funkcje zwracajaca magazyny wybranej firmy.
    results = []  # Tworzy pusta liste wynikow.
    for warehouse in database["warehouses"]:  # Przechodzi po wszystkich magazynach.
        if warehouse["company_id"] == company_id:  # Sprawdza, czy magazyn nalezy do wybranej firmy.
            results.append(warehouse)  # Dodaje magazyn do wynikow.
    return results  # Zwraca liste magazynow firmy.

def get_employees_for_company(company_id: int) -> list:  # Definiuje funkcje zwracajaca pracownikow wybranej firmy.
    results = []  # Tworzy pusta liste wynikow.
    for employee in database["employees"]:  # Przechodzi po wszystkich pracownikach.
        if employee["company_id"] == company_id:  # Sprawdza, czy pracownik nalezy do wybranej firmy.
            results.append(employee)  # Dodaje pracownika do wynikow.
    return results  # Zwraca liste pracownikow firmy.
