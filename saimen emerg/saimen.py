import requests

# Base URL for the Webex API
API_BASE_URL = 'https://webexapis.com/v1'

# Function to test the connection to Webex
def connection_test(access_token):
    try:
        url = f'{API_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        print("Connection test to Webex successful!")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Function to display user information
def display_user_info(access_token):
    try:
        url = f'{API_BASE_URL}/people/me'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        user_data = response.json()
        print("Display Name : " + user_data["displayName"])
        print("Nickname : " + user_data["nickName"])
        print("Email : " + user_data["emails"][0]) 
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Function to list the rooms
def list_rooms(access_token):
    try:
        url = f'{API_BASE_URL}/rooms'
        headers = {'Authorization' : f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()
            
        rooms = response.json()['items'][:6] 
        for room in rooms: 
            print("Room ID : " + room["id"])
            print("Room Title : " + room["title"])
            print("Date Created : " + room["created"])
            print("Last Activity : " + room["lastActivity"])
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Function to create a room
def create_room(access_token):
    try:
        url = f'{API_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
        room_title = input("Enter room title: ")
        data = {'title': room_title}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Room created successfully!")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Function to send a message to a room
def send_message(access_token):
    try:
        url = f'{API_BASE_URL}/rooms'
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        rooms = response.json()['items']  
        for i, room in enumerate(rooms, start=1):
            print(f"{i}. {room['title']}")

        room_number = int(input("Choose room: "))
        message = input("Enter the message: ")

        selected_room_id = rooms[room_number - 1]['id']
        url = f'{API_BASE_URL}/messages'
        headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
        data = {'roomId': selected_room_id, 'text': message}
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        print("Message sent successfully!")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

# Main function
def main():
    print("Welcome To WEBEX Troubleshoot Tool")
    access_token = input("Enter your Webex Access Token: ").strip()
    connection_test(access_token)
    
    while True:
        print("\n1. Display user information")
        print("2. List of rooms")
        print("3. Create a room")
        print("4. Send message to a room")
        print("5. Exit")

        option = int(input(">>: ")) 
        if option == 1:
            display_user_info(access_token)
        elif option == 2:
            list_rooms(access_token)
        elif option == 3:
            create_room(access_token)
        elif option == 4:
            send_message(access_token)
        elif option == 5:
            print("Thank you for choosing us. Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()