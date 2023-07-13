import requests as re
url = "http://127.0.0.1:8000/api/v1/mebel_sayt/prod"


def get_list(token, pk=None, page=1):

    url = "http://127.0.0.1:8000/api/v1/mebel_sayt/prod"
    if pk:
        url += f"{pk}/"
    else:
        url += f"?page={page}"

    payload = ""
    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = re.request("GET", url, headers=headers, data=payload)

    return response.json()
