import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["name"]["first"]
        user_gender = user_data["gender"]
        user_location = user_data["location"]["country"]
        return user_name, user_gender, user_location
    else:
        raise Exception("Failed to fetch user data.")
    
def main():
    try:
        username, gender, country = fetch_random_user_freeapi()
        print(f"Username: {username}\nGender: {gender}\nCountry: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()