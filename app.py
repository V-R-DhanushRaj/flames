from flask import Flask, render_template, request

app = Flask(__name__)

def Love_Calculator(name1, name2):
    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    count = 0
    n2_char = list(name2)
    for i in name1:
        if i in n2_char:
            n2_char.remove(i)
        else:
            count += 1
    count += len(n2_char)

    index = 0
    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)
    
    return flames[0]

@app.route('/')
def index():
    return render_template('Index.html')

@app.route('/destiny')
def destiny():
    if ("name1" not in request.args) or ("name2" not in request.args):
        return render_template('Index.html')
    
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')

    msg = Love_Calculator(name1, name2)

    return render_template('Destiny.html', destiny_msg=msg)