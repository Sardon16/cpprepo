import requests

def send_webex_message(token, room_id, message):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "roomId": room_id,
        "text": message
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.status_code

# Replace with your actual Webex API token, room ID, and message
token = "MmU3ZmQ0NDktOTkwNC00NWYzLWFiZDEtN2M0NGNjODY4MWY3MjE2ODA2Y2YtNjhl_P0A1_0c26c4a4-350e-4307-88fc-8674f5159bbe"
room_id = "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vZGQ0OTViZDAtYTE1MS0xMWVmLWIyYTQtODkzZDdmODMxZmYx"
message = "Build completed successfully!"

status = send_webex_message(token, room_id, message)
print(f"Message sent with status code: {status}")