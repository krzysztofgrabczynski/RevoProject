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
```


## Instalacja i uruchomienie testów wykorzystując virtual envoronment i konsolę bash
- Klonowanie repozytorium ```https://github.com/krzysztofgrabczynski/RevoProject.git```
- Stworzenie wirtualnego środowiska poprzez: ``` python -m venv venv ``` 
- Użycie ``` . venv/Scripts/activate ``` aby zaktywować lokalne środowisko
- Zainsalowanie zależności używając ``` pip install -r requirements.txt ```
- Użycie komendy poprzez ``` python manage.py download_revo_data ``` lub uruchomienie testów jednostkowych poprzez ``` python manage.py test ```


[Go to top](#top) 
