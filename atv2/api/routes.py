from flask import render_template, Flask, jsonify, request, abort
from api import app

students = [
  { 'id': 1, 'name': 'Samuel', 'age': 10 },
  { 'id': 2, 'name': 'Lucas', 'age': 11 },
  { 'id': 3, 'name': 'Silva', 'age': 12 },
  { 'id': 4, 'name': 'Sena', 'age': 13 }
]

# default is GET, but you can define that

# METHODS GET
@app.route('/')
def hello():
  return render_template('index.html')

@app.route('/api/student', methods=['GET'])
def get_students():
  return jsonify({ 'students': students })

@app.route('/api/students/<int:id>')
def get_student(id):
  res = [student for student in students if student['id'] == id]
  
  if len(res) > 0:
    return jsonify({ 'student': res })
  else:
    return abort(404)

@app.route('/api/students/search')
def query_example():
  if len(request.args) > 0:
    key = request.args['keyword']
    return jsonify({ 'search': key })
  else:
    return jsonify({'search': '' })

# METHODS POST
@app.route('/example-post', methods=['POST'])
def json_example():
  data = request.get_json()
  name = data['name']
  age = data['age']

  return jsonify({ 'name': name })

# METHODS PUT
@app.route('/api/students/<int:id>', methods=['PUT'])
def update_student(id):
  # update student
  # ...
  return jsonify({ 'student_id': id })

@app.route('/api/students/<int:id>', methods=['DELETE'])
def delete_student(id):
  # delete student
  # ...
  return jsonify({ 'student_id': id })

@app.errorhandler(404)
def not_found(error):
    print(">>> ", error)
    return jsonify({'error': 'Not Found'}), 404