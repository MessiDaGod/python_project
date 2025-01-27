import requests

def decode_google_doc(url):
    # Step 1: Fetch the content from the Google Docs URL
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch the document.")

    # Debug: Check the content of the response
    print(response.text)

    # Step 2: Parse the content to extract the input data
    rows = response.text.splitlines()
    data = []
    for row in rows:
        parts = row.split()
        # Ensure the row has at least 3 parts and the first and third parts are integers
        if len(parts) >= 3 and parts[0].isdigit() and parts[2].isdigit():
            x, char, y = parts[:3]
            data.append((int(x), char, int(y)))

    # Handle the case where no valid data was found
    if not data:
        raise Exception("No valid data found in the document. Please check the input format.")

    # Step 3: Determine grid size
    max_x = max(item[0] for item in data)
    max_y = max(item[2] for item in data)

    # Step 4: Create a grid and populate it with characters
    grid = [[" " for _ in range(max_y + 1)] for _ in range(max_x + 1)]
    for x, char, y in data:
        grid[x][y] = char

    # Step 5: Print the grid
    for row in grid:
        print("".join(row))

# Usage
decode_google_doc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
