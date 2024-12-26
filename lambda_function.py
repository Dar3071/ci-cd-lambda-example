import requests

def lambda_handler(event, context):
    url = "https://programming-quotes-api.herokuapp.com/quotes/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get("en")  # The quote text is stored in 'en'
        author = quote_data.get("author")  # The author is stored in 'author'
        print(f"Random Quote: '{content}' - {author}")
    else:
        print(f"Failed to retrieve a random quote., Status code: {response.status_code}")
