# <p align=center> <a name="top">RevoProject</a></p>  

Projekt stworzony na potrzeby zadania rekrutacyjnego.

## Directory tree

```
├───core                                    # Główny folder projektu z takimi plikami jak np. 'settings.py'
└───revo                                    # Folder aplikacji 'Revo'
    │   tests.py                            # Plik z testami jednostkowymi 
    │
    ├───management
    │   └───commands
    │       │   download_revo_data.py       # Plik z komendą do pobierania danych z API
|
│   .gitignore
│   README.md
│   manage.py
|   requirements.txt   
```

## Instalacja i uruchomienie testów wykorzystując virtual environment i konsolę bash
- Klonowanie repozytorium ```git clone https://github.com/krzysztofgrabczynski/RevoProject.git```
- Przejście do folderu projektu ``` cd RevoProject/ ```
- Stworzenie wirtualnego środowiska poprzez ``` python -m venv venv ``` 
- Użycie ``` . venv/Scripts/activate ``` aby zaktywować lokalne środowisko
- Zainsalowanie zależności używając ``` pip install -r requirements.txt ```
- Uruchomienie testów jednostkowych poprzez ``` python manage.py test ```


## Dodatkowe informacje:
W celu uproszczenia projektu oraz zwiększenia jego przejrzystości, świadomie zrezygnowałem z kilku elementów:
- Dane konfiguracyjne: Pozostawiłem takie dane jak secret_key czy opcje debugowania bez ukrywania ich w osobnych plikach konfiguracyjnych.
- Testy jednostkowe: W przypadku testu "Zwrócenie przez API danych o nieprawidłowym typie" sprawdziłem tylko jeden przykład nieprawidłowego formatu. W środowisku produkcyjnym należałoby rozszerzyć zakres testów o inne przypadki, takie jak brakujące wartości czy błędne typy danych. Można również użyć testów parametryzowanych.
- Walidacja danych: W metodzie validate_data uprościłem sprawdzanie poprawności danych. W produkcyjnym kodzie warto rozważyć użycie bardziej zaawansowanych narzędzi, takich jak serializatory Django REST Framework lub biblioteka Pydantic, co ułatwiłoby rozwój i utrzymanie aplikacji.
- Narzędzia wspierające rozwój: Zrezygnowałem z użycia konteneryzacji (np. Docker) oraz narzędzi do zarządzania zależnościami (np. Poetry), aby projekt był prostszy do analizy.



[Go to top](#top) 
