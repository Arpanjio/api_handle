import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()


    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        user_pass = user_data["login"]["password"]
        country = user_data["location"]["country"]

        return username,user_pass,country

    else:
        raise Exception("Failed to fetch api data")


def main():
    try:
        username, user_pass,country = fetch_random_user_freeapi()

        print(f"username:{username} \nPassword:{user_pass} \nCountry:{country}")
    except Exception as ex:
        print(str(ex))

if __name__ == "__main__":
    main()