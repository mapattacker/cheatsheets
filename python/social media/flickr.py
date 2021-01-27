import argparse
import os
import urllib

import flickrapi


def dl_flickr_images(query, folder, limit):
    """Download flickr images into local drive
    Read from FLICKR official API Docs:
    1) API Docs on Search: https://www.flickr.com/services/api/flickr.photos.search.html
    2) API Testing Site: https://www.flickr.com/services/api/explore/flickr.photos.search
    3) Sample API Query: https://api.flickr.com/services/rest/?format=json&api_key=<apikey>&method=flickr.photos.search&sort=relevance&text=<text>&extras=url_l&per_page=100
    
    Args
    ----
    text (str): keyword to search photos
    folder (str): folder where images will be downloaded & stored in
    limit (int): set limit on how many photos to download"""

    FLICKR_ACCESS_KEY = os.environ["FLICKR_ACCESS_KEY"]
    FLICKR_SECRET_KEY = os.environ["FLICKR_SECRET_KEY"]

    print("Downloading {}".format(query))
    flickr = flickrapi.FlickrAPI(FLICKR_ACCESS_KEY, FLICKR_SECRET_KEY, cache=True)

    photos = flickr.walk(text=query, sort="relevance", extras="url_c", per_page=100)

    folder = folder.replace(" ", "_")
    folder = os.path.join("images", folder)
    if not os.path.exists(folder):
        os.makedirs(folder)

    cnt = 0
    for photo in photos:
        url = photo.get("url_c")
        if url is not None:
            cnt += 1
            if cnt >= limit:
                break
            else:
                fill = str(cnt).zfill(3)
                imgpath = os.path.join(folder, "{}_{}.jpg".format(fill, text))
                urllib.request.urlretrieve(url, imgpath)
                if cnt % 50 == 0:
                    print("{} downloaded".format(cnt))

    print("{} photos downloaded!".format(cnt))


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--query", required=True, help="search query to in Flickr API")
    parser.add_argument("-o", "--output", required=True, help="path to output directory of images")
    parser.add_argument("-l", "--limit", required=True, help="no. images to search")
    args = parser.parse_args()

    query = args["query"]
    output = args["output"]
    limit = args["limit"]

    dl_flickr_images(query, output, limit)