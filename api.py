#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask Bob!'

men = [
    {
        'name': u"dave",
        'img': u'http://s8.postimg.org/ib4lbozp1/11000145_10153062157102570_157426480721790456_n.jpg',
        'age': 26,
        'married': True
    },
    {
        'name': u"gary",
        'img': u'http://s10.postimg.org/718snsqqx/IMG_6703.jpg',
        'age': 19,
        'married': True
    },
    {
        'name': "henry",
        'img': u'http://s28.postimg.org/4mcp3qzi5/IMG_6676.jpg',
        'age': 28,
        'married': False
    },
    {
        'name': "brad",
        'img': u'http://s21.postimg.org/dmnj8s6sn/IMG_5770.jpg',
        'age': 33,
        'married': False
    }

]

women = [

    {
        'name': "shirley",
        'img': u'http://s22.postimg.org/waazs9wep/IMG_6031.jpg',
        'age': 54,
        'married': False
    },
    {
        'name': "ashely",
        'img': u'http://s17.postimg.org/dwpmt06z3/IMG_6901.jpg',
        'age': 41,
        'married': False
    },
    {
        'name': u"carol",
        'img': u'http://s10.postimg.org/jkzbxspk9/IMG_6868.jpg',
        'age': 18,
        'married': False
    },
    {
        'name': u"mary",
        'img': u'http://s21.postimg.org/m1poa79t3/IMG_6884.jpg',
        'age': 30,
        'married': False
    }

]



@app.route('/2date/api/v1.0/men', methods=['GET'])
def get_men():
    return jsonify({'men': men})

@app.route('/2date/api/v1.0/women', methods=['GET'])
def get_women():
    return jsonify({'women': women})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)







