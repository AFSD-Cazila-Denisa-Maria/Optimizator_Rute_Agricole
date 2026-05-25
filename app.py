# importam Flask
from flask import Flask, render_template, request, jsonify

# importam harta
from graph_utils import load_graph

# importam algoritmul TSP
from tsp_solver import calculeaza_ruta_tsp

# importam osmnx
import osmnx as ox

# initializam aplicatia
app = Flask(__name__)

# incarcam harta la pornire
G = load_graph()


# pagina principala
@app.route("/")
def index():
    return render_template("index.html")


# calcul ruta
@app.route("/route", methods=["POST"])
def route():

    # citim datele trimise din browser
    data = request.json

    # punctul de start
    start = (
        data["start"]["lat"],
        data["start"]["lng"]
    )

    # punctele de lucru
    puncte_lucru = []

    for p in data["work_points"]:

        puncte_lucru.append(
            (
                p["lat"],
                p["lng"]
            )
        )

    try:

        # calculam ruta optima
        ruta, ordine, distanta = calculeaza_ruta_tsp(
            G,
            start,
            puncte_lucru
        )

        # convertim nodurile in coordonate
        coords = []

        for n in ruta:

            coords.append(
                (
                    G.nodes[n]["y"],
                    G.nodes[n]["x"]
                )
            )

        # convertim ordinea pentru afisare
        ordine_afisare = []

        for p in ordine:

            ordine_afisare.append(
                {
                    "lat": p[0],
                    "lng": p[1]
                }
            )

        # viteza medie utilaj
        viteza = 35

        timp = (
            distanta / 1000
        ) / viteza

        return jsonify(
            {
                "route": coords,
                "distance": round(
                    distanta / 1000,
                    2
                ),
                "time": round(
                    timp,
                    2
                ),
                "order": ordine_afisare
            }
        )

    except Exception as e:

        print(e)

        return jsonify(
            {
                "route": [],
                "distance": 0,
                "time": 0,
                "order": [],
                "error": str(e)
            }
        )


# pornim serverul
if __name__ == "__main__":
    app.run(
        debug=True
    )