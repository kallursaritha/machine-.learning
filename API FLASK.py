from flask import Flask, jsonify

app = Flask(__name__)
courses=[{'name':"python programming certificate",
          'course_id':"0",
          'Description':"Python programming certification helps you learn"
                         "python in the structured learning path with innovative"
                         "out of the box projects matching the industry standards",
         'price': "visit Edureka.co to know more"},
         {'name': "Data Science with python certification",
          'course_id':"1",
          'Description':"Data Science with python helps you master the data science"
                         "life cycle processes in a structured learning path",
          'price':"visit Edureka.co to know more"},
         {'name': "AI and ML learning certification",
          'course_id': "2",
          'Description':"AI and ML certification will help you master AI/ML with",
                        "top notch projects like speechrecognition, chatbots, etc." 
         'price': "visit Edureka.co to know more"}]
@app.route('/')
def index():
    return 'Welcome to the course API'

@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'courses':courses})


@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course= {'name': "python programming certificate",
          'course_id': "0",
          'Description':"Python programming certification helps you learn"
                        "python in the structured learning path with innovative"
                         "out of the box projects matching the industry standards",
         'price':"visit Edureka.co to know more"}
    courses.append(course)
    return jsonify({'created': course})

@app.route("/course/<int:course_id>",methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description']="XYZ"
    return jsonify({'course':courses[course_id]})


@app.route("/course/<int:course_id>",methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result':True})


if __name__=='__main__':
    app.run()
