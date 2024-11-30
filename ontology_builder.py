from rdflib import Graph, Literal, RDF, URIRef, Namespace
import json

# Define the namespace
FASHION = Namespace("http://example.org/fashion/")

# Initialize the graph
g = Graph()

# Load enriched data
with open("enriched_data.json") as f:
    products = json.load(f)

# Populate the graph
for product in products:
    product_uri = URIRef(FASHION[product["name"].replace(" ", "_")])
    g.add((product_uri, RDF.type, FASHION.Product))
    g.add((product_uri, FASHION.name, Literal(product["name"])))
    g.add((product_uri, FASHION.price, Literal(product["price"])))
    
    for feature, values in product.get("features", {}).items():
        for value in values:
            g.add((product_uri, FASHION[feature], Literal(value)))

# Save the graph in RDF/XML format
g.serialize("laptop_ontology.rdf", format="xml")

