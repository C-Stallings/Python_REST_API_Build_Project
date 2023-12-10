import requests

BASE = "http://127.0.0.1:5000/"

## Note: Initial Testing -  inputting and getting data ##
# data = [
#     {"likes": 50, "name": "Jane", "views": 50000},
#     {"likes": 100, "name": "How to make REST API", "views": 200000},
#     {"likes": 3, "name": "Blake", "views": 3000},
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), data[i])
#     print(response.json())

# input()

##### Below is a test code for DELETE, GET, PATCH database checks as well as checking what's currently in the full database #####
##### Disable comments as needed to test code #####

#### Note: Testing Delete - deleting from db ####
# response = requests.delete(BASE + "video/4")
# print(response)


#### Note: Testing Get - adding to the db ####
# response = requests.put(
#     BASE + "video/4", {"likes": 25000, "name": "Bob", "views": 70000}
# )
# print(response.json())


#### Note: Testing Patch - updating db ####
# response = requests.patch(BASE + "video/3", {"views": 1500, "likes": 8000})
# print(response.json())


#### Note: Testing Current db info - How to check what is currently in database ####
# Assuming the video IDs start from 1 and go up to the total number of videos
# total_videos = 5  # Update this with the total number of videos in your database

# for video_id in range(1, total_videos + 1):
#     response = requests.get(BASE + f"video/{video_id}")
#     if response.status_code == 200:
#         print(response.json())
#     else:
#         print(f"Video with ID {video_id} not found.")
