from bs4 import BeautifulSoup
import json

# Load the HTML content
with open('./test.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(content, 'html.parser')

# Find all table rows
rows = soup.find_all('tr')

# Create a dictionary to hold the data
data = {}

# Loop through each row
for row in rows:
    # Get the label (key) and value from the row
    key = ' '.join(row.find('th', class_='table-label').text.split())
    value = ' '.join(row.find('td').text.split())

    # Add the key-value pair to the dictionary
    data[key] = value

# Convert the dictionary to a JSON string
json_data = json.dumps(data, ensure_ascii=False)

# Print the JSON string
print(json_data)