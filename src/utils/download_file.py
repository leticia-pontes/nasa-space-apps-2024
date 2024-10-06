import requests

url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv'
response = requests.get(url)

# Write the content to a CSV file
with open('downloaded_file.csv', 'wb') as file:
    file.write(response.content)

print('CSV downloaded successfully!')