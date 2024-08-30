import urllib.request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen


def download_file_with_url():
    print("downloading...")
    url = 'https://i.pinimg.com/564x/83/8d/7b/838d7b3c917f2ec4cc2dab3dc87b42df.jpg'
    
    # Tải file về và đặt theo tên mong muốn
    urllib.request.urlretrieve(url, '../download.jpg')

# with urllib.request.urlopen(url) as response, open('download.jpg', 'wb') as out_file:
#     print('status: ', response.status)
#     print('downloading pixel art')
#     with open('download.jpg', 'wb') as in_file:
#         in_file.write(response.read())
def example_get_api_list():
    url = 'http://api.github.com'
    # url = 'https://api.pixabay.com/'
   
    response = requests.get(url)
    print(response.json())
    
def example_use_search_api():
    url = 'https://pixabay.com/en/photos/'
    params = {
        "q": "yellow",
        "type": "photo",
        "order": "popular",
        "imageWidth": 4000,
        "imageHeight": 2250
        # "filter": "some_filter"
    }
    response = requests.get(url, params)
    print(response.url)
    
def example_get_all_links():
    url = 'https://en.wikipedia.org/wiki/Python'
    # bs = BeautifulSoup(urlopen(url), 'html.parser')
    bs = BeautifulSoup(urlopen(url))
    
    for link in bs.find_all("a"):
        if 'href' in link.attrs:
            print(link.attrs['href'])
            
def example_get_all_images():
    url = 'https://en.wikipedia.org/wiki/Python'
    response = requests.get(url)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    images = []
    for img in soup.find_all('img'):
        # Check if the image has a 'src' attribute (might not always be present)
        if 'src' in img.attrs:
            image_url = img.attrs['src']
            # Handle absolute vs. relative URLs
            if not image_url.startswith('http'):
                image_url = f"https:{image_url}"  # Assuming it's a relative path on Wikipedia
            images.append(image_url)
    
    for url in images:
        print(url)
        
def temp():
    url = 'https://en.wikipedia.org/wiki/Python'
    headers = requests.utils.default_headers()
    
    response = requests.get(url, headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    images = []
    for img in soup.find_all('img'):
        # Check if the image has a 'src' attribute (might not always be present)
        if 'src' in img.attrs:
            image_url = img.attrs['src']
            # Handle absolute vs. relative URLs
            if not image_url.startswith('http'):
                image_url = f"https:{image_url}"  # Assuming it's a relative path on Wikipedia
            images.append(image_url)

    for url in images:
        print(url)
def exaple_get_ket_qua_xo_so():
    url = 'https://xoso.com.vn/xo-so-mien-bac/xsmb-p1.html'
    tag_name, attributes={}
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    pass

if __name__ == "__main__":
    # download_file_with_url()
    # example_get_api_list()
    exaple_get_ket_qua_xo_so()
    pass
    