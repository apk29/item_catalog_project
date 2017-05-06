# @app.route('/')
# @app.route('/hello')
# def HelloWorld():
#     category = session.query(Category).first()
#     items = session.query(Item).filter_by(category_id=category.id)
#     output = ''
#     for i in items:
#         output += i.name
#         output += '</br>'
#     return output