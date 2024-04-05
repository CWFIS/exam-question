
import requests
import statistics

def fetch_population_data():
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
if response.status_code == 200:
data = response.json()
return data
else:
print("Failed to fetch data from API")
return None

def calculate_population_density(country):
area = country.get("area", 1) # default to 1 if area is missing
population = country.get("population", 0)
return population / area

def main():
data = fetch_population_data()
if data:
population_densities = []
un_members_count = 0
euro_users_count = 0

for country_data in data:
country_name = country_data.get("name", "N/A")
population_density = calculate_population_density(country_data)
population_densities.append(population_density)

if country_data.get("unMember", False):
un_members_count += 1

if "eur" in country_data.get("currencies", {}):
euro_users_count += 1

print(f"Country: {country_name}, Population Density: {population_density}")

mean_density = statistics.mean(population_densities)
median_density = statistics.median(population_densities)
std_dev_density = statistics.stdev(population_densities)

print("\nPopulation Density Statistics:")
print(f"Mean: {mean_density}")
print(f"Median: {median_density}")
print(f"Standard Deviation: {std_dev_density}")

print("\nNumber of UN Members:", un_members_count)
print("Number of Euro Users:", euro_users_count)


if __name__ == "__main__":
main()

