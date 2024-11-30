import requests

api_url = "https://newsapi.org/v2/everything?q=Apple&from=2024-10-03&sortBy=popularity&apiKey=8081d528817b447499f06e2f6107f060"
response = requests.get(api_url)
print(response.status_code)
if (response.status_code == requests.codes.ok):
    print(str(response.content))

