import sys
import requests

def check_robot(url):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        response = requests.get(url + "/robots.txt")
        
        if response.status_code == 200:
            return response.text
        else:
            print(f"Error: /robots.txt not accessible. HTTP Error code {response.status_code}")
            sys.exit()
    except Exception as e:
        print("Error fetching /robots.txt:", e)
        sys.exit()
        
if __name__ == "__main__":
    target_host = input("Enter the target website: ")
    print(f"checking robots.txt in  {target_host}...")
    result = check_robot(target_host)

    if result:
        print(result)