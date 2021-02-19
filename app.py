
from flask import Flask,jsonify
from youtubesearchpython import VideosSearch


app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "api"

@app.route('/getlinks/<string:song_str>', methods=['GET'])
def get_links(song_str):
    songlist=song_str.split(',')
    for i in range(len(songlist)):
        songlist[i]=songlist[i].strip()

    url_list=[]

    
    url_list=[CustomSearch(song, VideoSortOrder.viewCount, limit = 1).result().get("result")[0].get("link") for song in songlist]

    return jsonify(url_list)

if __name__ == '__main__':
    app.run()



   

