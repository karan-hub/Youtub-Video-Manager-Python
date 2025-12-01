import sys
import  json 
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index , item in enumerate(videos , start=1):
        print(f'Sr. {index} , name:{item['name']} , Duration:{item['time']}')
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter Video Name")
    time = input("Enter Video Duration")
    videos.append({'name':name , 'time':time})
    save_data(videos)

def delete_video(videos):
    raise NotImplementedError

def update_video(videos):
    raise NotImplementedError

def load_data():
    try:
       with open('data.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except  Exception as e:
        print(f'Error: {e}')

def save_data(videos):
    data = load_data()
    data.append(videos)
    with open('data.txt','w') as file:
        json.dump(data , file , indent=4)


def main():
    videos=load_data()
    
    user = sys.argv[1] if len(sys.argv)>1 else "Guest"
    print(f'Hellow  {user}')
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")
         

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                delete_video(videos)
            case '4':
                update_video(videos)
            case '5':
                break
            case _:
                print("sorry ! invalid Input please try again latter")

if __name__=='__main__':
    main()
