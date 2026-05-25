# importam itertools pentru generarea permutarilor
import itertools

# importam networkx pentru algoritmii pe graf
import networkx as nx

# importam osmnx pentru identificarea nodurilor
import osmnx as ox


# functie care calculeaza distanta dintre doua puncte
def distanta(G, p1, p2):

    # transformam primul punct in nod
    n1 = ox.distance.nearest_nodes(
        G,
        p1[1],
        p1[0]
    )

    # transformam al doilea punct in nod
    n2 = ox.distance.nearest_nodes(
        G,
        p2[1],
        p2[0]
    )

    # calculam distanta minima dintre noduri
    return nx.shortest_path_length(
        G,
        n1,
        n2,
        weight="weight"
    )


# functie care determina ordinea optima de vizitare
def tsp(G, start, puncte_lucru):

    # cea mai buna ordine
    cea_mai_buna_ordine = None

    # distanta minima
    distanta_minima = float("inf")

    # generam toate permutarile punctelor
    for perm in itertools.permutations(puncte_lucru):

        # construim traseul complet
        traseu = [start] + list(perm)

        # distanta traseului
        total = 0

        # calculam costul traseului
        for i in range(len(traseu) - 1):

            total += distanta(
                G,
                traseu[i],
                traseu[i + 1]
            )

        # verificam daca este mai bun
        if total < distanta_minima:

            distanta_minima = total

            cea_mai_buna_ordine = traseu

    return cea_mai_buna_ordine, distanta_minima


# functie care construieste ruta finala
def construieste_ruta(G, ordine):

    # lista cu nodurile rutei finale
    ruta_finala = []

    # parcurgem punctele
    for i in range(len(ordine) - 1):

        # nodul de start
        n1 = ox.distance.nearest_nodes(
            G,
            ordine[i][1],
            ordine[i][0]
        )

        # nodul destinatie
        n2 = ox.distance.nearest_nodes(
            G,
            ordine[i + 1][1],
            ordine[i + 1][0]
        )

        # calculam segmentul optim
        segment = nx.shortest_path(
            G,
            n1,
            n2,
            weight="weight"
        )

        # adaugam segmentul la ruta
        ruta_finala.extend(segment)

    return ruta_finala


# functie principala folosita de aplicatie
def calculeaza_ruta_tsp(G, start, puncte_lucru):

    # obtinem ordinea optima
    ordine, distanta_totala = tsp(
        G,
        start,
        puncte_lucru
    )

    # construim ruta finala
    ruta = construieste_ruta(
        G,
        ordine
    )

    return (
        ruta,
        ordine,
        distanta_totala
    )