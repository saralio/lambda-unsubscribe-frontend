import os
from jinja2 import Environment, FileSystemLoader
from saral_utils.utils.frontend import ShareLinks
from saral_utils.utils.env import create_env_api_url

def serve_html(event, context):
    email_id = event['pathParameters']['email_id']

    print(f'unsubscribing for {email_id}')

    sl = ShareLinks()
    twitter_account_link = sl.twitter_account_link
    navbar_links = {'twitter_account_link': twitter_account_link}
    url = create_env_api_url(url='remove-db.saral.club/unsubscribe?')
    unsub_data = {
        'email_id': email_id,
        'url': url,
        'navbar_links': navbar_links
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
