import streamlit as st
from rdflib import Graph

# Streamlit app
st.title("Book Ontology Viewer")

# Upload RDF file
uploaded_file = st.file_uploader("Upload an RDF file (e.g., book_ontology.rdf)", type=["rdf"])

if uploaded_file:
    # Load the RDF data
    g = Graph()
    g.parse(uploaded_file, format="xml")

    # Define a SPARQL query
    query = """
    PREFIX ns1: <http://schema.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

    SELECT ?book_name ?author_name
    WHERE {
        ?book rdf:type ns1:Book .
        ?book ns1:name ?book_name .
        ?book ns1:author ?author .
        ?author ns1:name ?author_name .
    }
    """

    # Execute the query
    results = g.query(query)

    # Display the results
    st.subheader("Query Results:")
    data = []
    for row in results:
        book_name = row.book_name
        author_name = row.author_name
        data.append({"Book Name": book_name, "Author Name": author_name})

    # Show results as a table
    st.write(data)

    # Optionally, allow download of results
    st.download_button(
        label="Download Results as CSV",
        data="\n".join([f"{item['Book Name']},{item['Author Name']}" for item in data]),
        file_name="query_results.csv",
        mime="text/csv"
    )
else:
    st.info("Please upload an RDF file to start.")

