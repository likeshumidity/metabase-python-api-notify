#!/usr/bin/env python

import os
import requests

import fire

from dotenv import load_dotenv

# Load .env file if exists
load_dotenv()


def create_session_token():
    """Creates a session token. Requires environment variables or .env file:
        METABASE_USER, METABASE_PASS, and METABASE_URL.
        """
    metabase_url = os.getenv('METABASE_URL')

    url = f'{metabase_url}/api/session'

    response = requests.post(
        url,
        json={
            'username': os.getenv('METABASE_USER'),
            'password': os.getenv('METABASE_PASS'),
        },
    )

    return response.json()['id']


def list_databases(session_token):
    """Calls GET /api/database/ to get a list of databases. Requires
        session_token argument and environment variables or .env file for:
        METABASE_USER, METABASE_PASS, and METABASE_URL.
        """
    metabase_url = os.getenv('METABASE_URL')

    url = f'{metabase_url}/api/database/'

    response = requests.get(
        url,
        headers={
            'X-Metabase-Session': session_token,
        },
    )

    return response.json()['data']


# re: https://www.metabase.com/docs/latest/api/notify
def notify_rescan_db(database_id, *args, table_id=None, table_name=None, scan_type=None):
    """Notifies Metabase of potential schema change. Requires database_id
        argument and environment variables METABASE_URL, MB_API_TOKEN.
        Optionally accepts table_id, table_name, and scan_type.
        """
    metabase_url = os.getenv('METABASE_URL')

    url = f'{metabase_url}/api/notify/db/{database_id}'

    request_data = {}

    if table_id:
        request_data['table_id'] = table_id

    if table_name:
        request_data['table_name'] = table_name

    if scan_type:
        request_data['scan'] = scan_type

    response = requests.post(
        url,
        headers={
            'X-Metabase-Apikey': os.getenv('MB_API_KEY'),
        },
        json=request_data,
    )

    return response.json()


if __name__ == '__main__':
    fire.Fire({
        'create_session_token': create_session_token,
        'list_databases': list_databases,
        'notify_rescan_db': notify_rescan_db,
    })
