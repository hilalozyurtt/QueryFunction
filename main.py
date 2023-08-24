from google.cloud import bigquery
import json

def query_bigquery(request):
    client = bigquery.Client()

    query = """
        SELECT title
        FROM `bigquery-public-data.bbc_news.fulltext`
        WHERE category = 'tech'
        LIMIT 50
    """

    query_job = client.query(query)
    results = query_job.result()

    print(results)

    data = []
    for row in results:
        data.append({"title":row.title})

    json_data = json.dumps(data)
    
    headers = {'Content-Type': 'application/json'}
    return (json_data, 200, headers)