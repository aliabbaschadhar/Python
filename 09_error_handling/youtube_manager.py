import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            content = file.read()
            if not content.strip():  # Check if the file is empty
                return []  # Return an empty list if the file is empty
            else:
                return json.loads(content)  # Parse the JSON string
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Warning: The file contains non-JSON data. Returning an empty list.")
        return []

# To save the videos in the text file
def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file) # Will write the data of videos in the text file

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos,start=1):
        print(f"{index}, {video["name"]}, Duration: {video['time']}")
    
    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name": name, "time": time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    if 1<=index<=len(videos):
        index = int(input("Enter the index of the video you want to update: "))
        name = input("Enter the new name: ")
        time = input("Enter the new time: ")
        videos[index -1]["name"] = name
        # index-1 list is always starting from 0 not 1 so -1
        # We did the index of tuples created by enumerate function in list_all_videos to show user that index starts from 1 but in program list starts from 0
        videos[index-1]["time"] = time
        save_data_helper(videos)
    else:
        print("Invalid index")

def delete_video(videos):
    list_all_videos(videos)
    if 1<=index<=len(videos):
        index = int(input("Enter the index of the video you want to delete: "))
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index")


# Now we have a problem that from where should our code starts running like which method should run first? 
# For that we make a main function in python and call it at the end of our code

def main():

    videos = load_data()

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
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break # Break the loop and exit
            case _: # Default case
                print("Invalid choice") 

# Call the main function
if __name__=="__main__": # Search the whole file and look for function name with main and then call it
    main()
