import streamlit as st
from rdflib import Graph

# Streamlit app
st.title("Laptop Ontology Viewer")

# Upload RDF file
uploaded_file = st.file_uploader("Upload an RDF file (e.g., laptop_ontology.rdf)", type=["rdf"])

if uploaded_file:
    # Load the RDF data
    g = Graph()
    g.parse(uploaded_file, format="xml")

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

    # Display the results
    st.subheader("Query Results:")
    data = []
    for row in results:
        name = row.name
        price = row.price
        color = row.color if row.color else "N/A"
        data.append({"Name": name, "Price": price, "Color": color})

    # Show results as a table
    st.write(data)

    # Optionally, allow download of results
    st.download_button(
        label="Download Results as CSV",
        data="\n".join([f"{item['Name']},{item['Price']},{item['Color']}" for item in data]),
        file_name="query_results.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload an RDF file to start.")

