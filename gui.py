# Plik zawiera interfejs graficzny aplikacji wykonany w bibliotece tkinter.
import tkinter as tk  # Importuje podstawowa biblioteke do tworzenia okien.
from tkinter import ttk, messagebox  # Importuje dodatkowe widzety oraz okna komunikatow.
import controller  # Importuje funkcje z pliku controller.py.

try:  # Rozpoczyna probe importu mapy.
    import tkintermapview  # Importuje biblioteke tkintermapview do wyswietlania mapy.
except ImportError:  # Obsluguje sytuacje, gdy biblioteka nie jest zainstalowana.
    tkintermapview = None  # Ustawia brak mapy, aby program mogl pokazac komunikat.

class WarehouseApp:  # Definiuje klase glownego programu GUI.
    def __init__(self, root):  # Definiuje funkcje startowa klasy.
        self.root = root  # Zapamietuje glowne okno programu.
        self.root.title("System zarzadzania magazynami i zapasami")  # Ustawia tytul glownego okna.
        self.root.geometry("1180x720")  # Ustawia rozmiar glownego okna.
        self.selected_company_id = None  # Tworzy zmienna na id zaznaczonej firmy.
        self.selected_warehouse_id = None  # Tworzy zmienna na id zaznaczonego magazynu.
        self.selected_employee_id = None  # Tworzy zmienna na id zaznaczonego pracownika.
        self.login_frame = tk.Frame(self.root, bg="#ffd6e8")  # Tworzy rozowy panel logowania.
        self.login_frame.pack(fill="both", expand=True)  # Pokazuje panel logowania na calym oknie.
        self.build_login_view()  # Buduje widok logowania.

    def build_login_view(self):  # Definiuje funkcje tworzaca ekran logowania.
        tk.Label(self.login_frame, text="Logowanie do systemu", bg="#ffd6e8", font=("Arial", 20, "bold")).pack(pady=40)  # Tworzy tytul logowania.
        tk.Label(self.login_frame, text="Login:", bg="#ffd6e8", font=("Arial", 12)).pack()  # Tworzy etykiete pola loginu.
        self.login_entry = tk.Entry(self.login_frame, width=30)  # Tworzy pole wpisywania loginu.
        self.login_entry.pack(pady=5)  # Pokazuje pole loginu.
        tk.Label(self.login_frame, text="Haslo:", bg="#ffd6e8", font=("Arial", 12)).pack()  # Tworzy etykiete pola hasla.
        self.password_entry = tk.Entry(self.login_frame, show="*", width=30)  # Tworzy pole wpisywania hasla.
        self.password_entry.pack(pady=5)  # Pokazuje pole hasla.
        tk.Button(self.login_frame, text="Zaloguj", bg="#ff69b4", fg="white", width=20, command=self.check_login).pack(pady=20)  # Tworzy rozowy przycisk logowania.
        tk.Label(self.login_frame, text="Dane testowe: admin / admin", bg="#ffd6e8").pack()  # Pokazuje podpowiedz z danymi testowymi.

    def check_login(self):  # Definiuje funkcje sprawdzajaca login i haslo.
        login = self.login_entry.get()  # Pobiera login wpisany przez uzytkownika.
        password = self.password_entry.get()  # Pobiera haslo wpisane przez uzytkownika.
        if controller.login_user(login, password):  # Sprawdza dane logowania w kontrolerze.
            self.login_frame.destroy()  # Usuwa ekran logowania po poprawnym logowaniu.
            self.build_main_view()  # Buduje glowny widok aplikacji.
        else:  # Wykonuje sie, gdy logowanie jest niepoprawne.
            messagebox.showerror("Blad", "Niepoprawny login lub haslo")  # Pokazuje komunikat bledu.

    def build_main_view(self):  # Definiuje funkcje tworzaca glowny widok programu.
        self.notebook = ttk.Notebook(self.root)  # Tworzy zakladki programu.
        self.notebook.pack(fill="both", expand=True)  # Pokazuje zakladki na calym oknie.
        self.company_tab = ttk.Frame(self.notebook)  # Tworzy zakladke central firm.
        self.warehouse_tab = ttk.Frame(self.notebook)  # Tworzy zakladke magazynow.
        self.employee_tab = ttk.Frame(self.notebook)  # Tworzy zakladke pracownikow.
        self.company_details_tab = ttk.Frame(self.notebook)  # Tworzy zakladke danych wybranej firmy.
        self.notebook.add(self.company_tab, text="Centrale firm")  # Dodaje zakladke central firm.
        self.notebook.add(self.warehouse_tab, text="Magazyny")  # Dodaje zakladke magazynow.
        self.notebook.add(self.employee_tab, text="Pracownicy")  # Dodaje zakladke pracownikow.
        self.notebook.add(self.company_details_tab, text="Wybrana firma")  # Dodaje zakladke wybranej firmy.
        self.build_company_tab()  # Buduje zawartosc zakladki firm.
        self.build_warehouse_tab()  # Buduje zawartosc zakladki magazynow.
        self.build_employee_tab()  # Buduje zawartosc zakladki pracownikow.
        self.build_company_details_tab()  # Buduje zawartosc zakladki wybranej firmy.
        self.refresh_all_views()  # Odswieza wszystkie tabele i mapy.

    def make_map(self, parent):  # Definiuje funkcje tworzaca mape albo komunikat o braku biblioteki.
        if tkintermapview is None:  # Sprawdza, czy biblioteka mapy nie zostala zainstalowana.
            label = tk.Label(parent, text="Brak biblioteki tkintermapview. Zainstaluj: pip install tkintermapview")  # Tworzy komunikat o braku mapy.
            label.pack(fill="both", expand=True)  # Pokazuje komunikat na miejscu mapy.
            return None  # Zwraca brak obiektu mapy.
        map_widget = tkintermapview.TkinterMapView(parent, width=520, height=420, corner_radius=0)  # Tworzy widzet mapy.
        map_widget.pack(fill="both", expand=True)  # Pokazuje mape w oknie.
        map_widget.set_position(52.0, 19.0)  # Ustawia srodek mapy na Polske.
        map_widget.set_zoom(6)  # Ustawia przyblizenie mapy.
        return map_widget  # Zwraca gotowa mape.

    def clear_map(self, map_widget):  # Definiuje funkcje czyszczaca znaczniki mapy.
        if map_widget is not None:  # Sprawdza, czy mapa istnieje.
            map_widget.delete_all_marker()  # Usuwa wszystkie znaczniki z mapy.

    def fill_map(self, map_widget, items, title_field):  # Definiuje funkcje dodajaca znaczniki do mapy.
        self.clear_map(map_widget)  # Czyści poprzednie znaczniki mapy.
        for item in items:  # Przechodzi po elementach, ktore maja byc pokazane na mapie.
            text = str(item[title_field]) + " - " + str(item["city"])  # Tworzy opis znacznika.
            if map_widget is not None:  # Sprawdza, czy mapa istnieje.
                map_widget.set_marker(item["latitude"], item["longitude"], text=text)  # Dodaje znacznik na mapie.

    def parse_float(self, value):  # Definiuje funkcje zamieniajaca tekst na liczbe zmiennoprzecinkowa.
        try:  # Rozpoczyna probe konwersji.
            return float(value.replace(",", "."))  # Zwraca liczbe i pozwala uzywac przecinka zamiast kropki.
        except ValueError:  # Obsluguje bledna liczbe.
            messagebox.showerror("Blad", "Wspolrzedne musza byc liczbami")  # Pokazuje komunikat bledu.
            return None  # Zwraca brak wartosci.

    def parse_int(self, value):  # Definiuje funkcje zamieniajaca tekst na liczbe calkowita.
        try:  # Rozpoczyna probe konwersji.
            return int(value)  # Zwraca liczbe calkowita.
        except ValueError:  # Obsluguje bledna liczbe.
            messagebox.showerror("Blad", "Id firmy musi byc liczba")  # Pokazuje komunikat bledu.
            return None  # Zwraca brak wartosci.

    def build_company_tab(self):  # Definiuje funkcje budujaca zakladke central firm.
        left = tk.Frame(self.company_tab)  # Tworzy lewy panel zakladki.
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)  # Ustawia lewy panel.
        right = tk.Frame(self.company_tab)  # Tworzy prawy panel zakladki.
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)  # Ustawia prawy panel.
        form = tk.Frame(left)  # Tworzy panel formularza.
        form.pack(fill="x")  # Pokazuje panel formularza.
        self.company_name = tk.Entry(form)  # Tworzy pole nazwy firmy.
        self.company_city = tk.Entry(form)  # Tworzy pole miasta firmy.
        self.company_address = tk.Entry(form)  # Tworzy pole adresu firmy.
        self.company_latitude = tk.Entry(form)  # Tworzy pole szerokosci geograficznej.
        self.company_longitude = tk.Entry(form)  # Tworzy pole dlugosci geograficznej.
        self.add_label_entry(form, "Nazwa", self.company_name, 0)  # Dodaje pole nazwy do formularza.
        self.add_label_entry(form, "Miasto", self.company_city, 1)  # Dodaje pole miasta do formularza.
        self.add_label_entry(form, "Adres", self.company_address, 2)  # Dodaje pole adresu do formularza.
        self.add_label_entry(form, "Szerokosc", self.company_latitude, 3)  # Dodaje pole szerokosci do formularza.
        self.add_label_entry(form, "Dlugosc", self.company_longitude, 4)  # Dodaje pole dlugosci do formularza.
        buttons = tk.Frame(left)  # Tworzy panel przyciskow.
        buttons.pack(fill="x", pady=5)  # Pokazuje panel przyciskow.
        tk.Button(buttons, text="Dodaj", command=self.add_company).pack(side="left", padx=3)  # Tworzy przycisk dodawania firmy.
        tk.Button(buttons, text="Aktualizuj", command=self.update_company).pack(side="left", padx=3)  # Tworzy przycisk aktualizacji firmy.
        tk.Button(buttons, text="Usun", command=self.delete_company).pack(side="left", padx=3)  # Tworzy przycisk usuwania firmy.
        tk.Button(buttons, text="Wyczysc", command=self.clear_company_form).pack(side="left", padx=3)  # Tworzy przycisk czyszczenia formularza.
        tk.Label(left, text="Filtruj po nazwie lub miescie").pack(anchor="w")  # Tworzy etykiete filtra.
        self.company_filter = tk.Entry(left)  # Tworzy pole filtra firm.
        self.company_filter.pack(fill="x", pady=3)  # Pokazuje pole filtra.
        self.company_filter.bind("<KeyRelease>", self.refresh_companies)  # Odswieza liste przy pisaniu filtra.
        columns = ("id", "name", "city", "address", "latitude", "longitude")  # Ustawia kolumny tabeli firm.
        self.company_tree = ttk.Treeview(left, columns=columns, show="headings", height=14)  # Tworzy tabele firm.
        self.setup_tree(self.company_tree, columns)  # Konfiguruje naglowki tabeli firm.
        self.company_tree.pack(fill="both", expand=True)  # Pokazuje tabele firm.
        self.company_tree.bind("<<TreeviewSelect>>", self.select_company)  # Obsluguje zaznaczenie firmy.
        self.company_map = self.make_map(right)  # Tworzy mape firm.

    def build_warehouse_tab(self):  # Definiuje funkcje budujaca zakladke magazynow.
        left = tk.Frame(self.warehouse_tab)  # Tworzy lewy panel zakladki.
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)  # Ustawia lewy panel.
        right = tk.Frame(self.warehouse_tab)  # Tworzy prawy panel zakladki.
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)  # Ustawia prawy panel.
        form = tk.Frame(left)  # Tworzy panel formularza.
        form.pack(fill="x")  # Pokazuje panel formularza.
        self.warehouse_company_id = tk.Entry(form)  # Tworzy pole id firmy.
        self.warehouse_name = tk.Entry(form)  # Tworzy pole nazwy magazynu.
        self.warehouse_city = tk.Entry(form)  # Tworzy pole miasta magazynu.
        self.warehouse_address = tk.Entry(form)  # Tworzy pole adresu magazynu.
        self.warehouse_latitude = tk.Entry(form)  # Tworzy pole szerokosci geograficznej.
        self.warehouse_longitude = tk.Entry(form)  # Tworzy pole dlugosci geograficznej.
        self.add_label_entry(form, "Id firmy", self.warehouse_company_id, 0)  # Dodaje pole id firmy do formularza.
        self.add_label_entry(form, "Nazwa", self.warehouse_name, 1)  # Dodaje pole nazwy do formularza.
        self.add_label_entry(form, "Miasto", self.warehouse_city, 2)  # Dodaje pole miasta do formularza.
        self.add_label_entry(form, "Adres", self.warehouse_address, 3)  # Dodaje pole adresu do formularza.
        self.add_label_entry(form, "Szerokosc", self.warehouse_latitude, 4)  # Dodaje pole szerokosci do formularza.
        self.add_label_entry(form, "Dlugosc", self.warehouse_longitude, 5)  # Dodaje pole dlugosci do formularza.
        buttons = tk.Frame(left)  # Tworzy panel przyciskow.
        buttons.pack(fill="x", pady=5)  # Pokazuje panel przyciskow.
        tk.Button(buttons, text="Dodaj", command=self.add_warehouse).pack(side="left", padx=3)  # Tworzy przycisk dodawania magazynu.
        tk.Button(buttons, text="Aktualizuj", command=self.update_warehouse).pack(side="left", padx=3)  # Tworzy przycisk aktualizacji magazynu.
        tk.Button(buttons, text="Usun", command=self.delete_warehouse).pack(side="left", padx=3)  # Tworzy przycisk usuwania magazynu.
        tk.Button(buttons, text="Wyczysc", command=self.clear_warehouse_form).pack(side="left", padx=3)  # Tworzy przycisk czyszczenia formularza.
        tk.Label(left, text="Filtruj po nazwie lub miescie").pack(anchor="w")  # Tworzy etykiete filtra.
        self.warehouse_filter = tk.Entry(left)  # Tworzy pole filtra magazynow.
        self.warehouse_filter.pack(fill="x", pady=3)  # Pokazuje pole filtra.
        self.warehouse_filter.bind("<KeyRelease>", self.refresh_warehouses)  # Odswieza magazyny przy pisaniu filtra.
        columns = ("id", "company_id", "name", "city", "address", "latitude", "longitude")  # Ustawia kolumny tabeli magazynow.
        self.warehouse_tree = ttk.Treeview(left, columns=columns, show="headings", height=14)  # Tworzy tabele magazynow.
        self.setup_tree(self.warehouse_tree, columns)  # Konfiguruje naglowki tabeli magazynow.
        self.warehouse_tree.pack(fill="both", expand=True)  # Pokazuje tabele magazynow.
        self.warehouse_tree.bind("<<TreeviewSelect>>", self.select_warehouse)  # Obsluguje zaznaczenie magazynu.
        self.warehouse_map = self.make_map(right)  # Tworzy mape magazynow.

    def build_employee_tab(self):  # Definiuje funkcje budujaca zakladke pracownikow.
        left = tk.Frame(self.employee_tab)  # Tworzy lewy panel zakladki.
        left.pack(side="left", fill="both", expand=True, padx=10, pady=10)  # Ustawia lewy panel.
        right = tk.Frame(self.employee_tab)  # Tworzy prawy panel zakladki.
        right.pack(side="right", fill="both", expand=True, padx=10, pady=10)  # Ustawia prawy panel.
        form = tk.Frame(left)  # Tworzy panel formularza.
        form.pack(fill="x")  # Pokazuje panel formularza.
        self.employee_company_id = tk.Entry(form)  # Tworzy pole id firmy.
        self.employee_name = tk.Entry(form)  # Tworzy pole imienia i nazwiska.
        self.employee_position = tk.Entry(form)  # Tworzy pole stanowiska.
        self.employee_city = tk.Entry(form)  # Tworzy pole miasta.
        self.employee_latitude = tk.Entry(form)  # Tworzy pole szerokosci geograficznej.
        self.employee_longitude = tk.Entry(form)  # Tworzy pole dlugosci geograficznej.
        self.add_label_entry(form, "Id firmy", self.employee_company_id, 0)  # Dodaje pole id firmy do formularza.
        self.add_label_entry(form, "Imie i nazwisko", self.employee_name, 1)  # Dodaje pole imienia i nazwiska do formularza.
        self.add_label_entry(form, "Stanowisko", self.employee_position, 2)  # Dodaje pole stanowiska do formularza.
        self.add_label_entry(form, "Miasto", self.employee_city, 3)  # Dodaje pole miasta do formularza.
        self.add_label_entry(form, "Szerokosc", self.employee_latitude, 4)  # Dodaje pole szerokosci do formularza.
        self.add_label_entry(form, "Dlugosc", self.employee_longitude, 5)  # Dodaje pole dlugosci do formularza.
        buttons = tk.Frame(left)  # Tworzy panel przyciskow.
        buttons.pack(fill="x", pady=5)  # Pokazuje panel przyciskow.
        tk.Button(buttons, text="Dodaj", command=self.add_employee).pack(side="left", padx=3)  # Tworzy przycisk dodawania pracownika.
        tk.Button(buttons, text="Aktualizuj", command=self.update_employee).pack(side="left", padx=3)  # Tworzy przycisk aktualizacji pracownika.
        tk.Button(buttons, text="Usun", command=self.delete_employee).pack(side="left", padx=3)  # Tworzy przycisk usuwania pracownika.
        tk.Button(buttons, text="Wyczysc", command=self.clear_employee_form).pack(side="left", padx=3)  # Tworzy przycisk czyszczenia formularza.
        tk.Label(left, text="Filtruj po nazwie lub miescie").pack(anchor="w")  # Tworzy etykiete filtra.
        self.employee_filter = tk.Entry(left)  # Tworzy pole filtra pracownikow.
        self.employee_filter.pack(fill="x", pady=3)  # Pokazuje pole filtra.
        self.employee_filter.bind("<KeyRelease>", self.refresh_employees)  # Odswieza pracownikow przy pisaniu filtra.
        columns = ("id", "company_id", "name", "position", "city", "latitude", "longitude")  # Ustawia kolumny tabeli pracownikow.
        self.employee_tree = ttk.Treeview(left, columns=columns, show="headings", height=14)  # Tworzy tabele pracownikow.
        self.setup_tree(self.employee_tree, columns)  # Konfiguruje naglowki tabeli pracownikow.
        self.employee_tree.pack(fill="both", expand=True)  # Pokazuje tabele pracownikow.
        self.employee_tree.bind("<<TreeviewSelect>>", self.select_employee)  # Obsluguje zaznaczenie pracownika.
        self.employee_map = self.make_map(right)  # Tworzy mape pracownikow.

    def build_company_details_tab(self):  # Definiuje funkcje budujaca zakladke wybranej firmy.
        top = tk.Frame(self.company_details_tab)  # Tworzy gorny panel wyboru firmy.
        top.pack(fill="x", padx=10, pady=10)  # Pokazuje gorny panel.
        tk.Label(top, text="Id firmy:").pack(side="left")  # Tworzy etykiete pola id firmy.
        self.details_company_id = tk.Entry(top, width=10)  # Tworzy pole wpisania id firmy.
        self.details_company_id.pack(side="left", padx=5)  # Pokazuje pole id firmy.
        tk.Button(top, text="Pokaz", command=self.refresh_company_details).pack(side="left")  # Tworzy przycisk pokazujacy dane firmy.
        tables = tk.Frame(self.company_details_tab)  # Tworzy panel dwoch list.
        tables.pack(fill="both", expand=True, padx=10, pady=10)  # Pokazuje panel dwoch list.
        left = tk.Frame(tables)  # Tworzy lewa czesc z magazynami.
        left.pack(side="left", fill="both", expand=True, padx=5)  # Pokazuje lewa czesc.
        right = tk.Frame(tables)  # Tworzy prawa czesc z pracownikami.
        right.pack(side="right", fill="both", expand=True, padx=5)  # Pokazuje prawa czesc.
        tk.Label(left, text="Magazyny wybranej firmy").pack(anchor="w")  # Tworzy tytul listy magazynow firmy.
        self.details_warehouse_tree = ttk.Treeview(left, columns=("id", "name", "city", "address"), show="headings", height=16)  # Tworzy tabele magazynow firmy.
        self.setup_tree(self.details_warehouse_tree, ("id", "name", "city", "address"))  # Konfiguruje tabele magazynow firmy.
        self.details_warehouse_tree.pack(fill="both", expand=True)  # Pokazuje tabele magazynow firmy.
        tk.Label(right, text="Pracownicy wybranej firmy").pack(anchor="w")  # Tworzy tytul listy pracownikow firmy.
        self.details_employee_tree = ttk.Treeview(right, columns=("id", "name", "position", "city"), show="headings", height=16)  # Tworzy tabele pracownikow firmy.
        self.setup_tree(self.details_employee_tree, ("id", "name", "position", "city"))  # Konfiguruje tabele pracownikow firmy.
        self.details_employee_tree.pack(fill="both", expand=True)  # Pokazuje tabele pracownikow firmy.

    def add_label_entry(self, parent, text, entry, row):  # Definiuje funkcje dodajaca etykiete i pole do formularza.
        tk.Label(parent, text=text).grid(row=row, column=0, sticky="w", pady=2)  # Dodaje etykiete w wybranym wierszu.
        entry.grid(row=row, column=1, sticky="ew", pady=2)  # Dodaje pole tekstowe w wybranym wierszu.
        parent.columnconfigure(1, weight=1)  # Ustawia rozszerzanie drugiej kolumny.

    def setup_tree(self, tree, columns):  # Definiuje funkcje ustawiajaca naglowki tabeli.
        for column in columns:  # Przechodzi po nazwach kolumn.
            tree.heading(column, text=column)  # Ustawia tekst naglowka kolumny.
            tree.column(column, width=110)  # Ustawia szerokosc kolumny.

    def fill_tree(self, tree, items, columns):  # Definiuje funkcje wypelniajaca tabele danymi.
        for row in tree.get_children():  # Przechodzi po obecnych wierszach tabeli.
            tree.delete(row)  # Usuwa stary wiersz z tabeli.
        for item in items:  # Przechodzi po nowych danych.
            values = []  # Tworzy pusta liste wartosci wiersza.
            for column in columns:  # Przechodzi po kolumnach tabeli.
                values.append(item[column])  # Dodaje wartosc wybranej kolumny.
            tree.insert("", "end", values=values)  # Dodaje nowy wiersz do tabeli.

    def refresh_all_views(self):  # Definiuje funkcje odswiezajaca caly program.
        self.refresh_companies()  # Odswieza centrale firm.
        self.refresh_warehouses()  # Odswieza magazyny.
        self.refresh_employees()  # Odswieza pracownikow.
        self.refresh_company_details()  # Odswieza widok wybranej firmy.

    def refresh_companies(self, event=None):  # Definiuje funkcje odswiezajaca centrale firm.
        text = self.company_filter.get()  # Pobiera tekst filtra firm.
        items = controller.filter_items(controller.get_companies(), text)  # Filtruje centrale firm.
        self.fill_tree(self.company_tree, items, ("id", "name", "city", "address", "latitude", "longitude"))  # Wypelnia tabele firm.
        self.fill_map(self.company_map, items, "name")  # Wypelnia mape firm tymi samymi wynikami.

    def refresh_warehouses(self, event=None):  # Definiuje funkcje odswiezajaca magazyny.
        text = self.warehouse_filter.get()  # Pobiera tekst filtra magazynow.
        items = controller.filter_items(controller.get_warehouses(), text)  # Filtruje magazyny.
        self.fill_tree(self.warehouse_tree, items, ("id", "company_id", "name", "city", "address", "latitude", "longitude"))  # Wypelnia tabele magazynow.
        self.fill_map(self.warehouse_map, items, "name")  # Wypelnia mape magazynow tymi samymi wynikami.

    def refresh_employees(self, event=None):  # Definiuje funkcje odswiezajaca pracownikow.
        text = self.employee_filter.get()  # Pobiera tekst filtra pracownikow.
        items = controller.filter_items(controller.get_employees(), text)  # Filtruje pracownikow.
        self.fill_tree(self.employee_tree, items, ("id", "company_id", "name", "position", "city", "latitude", "longitude"))  # Wypelnia tabele pracownikow.
        self.fill_map(self.employee_map, items, "name")  # Wypelnia mape pracownikow tymi samymi wynikami.

    def refresh_company_details(self):  # Definiuje funkcje odswiezajaca dane wybranej firmy.
        company_id = self.parse_int(self.details_company_id.get() or "1")  # Pobiera id firmy albo przyjmuje firme numer 1.
        if company_id is None:  # Sprawdza, czy id firmy jest niepoprawne.
            return  # Przerywa dzialanie funkcji.
        warehouses = controller.get_warehouses_for_company(company_id)  # Pobiera magazyny wybranej firmy.
        employees = controller.get_employees_for_company(company_id)  # Pobiera pracownikow wybranej firmy.
        self.fill_tree(self.details_warehouse_tree, warehouses, ("id", "name", "city", "address"))  # Wypelnia tabele magazynow firmy.
        self.fill_tree(self.details_employee_tree, employees, ("id", "name", "position", "city"))  # Wypelnia tabele pracownikow firmy.

    def select_company(self, event):  # Definiuje funkcje obslugujaca wybor firmy z tabeli.
        selected = self.company_tree.focus()  # Pobiera zaznaczony wiersz tabeli.
        if selected:  # Sprawdza, czy jakis wiersz jest zaznaczony.
            values = self.company_tree.item(selected, "values")  # Pobiera wartosci zaznaczonego wiersza.
            self.selected_company_id = int(values[0])  # Zapamietuje id wybranej firmy.
            self.clear_company_form()  # Czysci formularz firmy.
            self.company_name.insert(0, values[1])  # Wstawia nazwe firmy do formularza.
            self.company_city.insert(0, values[2])  # Wstawia miasto firmy do formularza.
            self.company_address.insert(0, values[3])  # Wstawia adres firmy do formularza.
            self.company_latitude.insert(0, values[4])  # Wstawia szerokosc do formularza.
            self.company_longitude.insert(0, values[5])  # Wstawia dlugosc do formularza.
            self.details_company_id.delete(0, tk.END)  # Czysci pole id firmy w zakladce szczegolow.
            self.details_company_id.insert(0, values[0])  # Wstawia id firmy do zakladki szczegolow.
            self.refresh_company_details()  # Odswieza magazyny i pracownikow wybranej firmy.

    def select_warehouse(self, event):  # Definiuje funkcje obslugujaca wybor magazynu z tabeli.
        selected = self.warehouse_tree.focus()  # Pobiera zaznaczony wiersz tabeli.
        if selected:  # Sprawdza, czy jakis wiersz jest zaznaczony.
            values = self.warehouse_tree.item(selected, "values")  # Pobiera wartosci zaznaczonego wiersza.
            self.selected_warehouse_id = int(values[0])  # Zapamietuje id wybranego magazynu.
            self.clear_warehouse_form()  # Czysci formularz magazynu.
            self.warehouse_company_id.insert(0, values[1])  # Wstawia id firmy do formularza.
            self.warehouse_name.insert(0, values[2])  # Wstawia nazwe magazynu do formularza.
            self.warehouse_city.insert(0, values[3])  # Wstawia miasto magazynu do formularza.
            self.warehouse_address.insert(0, values[4])  # Wstawia adres magazynu do formularza.
            self.warehouse_latitude.insert(0, values[5])  # Wstawia szerokosc do formularza.
            self.warehouse_longitude.insert(0, values[6])  # Wstawia dlugosc do formularza.

    def select_employee(self, event):  # Definiuje funkcje obslugujaca wybor pracownika z tabeli.
        selected = self.employee_tree.focus()  # Pobiera zaznaczony wiersz tabeli.
        if selected:  # Sprawdza, czy jakis wiersz jest zaznaczony.
            values = self.employee_tree.item(selected, "values")  # Pobiera wartosci zaznaczonego wiersza.
            self.selected_employee_id = int(values[0])  # Zapamietuje id wybranego pracownika.
            self.clear_employee_form()  # Czysci formularz pracownika.
            self.employee_company_id.insert(0, values[1])  # Wstawia id firmy do formularza.
            self.employee_name.insert(0, values[2])  # Wstawia imie i nazwisko do formularza.
            self.employee_position.insert(0, values[3])  # Wstawia stanowisko do formularza.
            self.employee_city.insert(0, values[4])  # Wstawia miasto do formularza.
            self.employee_latitude.insert(0, values[5])  # Wstawia szerokosc do formularza.
            self.employee_longitude.insert(0, values[6])  # Wstawia dlugosc do formularza.

    def add_company(self):  # Definiuje funkcje dodajaca firme z formularza.
        latitude = self.parse_float(self.company_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.company_longitude.get())  # Pobiera dlugosc geograficzna.
        if latitude is None or longitude is None:  # Sprawdza, czy wspolrzedne sa niepoprawne.
            return  # Przerywa dodawanie firmy.
        controller.add_company(self.company_name.get(), self.company_city.get(), self.company_address.get(), latitude, longitude)  # Dodaje firme przez kontroler.
        self.clear_company_form()  # Czysci formularz firmy.
        self.refresh_all_views()  # Odswieza widoki po dodaniu firmy.

    def update_company(self):  # Definiuje funkcje aktualizujaca firme.
        if self.selected_company_id is None:  # Sprawdza, czy wybrano firme.
            messagebox.showwarning("Uwaga", "Wybierz firme z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa aktualizacje.
        latitude = self.parse_float(self.company_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.company_longitude.get())  # Pobiera dlugosc geograficzna.
        if latitude is None or longitude is None:  # Sprawdza, czy wspolrzedne sa niepoprawne.
            return  # Przerywa aktualizacje firmy.
        controller.update_company(self.selected_company_id, self.company_name.get(), self.company_city.get(), self.company_address.get(), latitude, longitude)  # Aktualizuje firme przez kontroler.
        self.clear_company_form()  # Czysci formularz firmy.
        self.refresh_all_views()  # Odswieza widoki po aktualizacji.

    def delete_company(self):  # Definiuje funkcje usuwajaca firme.
        if self.selected_company_id is None:  # Sprawdza, czy wybrano firme.
            messagebox.showwarning("Uwaga", "Wybierz firme z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa usuwanie.
        controller.delete_company(self.selected_company_id)  # Usuwa firme przez kontroler.
        self.clear_company_form()  # Czysci formularz firmy.
        self.refresh_all_views()  # Odswieza widoki po usunieciu.

    def add_warehouse(self):  # Definiuje funkcje dodajaca magazyn.
        company_id = self.parse_int(self.warehouse_company_id.get())  # Pobiera id firmy.
        latitude = self.parse_float(self.warehouse_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.warehouse_longitude.get())  # Pobiera dlugosc geograficzna.
        if company_id is None or latitude is None or longitude is None:  # Sprawdza, czy dane liczbowe sa poprawne.
            return  # Przerywa dodawanie magazynu.
        controller.add_warehouse(company_id, self.warehouse_name.get(), self.warehouse_city.get(), self.warehouse_address.get(), latitude, longitude)  # Dodaje magazyn przez kontroler.
        self.clear_warehouse_form()  # Czysci formularz magazynu.
        self.refresh_all_views()  # Odswieza widoki po dodaniu.

    def update_warehouse(self):  # Definiuje funkcje aktualizujaca magazyn.
        if self.selected_warehouse_id is None:  # Sprawdza, czy wybrano magazyn.
            messagebox.showwarning("Uwaga", "Wybierz magazyn z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa aktualizacje.
        company_id = self.parse_int(self.warehouse_company_id.get())  # Pobiera id firmy.
        latitude = self.parse_float(self.warehouse_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.warehouse_longitude.get())  # Pobiera dlugosc geograficzna.
        if company_id is None or latitude is None or longitude is None:  # Sprawdza, czy dane liczbowe sa poprawne.
            return  # Przerywa aktualizacje magazynu.
        controller.update_warehouse(self.selected_warehouse_id, company_id, self.warehouse_name.get(), self.warehouse_city.get(), self.warehouse_address.get(), latitude, longitude)  # Aktualizuje magazyn przez kontroler.
        self.clear_warehouse_form()  # Czysci formularz magazynu.
        self.refresh_all_views()  # Odswieza widoki po aktualizacji.

    def delete_warehouse(self):  # Definiuje funkcje usuwajaca magazyn.
        if self.selected_warehouse_id is None:  # Sprawdza, czy wybrano magazyn.
            messagebox.showwarning("Uwaga", "Wybierz magazyn z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa usuwanie.
        controller.delete_warehouse(self.selected_warehouse_id)  # Usuwa magazyn przez kontroler.
        self.clear_warehouse_form()  # Czysci formularz magazynu.
        self.refresh_all_views()  # Odswieza widoki po usunieciu.

    def add_employee(self):  # Definiuje funkcje dodajaca pracownika.
        company_id = self.parse_int(self.employee_company_id.get())  # Pobiera id firmy.
        latitude = self.parse_float(self.employee_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.employee_longitude.get())  # Pobiera dlugosc geograficzna.
        if company_id is None or latitude is None or longitude is None:  # Sprawdza, czy dane liczbowe sa poprawne.
            return  # Przerywa dodawanie pracownika.
        controller.add_employee(company_id, self.employee_name.get(), self.employee_position.get(), self.employee_city.get(), latitude, longitude)  # Dodaje pracownika przez kontroler.
        self.clear_employee_form()  # Czysci formularz pracownika.
        self.refresh_all_views()  # Odswieza widoki po dodaniu.

    def update_employee(self):  # Definiuje funkcje aktualizujaca pracownika.
        if self.selected_employee_id is None:  # Sprawdza, czy wybrano pracownika.
            messagebox.showwarning("Uwaga", "Wybierz pracownika z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa aktualizacje.
        company_id = self.parse_int(self.employee_company_id.get())  # Pobiera id firmy.
        latitude = self.parse_float(self.employee_latitude.get())  # Pobiera szerokosc geograficzna.
        longitude = self.parse_float(self.employee_longitude.get())  # Pobiera dlugosc geograficzna.
        if company_id is None or latitude is None or longitude is None:  # Sprawdza, czy dane liczbowe sa poprawne.
            return  # Przerywa aktualizacje pracownika.
        controller.update_employee(self.selected_employee_id, company_id, self.employee_name.get(), self.employee_position.get(), self.employee_city.get(), latitude, longitude)  # Aktualizuje pracownika przez kontroler.
        self.clear_employee_form()  # Czysci formularz pracownika.
        self.refresh_all_views()  # Odswieza widoki po aktualizacji.

    def delete_employee(self):  # Definiuje funkcje usuwajaca pracownika.
        if self.selected_employee_id is None:  # Sprawdza, czy wybrano pracownika.
            messagebox.showwarning("Uwaga", "Wybierz pracownika z tabeli")  # Pokazuje ostrzezenie.
            return  # Przerywa usuwanie.
        controller.delete_employee(self.selected_employee_id)  # Usuwa pracownika przez kontroler.
        self.clear_employee_form()  # Czysci formularz pracownika.
        self.refresh_all_views()  # Odswieza widoki po usunieciu.

    def clear_company_form(self):  # Definiuje funkcje czyszczaca formularz firmy.
        self.selected_company_id = None  # Usuwa zapamietane id firmy.
        for entry in [self.company_name, self.company_city, self.company_address, self.company_latitude, self.company_longitude]:  # Przechodzi po polach formularza firmy.
            entry.delete(0, tk.END)  # Czysci wybrane pole formularza.

    def clear_warehouse_form(self):  # Definiuje funkcje czyszczaca formularz magazynu.
        self.selected_warehouse_id = None  # Usuwa zapamietane id magazynu.
        for entry in [self.warehouse_company_id, self.warehouse_name, self.warehouse_city, self.warehouse_address, self.warehouse_latitude, self.warehouse_longitude]:  # Przechodzi po polach formularza magazynu.
            entry.delete(0, tk.END)  # Czysci wybrane pole formularza.

    def clear_employee_form(self):  # Definiuje funkcje czyszczaca formularz pracownika.
        self.selected_employee_id = None  # Usuwa zapamietane id pracownika.
        for entry in [self.employee_company_id, self.employee_name, self.employee_position, self.employee_city, self.employee_latitude, self.employee_longitude]:  # Przechodzi po polach formularza pracownika.
            entry.delete(0, tk.END)  # Czysci wybrane pole formularza.

def start_app():  # Definiuje funkcje startujaca aplikacje.
    root = tk.Tk()  # Tworzy glowne okno tkinter.
    WarehouseApp(root)  # Tworzy obiekt aplikacji w glownym oknie.
    root.mainloop()  # Uruchamia petle zdarzen okna.
