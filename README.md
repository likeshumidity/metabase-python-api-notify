# Metabase Python with Notify API

## Dependencies
- [poetry](https://python-poetry.org/)
- Must set [MB_API_KEY](https://www.metabase.com/docs/latest/configuring-metabase/environment-variables#mb_api_key) to use Notify API


## Installation
- `$ poetry install`
- Copy `env.sample` to `.env` or set environment variables


## Usage

### Getting a Session Token (not required for Notify API)
- requires environment variables
    - METABASE_USER
    - METABASE_PASS
    - METABASE_URL

`$ ./metabase-python-api-notify.py create_session_token`

- or to store in environment variable

`$ METABASE_SESSION_TOKEN=./metabase-python-api-notify.py create_session_token`

### Listing databases
- requires environment variables
    - METABASE_URL
- requires session token to be passed as an argument

`$ ./metabase-python-api-notify.py $METABASE_SESSION_TOKEN`

- response will be JSON list of databases and database attributes

### Using Metabase Notify API
- requires environment variables
    - METABASE_URL
    - MB_API_KEY
- requires argument
    - database_id - should be integer
- optional parameters
    - table_id - should be integer (cannot use with table_name)
    - table_name - should be string (cannot use with table_id)
    - scan_type - should be string (either `full` or `schema`)

- Format
    - `$ ./metabase-python-api-notify.py database_id table_id=table_id table_name=table_name scan_type=scan_type`
- Example: rescan database 15
    - `$ ./metabase-python-api-notify.py 15`
- Example: rescan database 15 table 41
    - `$ ./metabase-python-api-notify.py 15 table_id=41`
- Example: rescan database 15 table abc_123
    - `$ ./metabase-python-api-notify.py 15 table_name=abc_123`
- Example: rescan database 15 full
    - `$ ./metabase-python-api-notify.py 15 scan_type=full`

