import requests
import json

def get_company_info_by_name(name):
    url = "https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }
    data = json.dumps({"obchodniJmeno": name})
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        data = response.json()
        try:
            total_count = data['pocetCelkem']
            companies = data['ekonomickeSubjekty']
            return total_count, companies
        except KeyError:
            print("Nelze najít informace o subjektech.")
            return None
    else:
        print("Chyba při získávání dat z API.")
        return None

def main():
    name = input("Zadejte název subjektu: ")
    result = get_company_info_by_name(name)
    if result:
        total_count, companies = result
        print(f"Nalezeno subjektů: {total_count}")
        for company in companies:
            company_name = company.get('obchodniJmeno', 'N/A')
            company_ico = company.get('ico', 'N/A')
            print(f"{company_name}, {company_ico}")

if __name__ == "__main__":
    main()
