import re
import json

# Define users outside the handler to take advantage of Lambda container reuse
USERS = {
    "john_doe": "password123",
    "jane_smith": "securePass456"
}

def validate_login(username, password):
    return username in USERS and USERS[username] == password

def validate_username(username):
    if not username:
        return False
    if not re.match("^[a-zA-Z0-9_]{3,20}$", username):
        return False
    return True



def lambda_handler(event, context):
    # Parse input from the event
    body = json.loads(event['body']) if isinstance(event.get('body'), str) else event.get('body', {})
    username = body.get('username', '')
    password = body.get('password', '')

    # Validate input
    if not validate_username(username) or not validate_password(password):
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Invalid username or password format.'})
        }

    # Attempt login
    if validate_login(username, password):
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Login successful!'})
        }
    else:
        return {
            'statusCode': 401,
            'body': json.dumps({'message': 'Invalid credentials.'})
        }

# For local testing (will not be executed in Lambda)
if __name__ == '__main__':
    # Simulate a Lambda event
    test_event = {
        'body': json.dumps({
            'username': 'john_doe',
            'password': 'password123'
        })
    }
    print(lambda_handler(test_event, None))
