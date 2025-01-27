import re

def decode_google_doc(data):
    parsed_data = []
    lines = data.splitlines()

    for line in lines:
        match = re.search(r'(\d+)\s+(█|░)\s+(\d+)', line)
        if match:
            x, char, y = match.groups()
            parsed_data.append((int(x), char, int(y)))
        else:
            print(f"Skipping invalid line")

    if not parsed_data:
        raise ValueError("No valid data was parsed from the input.")

    max_x = max(item[0] for item in parsed_data)
    max_y = max(item[2] for item in parsed_data)
    print(f"Max values found: x={max_x}, y={max_y}")

    return parsed_data

# Example usage with file content
with open('response.txt', 'r') as file:
    content = file.read()

try:
    decoded_data = decode_google_doc(content)
    print("Decoded data:", decoded_data)
except ValueError as e:
    print("Error:", e)


# Usage
decode_google_doc("https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub")
