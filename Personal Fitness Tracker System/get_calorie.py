import requests

api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
def nutri_list(query):
    meal_list = []
    response = requests.get(api_url + query, headers={'X-Api-Key': '09Ppg3ZipoW1ZiAict0lQeODGCoytlBauAGZWD5G'})
    if response.status_code == requests.codes.ok:
       # print(response.text)
        calorie_json = response.json()
        try:
            meal = calorie_json["items"][0]["name"]
            calorie = calorie_json["items"][0]["calories"]
        except IndexError:
            return 'error'
        meal_list.append(meal)
        meal_list.append(calorie)
        return meal_list


    else:
        return "error"
    #    print("Error:", response.status_code, response.text)


