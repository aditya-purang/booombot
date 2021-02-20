
from flask import Flask, jsonify
from youtubesearchpython import VideosSearch, CustomSearch, VideoSortOrder


app = Flask(__name__)
app.config["DEBUG"] = True


'''
title: "Ashes on Fire",
      artist: "Attack on Titan",
      img_src: "./images/song-3.jpg",
      src:
'''


def return_dict(song_name):

    song_dict = CustomSearch(
        song_name, VideoSortOrder.viewCount, limit=1).result()
    src = song_dict.get("result")[0].get("link")
    image_src = song_dict.get("result")[0].get("thumbnails")[0].get("url")
    if(len(song_dict.get("result")[0].get("thumbnails"))>1):
        image_src = song_dict.get("result")[0].get("thumbnails")[1].get("url")
    channel = song_dict.get("result")[0].get("channel").get("name")
    title = song_dict.get("result")[0].get("title")

    ret_dict = {"src": src, "image_src": image_src,
                "channel": channel, "title": title}
    return ret_dict


@app.route('/', methods=['GET'])
def home():
    return "api"


@app.route('/getlinks/<string:song_str>', methods=['GET'])
def get_links(song_str):
    songlist = song_str.split(',')
    for i in range(len(songlist)):
        songlist[i] = songlist[i].strip()

    url_list = []

    url_list = [return_dict(song) for song in songlist]

    return jsonify(url_list)


if __name__ == '__main__':
    app.run()
