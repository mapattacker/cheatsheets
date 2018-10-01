from slackclient import SlackClient

# More here http://www.codingtricks.biz/slack-python-client-to-send-messages/
token = 'xxx'
slack_client = SlackClient(token)

# get list of channels & their ids
slack = slack_client.api_call("channels.list") 
print json.dumps(slack, indent=4)


# With channel id input
# send message to slack general channel
channel_id = ''
def send_message(channel_id, message): 
    
    slack_client.api_call("chat.postMessage", 
                          channel=channel_id, 
                          text=message, 
                          username='fbalert')

send_message(channel_id, message)


# delete all user sent messages
# https://medium.com/@jjerryhan/cleaning-all-messages-on-slack-channel-c46d71615c9a
# run in terminal

# verify
slack-cleaner --token="token-code" --message --channel general --user "*"
# execute delete all msgs
slack-cleaner --token="token-code" --message --channel general --user "*" --perform