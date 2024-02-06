from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('amazon_page.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Find elements containing the data you want to extract
# Example: find all product titles
titles = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')

# Extract data and store it in a list of dictionaries
data = []
for title in titles:
    product_name = title.text.strip()
    # Find the parent element of the title, which contains the price
    parent = title.find_parent('div', class_='sg-col-inner')
    # Find the price within the parent element
    price_element = parent.find('span', class_='a-offscreen')
    # Extract the price text
    price = price_element.text.strip() if price_element else 'Price not found'
    data.append({
        'Title': product_name,
        'Price': price
    })

# Create DataFrame from the data
df = pd.DataFrame(data)

# Save DataFrame to Excel
df.to_excel('amazon_data.xlsx', index=False)
