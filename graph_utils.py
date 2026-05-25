# importam osmnx pentru descarcarea hartii
import osmnx as ox


# functie care incarca reteaua de drumuri
def load_graph():

    # incarcam toate drumurile din Maramures
    # "all" include si drumuri agricole
    G = ox.graph_from_place(
        "Maramures, Romania",
        network_type="all"
    )

    # parcurgem toate muchiile din graf
    for u, v, d in G.edges(data=True):

        # extragem tipul drumului
        tip = d.get("highway")

        # uneori tipul este lista
        if isinstance(tip, list):
            tip = tip[0]

        # lungimea drumului in metri
        lungime = d.get("length", 1)

        # drum agricol
        if tip == "track":
            d["weight"] = lungime * 0.5

        # drum forestier
        elif tip == "service":
            d["weight"] = lungime * 0.8

        # drum local
        elif tip in ["residential", "unclassified", "tertiary"]:
            d["weight"] = lungime * 1.2

        # drum judetean
        elif tip == "secondary":
            d["weight"] = lungime * 2

        # drum national
        elif tip == "primary":
            d["weight"] = lungime * 3

        # autostrada
        elif tip == "motorway":
            d["weight"] = lungime * 10

        # orice alt drum
        else:
            d["weight"] = lungime * 2

    return G