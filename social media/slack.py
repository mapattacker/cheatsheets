# https://slack.dev/python-slackclient/index.html

import slack

token = 'xoxp-'
client = slack.WebClient(token=token)

# list channel name & id
channels = client.channels_list()
for i in channels['channels']:
    print(i['name'], i['id'])

# list user names & id
clients = client.users_list()
for i in clients['members']:
    print(i['id'], i['team_id'], i['name'], i['real_name'])


# Post Messages
client.chat_postMessage(
    channel="U010PDDAR0F",
    text="Hello from your app! :tada:"
)

