import sqlite3

con = sqlite3.connect("youtube_videos.db") #creating database connection

cursor= con.cursor() #creating cursor object

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_all_videos():
    #Becuase only cursor can execute query
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id= ?",(video_id,))
    con.commit()    


# MAIN METHOD

def main():

    while True:
        print("\n Youtube Manager  | choose an option")
        print("1. List all the videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        
        choice = input("Enter you choice: ")

        # Like switch case in other languages python has match case statements to handle multiple cases
        match choice:
            case "1":
                list_all_videos()
            case "2":
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name,time)    
            case "3":
                video_id = input("Enter video ID to update: ")
                name = input("Enter updated video name: ")
                time = input("Enter updated video time: ")
                update_video(video_id,name, time)
            case "4":
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case "5":
                break # Break the loop and exit
            case _: # Default case
                print("Invalid choice")

    con.close() # closing database connection

if __name__=="__main__":
    main()