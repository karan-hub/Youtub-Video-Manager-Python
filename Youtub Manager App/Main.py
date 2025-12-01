import sys
import  json 
def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index , item in enumerate(videos , start=1):
        print(f"Sr. {index}, Name: {item['name']}, Duration: {item['time']}")
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter Video Name")
    time = input("Enter Video Duration")
    videos.append({'name':name , 'time':time})
    save_data(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted"))

    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid index!")

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be updated"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name").strip() or videos[index-1]['name']
        time = input("Enter the new video time").strip() or videos[index-1]['time']
        videos[index-1] ={'name': name ,'time':time}
        save_data(videos)
        print("Video updated successfully!")
    else:
        print("Invalid index selected")



def load_data():
    try:
       with open('data.txt', 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except  Exception as e:
        return []

def save_data(videos):
    
    with open('data.txt','w') as file:
        json.dump(videos , file , indent=4)


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
               update_video(videos)
            case '4':
                 delete_video(videos)
            case '5':
                break
            case _:
                print("sorry ! invalid Input please try again latter")

if __name__=='__main__':
    main()
