from graph import Vertix, Edge, Graph, Queue
def business_trip(graph, city_names):
    if 

# Example graph setup
if __name__ == "__main__":
    g = Graph()
    metroville = g.add_vertix('Metroville')
    pandora = g.add_vertix('Pandora')
    arendelle = g.add_vertix('Arendelle')
    new_monstropolis = g.add_vertix('New Monstropolis')
    naboo = g.add_vertix('Naboo')
    narnia = g.add_vertix('Narnia')

    g.add_edge(metroville, pandora, 82)
    g.add_edge(arendelle, new_monstropolis, 115)
    g.add_edge(naboo, pandora)
    g.add_edge(narnia, arendelle)

    test_cases = [
        [metroville, pandora],  # Expected output: $82
        [arendelle, new_monstropolis, naboo],  # Expected output: $115
        [naboo, pandora],  # Expected output: null
        [narnia, arendelle, naboo]  # Expected output: null
    ]
    
    for cities in test_cases:
        result = business_trip(g, cities)
        print(f"{cities}: {result}")