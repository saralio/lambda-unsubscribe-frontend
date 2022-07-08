import os
from jinja2 import Environment, FileSystemLoader


def create_env_api_url(url: str) -> str:
    """depending on the environment variable returns the api url. Attaches the environment variable at the beggining of api url e.g. `test-deregister.saral.club`. But for prod it's without env i.e. `deregister.saral.club`

    Args:
        url (str): URL string

    Returns:
        str: `test-deregister.saral.club` for test/stg environment and `deregister.saral.club` for prod environments
    """
    env = os.environ['MY_ENV']
    if env != 'prod':
        url = f'{env}-{url}'
    return url


def serve_html(event, context):
    email_id = event['pathParameters']['email_id']

    print(f'unsubscribing for {email_id}')
    env = os.environ['MY_ENV']

    url = f"{env}-deregister.saral.club/emailId/{email_id}"
    unsub_data = {
        'email_id': email_id,
        'url': url
    }

    jinja_env = Environment(loader=FileSystemLoader('.'))

    with open('./templates/template.html', 'r') as file:
        html_template = file.read()

    template = jinja_env.from_string(html_template)
    content = template.render(unsub_data=unsub_data)

    response = {
        "statusCode": 200,
        "body": content,
        "headers": {
            "Content-type": "text/html",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type",
            "Access-Control-Allow-Methods": 'Get'
        }
    }

    return response
