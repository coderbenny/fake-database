import requests

url = "https://flagsapi.com/api/v1/flags?lang=en"
response = requests.get(url)
data = response.json()

# Now, you can update the JSON file with the actual flag links
for country in your_json_data["countries"]:
    country_name = country["name"]
    flag_link = data.get(country_name, {}).get("flag")
    country["flag_link"] = flag_link

# Save the updated JSON data to a file
with open("countries_data.json", "w") as json_file:
    json.dump(your_json_data, json_file, indent=2)
