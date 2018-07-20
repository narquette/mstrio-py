import requests


def create_dataset(connection, json_body, verbose=False):
    """
    Create a structured dataset with external data uploaded to the MicroStrategy Intelligence Server.

    :param connection: MicroStrategy REST API connection object
    :param json_body: JSON-formatted definition of the dataset. Generated by utils.formjson().
    :param verbose: Verbosity of request response; defaults to False
    :return: Complete HTTP response object
    """

    # check connection object
    if not hasattr(connection, 'auth_token'):
        print("Error: connection object does not contain 'auth_token'")
    if not hasattr(connection, 'base_url'):
        print("Error: connection object does not contain 'base_url'")
    if not hasattr(connection, 'cookies'):
        print("Error: connection object does not contain 'cookies'")
    if not hasattr(connection, 'project_id'):
        print("Error: connection object does not contain 'project_id'")

    response = requests.post(url=connection.base_url + '/datasets',
                             headers={'X-MSTR-AuthToken': connection.auth_token,
                                      'X-MSTR-ProjectID': connection.project_id},
                             cookies=connection.cookies,
                             json=json_body,
                             verify=connection.ssl_verify)

    if verbose:
        print(response.url)
    return response


def update_dataset(connection, dataset_id, table_name, update_policy, json_body, verbose=False, table_id=None):
    """
    Update a structured dataset with external data uploaded to the MicroStrategy Intelligence Server.

    :param connection: MicroStrategy REST API connection object
    :param dataset_id: Identifier of the MicroStrategy dataset.
    :param table_id: Identifier of the table to update within the MicroStrategy dataset.
    :param update_policy: Update operation type: 'Add' (inserts new, unique rows), 'Update' (updates data in existing
    rows and columns), 'Upsert' (updates existing data and inserts new rows), 'Replace' (similar to truncate and load,
    replaces the existing data with new data).
    :param json_body: JSON-formatted definition of the dataset. Generated by utils.formjson().
    :param verbose: Verbosity of request response; defaults to False
    :return: Complete HTTP response object
    """

    # check connection object
    if not hasattr(connection, 'auth_token'):
        print("Error: connection object does not contain 'auth_token'")
    if not hasattr(connection, 'base_url'):
        print("Error: connection object does not contain 'base_url'")
    if not hasattr(connection, 'cookies'):
        print("Error: connection object does not contain 'cookies'")
    if not hasattr(connection, 'project_id'):
        print("Error: connection object does not contain 'project_id'")

    response = requests.patch(url=connection.base_url + '/datasets/' + dataset_id + '/tables/' + table_name,
                              headers={'X-MSTR-AuthToken': connection.auth_token,
                                       'X-MSTR-ProjectID': connection.project_id,
                                       'updatePolicy': update_policy},
                              cookies=connection.cookies,
                              json=json_body,
                              verify=connection.ssl_verify)
    if verbose:
        print(response.url)
    return response