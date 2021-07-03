from flask import Flask , jsonify , request
app = Flask(__name__)

tasks = [
{
        'id': 1,
        'title': u'Pass_',
        'description': u'Rank 234 , 97%', 
        'done': False
    },
{
        'id': 2,
        'title': u'Fail',
        'description': u'Rank 33768 , 45%' ,
        'done': False
    }

]

@app.route("/")
def pass_():
    return "you are selected fill ! , the form to join"

@app.route("/add-data",methods =["POST"])
def Fail():
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message": "you are not selected",
        },400)

    task ={
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({
            "status" : "successful",
            "message": "Task added successfully ",
        })



@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks 
    })

if(__name__ == "__main__"):
    app.run(debug = True)