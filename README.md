# GitHub – student04

Repozytorium ćwiczeniowe z przedmiotu DevOps.

## Cel projektu

Nauka obsługi Git, GitHub oraz podstaw CI/CD.

Projekt obejmuje pracę z repozytoriami, gałęziami, Pull Requestami, automatycznymi testami Python oraz budowaniem obrazów Docker.

## Autor

Student 04

## Moje środowisko DevOps

**System operacyjny:** Linux

**Wykorzystane narzędzia:**
- Git
- GitHub
- Terminal Linux
- Python 3
- pytest
- Docker
- GitHub Actions

## Uruchomienie projektu

### 1. Wymagania

- Git
- Python 3
- pytest (do uruchomienia testów)
- Docker (opcjonalnie)

### 2. Sklonowanie repozytorium

```bash
git clone https://github.com/marcinioza/github-student04.git
```

### 3. Przejście do katalogu projektu

```bash
cd github-student04
```

### 4. Sprawdzenie plików

```bash
ls -la
```

### 5. Uruchomienie programu Python

```bash
python3 app.py
```

Oczekiwany wynik:

```text
Witaj z kontenera Docker
```

## Testy jednostkowe Python

Aplikacja zawiera funkcje:

- `add(a, b)` – dodawanie liczb
- `subtract(a, b)` – odejmowanie liczb

Kod znajduje się w pliku `app/app.py`, a testy w `app/test_app.py`.

### Instalacja zależności

```bash
python3 -m pip install -r requirements.txt
```

### Uruchomienie testów

```bash
python3 -m pytest
```

Oczekiwany rezultat:

```text
2 passed
```

## Docker

### Budowanie obrazu

```bash
docker build -t github-student:local .
```

### Uruchomienie kontenera

```bash
docker run --rm github-student:local
```

Oczekiwany wynik:

```text
Witaj z kontenera Docker
```

## GitHub Actions – CI/CD

Projekt wykorzystuje GitHub Actions do automatyzacji testowania i budowania aplikacji.

Workflow CI automatycznie:

1. Pobiera kod z repozytorium.
2. Przygotowuje środowisko Python.
3. Instaluje wymagane zależności.
4. Uruchamia testy jednostkowe pytest.
5. Buduje obraz Docker.

Workflow uruchamia się po wysłaniu zmian (`push`) oraz przy zdarzeniach Pull Request.

Wyniki automatycznych testów:

https://github.com/marcinioza/github-student04/actions

## Zarządzanie projektem

W projekcie wykorzystano:
- Gałęzie Git i operacje merge
- Pull Request i Code Review
- GitHub Issues
- GitHub Projects z tablicą Kanban
- GitHub Secrets
- Klucze SSH
- Tagi i GitHub Releases

## Wydanie projektu

**Wersja końcowa:** v1.1.0

Wydania projektu:

https://github.com/marcinioza/github-student04/releases

## Podsumowanie

Projekt został wykonany w ramach 20 ćwiczeń DevOps.

Zrealizowano podstawowe operacje Git i GitHub, przygotowano aplikację Python z testami jednostkowymi oraz skonfigurowano automatyczny pipeline CI/CD wykorzystujący GitHub Actions i Docker.

Końcowe testy oraz budowanie obrazu Docker zakończyły się sukcesem.
