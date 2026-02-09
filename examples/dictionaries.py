# Dictionaries example in Python


def main():
    number_of_apples = {"Juan": 5, "Maria": 3, "Carlos": 4}
    print(f"Number of apples for Juan: {number_of_apples['Juan']}")

    # If get method is not used here, it will raise a KeyError since "Alejandra" is not in the
    # dictionary. Using get allows us to provide a default value if the key is not found.
    print(f"Number of apples for Alejandra: {number_of_apples.get('Alejandra', 'Not found')}")

    regional_capitals = {
        "Metropolitana": "Santiago",
        "Valparaiso": "Valparaiso",
        "O'Higgins": "Rancagua",
        "Maule": "Talca",
    }
    print(f"RM Capital: {regional_capitals['Metropolitana']}")
    print(f"Arica y Parinacota Capital: {regional_capitals.get('Arica y Parinacota')}")  # None
    print(f"Magallanes Capital: {regional_capitals.get('Magallanes', 'Punta Arenas')}")  # Default

    regions = regional_capitals.keys()
    capitals = regional_capitals.values()
    print(f"Regions: {list(regions)}")
    print(f"Capitals: {list(capitals)}")

    for region, capital in regional_capitals.items():
        print(f"The capital of {region} is {capital}")


if __name__ == "__main__":
    main()
