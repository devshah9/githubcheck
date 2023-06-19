import requests


def get_friends_list():
    from config import synthica_api_url

    url = synthica_api_url + "v1/ai_friends"

    res = requests.get(url)
    data = res.json()

    new_data = {}

    for d in data:
        new_data[str(d['id'])] = d
        del new_data[str(d['id'])]['id']

    return new_data


def welcome_message(chat_mode):
    return f"Hi, I'm <b>{chat_mode['name']}, {'an' if chat_mode['occupation'][0].lower() in ['a', 'e', 'i', 'o', 'u'] else 'a'} {chat_mode['occupation']}</b>. How can I help you?"


def show_friend_profile(chat_mode):
    from config import synthica_api_url

    image_url = synthica_api_url + "storage/" + chat_mode.get('profile_image')

    name = chat_mode.get("name")
    occupation = chat_mode.get("occupation")
    age = str(chat_mode.get('age'))
    hair = chat_mode.get('hair')
    eyes = chat_mode.get('eyes')
    height = str(chat_mode.get('height'))
    site_profile = chat_mode.get('site_profile').split("\n")[0]

    # profile = f'<a href="{image_url}"></a>\n'
    profile = f"{occupation}\n\n"
    profile += f"<b>{name}</b>\n"
    profile += f"{age} years old\n"
    profile += f"{hair} Hair, {eyes} Eyes, {height}cm Tall\n\n"
    profile += site_profile

    return image_url, profile
