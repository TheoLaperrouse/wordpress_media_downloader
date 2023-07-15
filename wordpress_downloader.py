import os
import requests

def get_wordpress_media(url):
    api_url = url + '/wp-json/wp/v2/media?per_page=100'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        media_data = response.json()
        print(media_data)
        return media_data
    else:
        print('Erreur lors de la récupération des médias:', response.status_code)
        return None

def download_media(media_data):
    output_dir = 'wordpress_media'
    
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for item in media_data:
        media_url = item['source_url']
        media_filename = os.path.basename(media_url)
        output_path = os.path.join(output_dir, media_filename)
        response = requests.get(media_url)
        if response.status_code == 200:
            with open(output_path, 'wb') as file:
                file.write(response.content)
                print('Téléchargé:', media_filename)
        else:
            print('Erreur lors du téléchargement:', media_filename, response.status_code)

if __name__ == '__main__':
    wordpress_url = input('Quel est le site wordpress dont vous voulez récupérer les médias ? ')
    media = get_wordpress_media(wordpress_url)
    if media is not None:
        download_media(media)
