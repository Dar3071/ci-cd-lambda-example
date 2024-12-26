import requests

def lambda_handler(event, context):
    url = "https://zenquotes.io/api/random"  # Quote Url
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data[0].get("q")  # ZenQuotes stores the quote in 'q'
        author = quote_data[0].get("a")  # ZenQuotes stores the author in 'a'
        print(f"Random Quote: '{content}' - {author}")
    else:
        print(f"Failed to retrieve a random quote., Status code: {response.status_code}")
