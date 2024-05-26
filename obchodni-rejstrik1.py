import requests

def get_company_info(ico):
    url = f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        try:
            company_name = data['obchodniJmeno']
            address = data['sidlo']['textovaAdresa']
            return company_name, address
        except KeyError:
            print("Nelze najít informace o subjektu.")
            return None
    else:
        print("Chyba při získávání dat z API.")
        return None

def main():
    ico = input("Zadejte IČO subjektu: ")
    result = get_company_info(ico)
    if result:
        company_name, address = result
        print(company_name)
        print(address)

if __name__ == "__main__":
    main()
