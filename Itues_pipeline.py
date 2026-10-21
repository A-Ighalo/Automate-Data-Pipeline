
from datetime import date
import pandas as pd
import requests
import json
import os



class Song:
    def __init__ (self,ArtistId):
        self.ArtistId = ArtistId
        self.respnse_by_artist = None
       


    def main(self):
        self.response_by_artist = requests.get(f'https://itunes.apple.com/lookup?id={self.ArtistId}&entity=song&limit=200')
        # print(json.loads(self.response_by_artist.text))
        return self.response_by_artist
  

    def TransformData(self,data):
        tracks = []
        for data in data['results']:
             if data.get('wrapperType') == 'track':
                  tracks.append(data)
        return tracks
        
                  
    def SaveData(self,data):
        os.makedirs("data_folder",exist_ok=True)             
        df = pd.DataFrame(data)
        df.to_csv('data_folder/songs.csv', index=False)        
        
        with open('data_folder/songs.json','w') as file:
            json.dump(data,file, indent = 2)

if __name__ == '__main__':
        song = Song(ArtistId = 1304716885 )
        response = song.main()
        transform_data = song.TransformData(data=response.json())
        song.SaveData(data=transform_data)