import sqlite3

con = sqlite3.connect('data.db')
cursor=  con.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
     cursor.execute('''
SELECT * FROM VIDEOS 
''')
     for item  in cursor.fetchall():
         print(item)


def add_video(name, time):
    cursor.execute('''
        INSERT INTO VIDEOS (name , time) 
                      VALUES (?,?)
''' ,(name , time))
    
    con.commit()

def update_video(video_id, name, time):
      cursor.execute('''
        UPDATE VIDEOS SET name =? , time=? 
        WHERE ID= ?
''' ,(name , time , video_id))
      
      con.commit()

def delete_video(video_id):
    cursor.execute('''
        DELETE FROM VIDEOS  
        WHERE ID= ?
''' ,(video_id ,))
    con.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

    conn.close()

if __name__ == "__main__":
    main()
