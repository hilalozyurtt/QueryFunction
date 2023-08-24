from google.cloud import bigquery
import json

def query_bigquery(request):
    # Signs in to Google Cloud
    client = bigquery.Client() 

    # Prepare your query to pull data from BigQuery
    query = """
        SELECT title
        FROM `bigquery-public-data.bbc_news.fulltext`
        WHERE category = 'tech'
        LIMIT 50
    """

    query_job = client.query(query) # API request
    results = query_job.result() # Waits for query to finish

    print(results)

    # A dictionary is created to store the results in a JSON format
    data = []
    for row in results:
        data.append({"title":row.title})

    # Results are returned in JSON format
    json_data = json.dumps(data)
    
    # HTTP response is generated for Cloud Function
    headers = {'Content-Type': 'application/json'}
    return (json_data, 200, headers)