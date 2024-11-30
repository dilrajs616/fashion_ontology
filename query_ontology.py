from rdflib import Graph

# Load the RDF file
rdf_file = "laptop_ontology.rdf"

# Create an RDF graph
g = Graph()
g.parse(rdf_file, format="xml")

# Define a SPARQL query
query = """
PREFIX ns1: <http://example.org/fashion/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?name ?price ?color
WHERE {
    ?product rdf:type ns1:Product .
    ?product ns1:name ?name .
    ?product ns1:price ?price .
    OPTIONAL { ?product ns1:color ?color }
}
"""

# Execute the query
results = g.query(query)

# Print the results
print("Products:")
for row in results:
    name = row.name
    price = row.price
    color = row.color if row.color else "N/A"
    print(f"Name: {name}, Price: {price}, Color: {color}")


