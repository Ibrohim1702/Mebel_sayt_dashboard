import json

import requests as re

import requests
import json

from contextlib import closing

from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return []
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def all_category():
    sql = """
        select * from milner_category 

    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)

        return data


def search_recipe(s):
    sql = f"""
        select * from milner_recipe 
        where  lower("name") like lower('%{s}%') 

    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        data = dictfetchall(cursor)

    return data


def edit_profile(data, token):

    url = "http://127.0.0.1:8000/api/v1/dashboard/user/"

    payload = json.dumps(data)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = re.request("PUT", url, headers=headers, data=payload)

    return response.json()


