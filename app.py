from os import environ
from flask import Flask, request
import media
keys = ["1234", "test", "dhurgham", "aymen"]
#servers = ["youtube","youtube1","facebook","twitter","twitter1","twitter2","twitter3","soundcloud","pinterest","pinterest_search","tiktok"]
my_app = Flask(__name__)

@my_app.route("/", methods=['GET'])
def home():
    url = request.args.get("url")
    server = request.args.get("s")
    key = request.args.get("key")
    text = request.args.get("text")
    if key in keys:
        if url != None:
            if server == "facebook":
                return media.facebook.dl(url)
            elif server == "twitter":
                return media.twitter.dl(url)
            elif server == "twitter1":
                return media.twitter1.dl(url)
            elif server == "twitter2":
                return media.twitter2.dl(url)
            elif server == "twitter3":
                return media.twitter3.dl(url)
            elif server == "soundloud":
                return media.soundcloud.dl(url)
            elif server == "youtube":
                return media.youtube.dl(url)
            elif server == "youtube1":
                return media.youtube1.dl(url)
            elif server == "pinterest":
                return media.pinterest.dl(url)
            elif server == "tiktok":
                return media.tiktok.dl(url)
        elif url == None and server == "pinterest_search":
            return media.pinterest_search.search(text=text)
        else:
            return ":)"

    else:
        return ":)"


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(environ.get('PORT', 5000))
    my_app.run(host='0.0.0.0', port=port)
