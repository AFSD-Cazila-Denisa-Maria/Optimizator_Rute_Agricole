# Optimizator de Rute pentru Utilaje Agricole

## Descriere

Aplicatia calculeaza trasee optime pentru utilaje agricole folosind date reale din OpenStreetMap.

Utilizatorul selecteaza un punct de start si mai multe puncte de lucru pe harta.

Aplicatia determina ordinea optima de vizitare si afiseaza:

- traseul optim
- distanta totala
- timpul estimat

## Tehnologii utilizate

- Python
- Flask
- OSMnx
- NetworkX
- Leaflet
- OpenStreetMap

## Structura proiectului

```text
app.py
graph_utils.py
tsp_solver.py
templates/index.html
```

## Instalare

Instalarea bibliotecilor:

```bash
pip install flask
pip install osmnx
pip install networkx
pip install scikit-learn
```

## Rulare

```bash
python app.py
```

Aplicatia este disponibila la:

```text
http://127.0.0.1:5000
```

## Functionalitati

- selectare punct start
- selectare puncte de lucru
- calcul ruta optima
- afisare distanta
- afisare timp estimat
- vizualizare pe harta

## Autor

Nume studente: Cǎzilǎ Denisa-Maria și Moldovan Cosmina-Crina

Disciplina: Practicǎ de specialitate,Proiect