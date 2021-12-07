from googleapiclient.discovery import build

api_Y_key = 'AIzaSyC4JY5dF76VLuKt4Vk6p4rwxgGLw6PWgbA'
youtube = build('youtube', 'v3', developerKey=api_Y_key)

collection = youtube.channels().list(
    part='statistics',
    forUsername='Tainam Silva'
)

response = collection.execute()
print(response)
