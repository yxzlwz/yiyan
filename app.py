import os
import random as rd

import requests as rq
from flask import *

import config as c

app = Flask(__name__)
thisDir = os.path.dirname(os.path.abspath(__file__))
sentences = {}
types = ""
types_name = {
    "a": "原创",
    "b": "网络",
    "c": "歌曲",
    "d": "文学",
    "e": "影视",
    "f": "游戏",
    "g": "哲学",
    "h": "诗词",
    "i": "动漫/漫画",
    "j": "抖机灵",
    "y": "其它",
    "z": "未知"
}
stc_uuid = {}


def init_local_data(dir=c.dir, cate=c.cate):
    global sentences, types
    for i in cate:
        with open(f"{dir}/{i}.json", "r", encoding="utf-8") as f:
            if not sentences.get(i):
                sentences[i] = []
            data = json.loads(f.read())
            l = len(sentences[i])
            for j in range(len(data)):
                stc_uuid[data[j]["uuid"]] = [i, j + l]
            sentences[i] += data
    types = "".join(sentences.keys())


def init_remote_data(url=c.url, cate=c.cate):
    global sentences, types
    for i in cate:
        if not sentences.get(i):
            sentences[i] = []
        data = rq.get(f"{url}/{i}.json").json()
        l = len(sentences[i])
        for j in range(len(data)):
            stc_uuid[data[j]["uuid"]] = [i, j + l]
        sentences[i] += data
        print(i)
    types = "".join(sentences.keys())


def init():
    global types, types_name, sentences
    if c.data_from == "local":
        init_local_data()
    else:
        init_remote_data()
    types = [i for i in types]
    for i in types_name.keys():
        if not sentences.get(i):
            sentences[i] = []
            types.remove(i)
    types = "".join(types)


@app.route("/get", methods=["GET", "POST"])
def get_sentences():
    _type = rd.choice(request.values.get("type") or types)
    res = rd.choice(sentences[_type])
    return json.dumps(res,
                      ensure_ascii=False,
                      indent=4,
                      sort_keys=True,
                      separators=(",", ": "))


@app.route("/uuid/<uuid>", methods=["GET", "POST"])
def get_sentence_with_uuid(uuid):
    return json.dumps(sentences[stc_uuid[uuid][0]][stc_uuid[uuid][1]],
                      ensure_ascii=False,
                      indent=4,
                      sort_keys=True,
                      separators=(",", ": "))


@app.route("/")
def index():
    return render_template("index.html",
                           sentence=rd.choice(sentences[rd.choice(types)]))


init()


if __name__ == "__main__":
    app.run(debug=False, port=596, host="0.0.0.0")
