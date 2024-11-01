from flask import Flask, request, jsonify
from tavily import TavilyClient

app = Flask(__name__)

# Initialize the Tavily client with your API key
client = TavilyClient(api_key="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")

@app.route('/search', methods=['POST'])
def search():
    # Get the JSON data from the request
    data = request.json
    query = data.get('query','latest news')  # Expecting the query to be in the request body

    # Predefined parameters
    search_depth = "advanced"
    include_images = True
    include_answer = True
    include_raw_content = True
    max_results = 10

    # Check if query is provided
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Perform the search using the Tavily API
    try:
        response = client.search(
            query,
            search_depth=search_depth,
            include_images=include_images,
            include_answer=include_answer,
            include_raw_content=include_raw_content,
            max_results=max_results
        )
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
