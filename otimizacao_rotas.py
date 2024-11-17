import networkx as nx
import matplotlib.pyplot as plt
import random

graph = nx.Graph()

locations = {
    "Warehouse": (0, 0),
    "Client A": (1, 2),
    "Client B": (3, 1),
    "Client C": (4, 3),
    "Client D": (5, 0),
    "Client E": (2, 4)
}

for location, coords in locations.items():
    graph.add_node(location, pos=coords)

edges = [
    ("Warehouse", "Client A", 2.5),
    ("Warehouse", "Client B", 4.0),
    ("Warehouse", "Client E", 3.5),
    ("Client A", "Client B", 1.5),
    ("Client A", "Client C", 3.0),
    ("Client B", "Client D", 2.0),
    ("Client C", "Client D", 2.5),
    ("Client E", "Client C", 2.0)
]

for edge in edges:
    graph.add_edge(edge[0], edge[1], weight=edge[2])

# Horários de entrega
delivery_windows = {
    "Client A": (8, 12),
    "Client B": (9, 13),
    "Client C": (10, 14),
    "Client D": (11, 15),
    "Client E": (7, 11)
}

# Pesos das entregas
delivery_weights = {
    "Client A": 3,
    "Client B": 4,
    "Client C": 2,
    "Client D": 5,
    "Client E": 3
}

vehicle_capacities = {"Vehicle 1": 8, "Vehicle 2": 10}

def calculate_total_distance(route, graph):
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += graph[route[i]][route[i+1]]["weight"]
    return total_distance

def initial_solution(delivery_weights, vehicle_capacities):
    return assign_deliveries(delivery_weights, vehicle_capacities)

def local_search_optimization(assignments, graph):
    best_assignments = assignments
    best_distance = calculate_total_distance_for_all_vehicles(assignments, graph)

    for _ in range(100):  
        vehicles = list(assignments.keys())
        vehicle1, vehicle2 = random.sample(vehicles, 2)

        new_assignments = best_assignments.copy()
        client1 = random.choice(new_assignments[vehicle1])
        client2 = random.choice(new_assignments[vehicle2])

        new_assignments[vehicle1].remove(client1)
        new_assignments[vehicle2].remove(client2)
        new_assignments[vehicle1].append(client2)
        new_assignments[vehicle2].append(client1)

        if is_valid_assignment(new_assignments, vehicle_capacities):
            new_distance = calculate_total_distance_for_all_vehicles(new_assignments, graph)
            if new_distance < best_distance:
                best_distance = new_distance
                best_assignments = new_assignments

    return best_assignments

def calculate_total_distance_for_all_vehicles(assignments, graph):
    total_distance = 0
    for vehicle, clients in assignments.items():
        if clients:
            nodes = ["Warehouse"] + clients + ["Warehouse"]
            route = nx.dijkstra_path(graph.subgraph(nodes), source="Warehouse", target="Warehouse", weight="weight")
            total_distance += calculate_total_distance(route, graph)
    return total_distance

def is_valid_assignment(assignments, vehicle_capacities):
    for vehicle, clients in assignments.items():
        total_weight = sum(delivery_weights[client] for client in clients)
        if total_weight > vehicle_capacities[vehicle]:
            return False
    return True

def assign_deliveries(delivery_weights, vehicle_capacities):
    assignments = {vehicle: [] for vehicle in vehicle_capacities}
    sorted_deliveries = sorted(delivery_weights.items(), key=lambda x: -x[1])  # Ordenar por peso

    for client, weight in sorted_deliveries:
        for vehicle, capacity in vehicle_capacities.items():
            if sum(delivery_weights[c] for c in assignments[vehicle]) + weight <= capacity:
                assignments[vehicle].append(client)
                break

    return assignments

initial_assignments = initial_solution(delivery_weights, vehicle_capacities)
optimized_assignments = local_search_optimization(initial_assignments, graph)

print("Solução Inicial:")
for vehicle, clients in initial_assignments.items():
    print(f"{vehicle}: {clients}")

print("\nSolução Otimizada:")
for vehicle, clients in optimized_assignments.items():
    print(f"{vehicle}: {clients}")

initial_distance = calculate_total_distance_for_all_vehicles(initial_assignments, graph)
optimized_distance = calculate_total_distance_for_all_vehicles(optimized_assignments, graph)

print(f"\nDistância total inicial: {initial_distance}")
print(f"Distância total otimizada: {optimized_distance}")

pos = nx.get_node_attributes(graph, 'pos')
nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10)
labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

for vehicle, clients in optimized_assignments.items():
    if clients:
        nodes = ["Warehouse"] + clients + ["Warehouse"]
        route = nx.dijkstra_path(graph.subgraph(nodes), source="Warehouse", target="Warehouse", weight="weight")
        nx.draw_networkx_edges(
            graph, pos, edgelist=list(zip(route[:-1], route[1:])), width=2.5, edge_color="red"
        )

plt.show()
