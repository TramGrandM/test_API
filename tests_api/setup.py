base_url = 'https://de-genki.genkimiru.jp'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9kZS1nZW5raS5nZW5raW1pcnUuanBcL2FwaVwvdjFcL2xvZ2luIiwiaWF0IjoxNzA1ODg2MzQzLCJleHAiOjE3MDg0NzgzNDMsIm5iZiI6MTcwNTg4NjM0MywianRpIjoiQ2VIRlIxWWZZNnpDSWtYMSIsInN1YiI6MjkzMywicHJ2IjoiYzhlZTFmYzg5ZTc3NWVjNGM3Mzg2NjdlNWJlMTdhNTkwYjZkNDBmYyJ9.2DFtA6NUULazkgtWoSFWe8DigCAZLTGmuLbSlh0YK28'
headers = {
    "token": f"{token}",
    "Content-Type": "application/json",
}


def process_response(response, error_messages):
    for error_code, error_message in error_messages.items():
        if error_code in response.text:
            print(error_message, response.text)
            return
    if response.status_code == 200:
        print("Response 200", response.json())
    else:
        print("Not found", response.json())
