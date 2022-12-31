student = {
  'name': 'sanket',
  'class': '10',
  'roll_id': '2'
}
print(student.keys() >= {'class', 'name'})
print(student.keys() >= {'name', 'sanket'})
print(student.keys() >= {'roll_id', 'name'})