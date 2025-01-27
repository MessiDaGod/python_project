import requests
from bs4 import BeautifulSoup

def decode_google_doc(url):
    # Step 1: Fetch the content from the Google Docs URL
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the document.")

    # Step 2: Save the content to a file for debugging
    with open("response.html", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Response saved to response.html")

    # Step 3: Extract the <table> element from the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        raise Exception("No <table> found in the HTML document.")

    # Save the extracted table for debugging
    with open("extracted_table.html", "w", encoding="utf-8") as file:
        file.write(str(table))
    print("Table extracted and saved to extracted_table.html")

    # Step 4: Extract rows and process the table data
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cells = row.find_all('td')
        if len(cells) >= 3:  # Ensure there are enough cells
            try:
                x = int(cells[0].text.strip())
                char = cells[1].text.strip()
                y = int(cells[2].text.strip())
                data.append((x, char, y))
            except ValueError:
                # Skip rows with invalid data
                continue

    # Handle the case where no valid data was found
    if not data:
        raise Exception("No valid data found in the table. Please check the input format.")

    # Step 5: Determine grid size
    max_x = max(item[0] for item in data)
    max_y = max(item[2] for item in data)

    # Step 6: Create a grid and populate it with characters
    grid = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    for x, char, y in data:
        grid[x][y] = char

    # Step 7: Print the grid
    print("\nDecoded Grid:")
    for row in grid:
        print("".join(row))

# Usage
decode_google_doc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
