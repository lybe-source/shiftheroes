import requests
import time
import schedule

headers = {
    'Authorization': 'Bearer b9ef01cbdbd869cd616f730d179036ad',
}

# daily, weekly, permanent
planning_type_liste = ["daily"]

for planning_type in planning_type_liste:
    try:
        planning_initiale = requests.get(f'https://shiftheroes.fr/api/v1/plannings?type={planning_type}', headers=headers).json()
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la première requête récupérant les plannings : {e}")

    print(planning_initiale)

    for i in planning_initiale:
        planning_id = i['id']
        print(f"L'ID du planning initiale : {planning_id}")

    print("-" * 50)


def register_to_all_new_shift():
    # Récupérer la liste des plannings (3 plannings: daily, permanent, weekly)
    for planning_type in planning_type_liste:

        try:
            planning_initiale = requests.get(f'https://shiftheroes.fr/api/v1/plannings?type={planning_type}', headers=headers).json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la première requête récupérant les plannings : {e}")

        print(planning_initiale)

        for i in planning_initiale:
            planning_id = i['id']
            print(f"L'ID du planning initiale est toujours : {planning_id}")

        print("-" * 50)

        try:
            new_planning = requests.get(f'https://shiftheroes.fr/api/v1/plannings?type={planning_type}', headers=headers).json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la seconde requête récupérant les plannings : {e}")
            break
    
        if not new_planning:
            print("Le nouveau planning est vide ou invalide.")
            break
        

        while planning_initiale == new_planning:
            time.sleep(1)
            try:
                new_planning = requests.get(f'https://shiftheroes.fr/api/v1/plannings?type={planning_type}', headers=headers).json()
            except requests.exceptions.RequestException as e:
                print(f"Erreur lors de la troisième requête récupérant les plannings : {e}")

        print("✨" * 50)
        print("Nouveau planning disponible !")
        print("✨" * 50)


        for i in new_planning:
            planning_id = i['id']
            print(f"L'ID du nouveau planning : {planning_id}")

        print("-" * 50)

        # Récupérer les créneaux du planning
        try:
            response = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts', headers=headers).json()
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de la requête récupérant les créneaux dans les plannings : {e}")

        print(response)
        print("-" * 50)

        for i in response:
            shift_id = i['id']
            print(shift_id)

            try:
                response = requests.post(f'https://shiftheroes.fr/api/v1/plannings/{planning_id}/shifts/{shift_id}/reservations', headers=headers)
            except requests.exceptions.RequestException as e:
                print(f"Erreur lors de la requête permettant de s'enregister sur un créneau : {e}")

        print("Enregistrement effectué")
        print("-" * 50)

# schedule.every().saturday.at("09:59:45", "Europe/Amsterdam").do(register_to_all_new_shift)
schedule.every().day.at("17:59:45", "Europe/Amsterdam").do(register_to_all_new_shift)

while True:
    schedule.run_pending()
    time.sleep(1)