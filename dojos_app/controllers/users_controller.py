# # from flask_app import app
# # from flask import render_template,redirect,request,session,flash
# # from flask_app.config.mysqlconnection import connectToMySQL
# # from flask_app.models.user import User

# from dojos_app import app
# from flask import render_template, redirect, request
# from dojos_app.models.user import User


# @app.route('/')
# def user_index():
#     #return render_template('main.html')
#     return redirect('/users')

# @app.route('/users')
# def user_dashboard():
#     users = User.get_all()
#     print('users', users)
#     return render_template("users_dash.html", users = users)


# @app.route('/users/new')
# def new_user():
#     return render_template('new_user.html')#show form


# @app.route('/users/create', methods = ['POST'])
# def create_user():
#     print("request.form:",request.form)
#     User.save(request.form)
#     return redirect('/users')


# @app.route('/users/<int:user_id>')
# def user_show(user_id):
#     data = {
#         'id':user_id
#     }
#     user = User.get_one_complete(data)
#     #user = User.get_one_with_user(data)
#     #user = User.get_one_with_maker(data)
#     #user = User.get_one(data)
#     return render_template('users_view.html', user = user)





# @app.route("/users/<int:user_id>/edit")
# def user_edit(user_id):
#     data = {
#         'id':user_id
#     }
#     user = User.get_one(data)
#     return render_template('users_edit.html', user = user)


# # @app.route("/users/<int:user_id>/update", methods=['POST'])
# # def user_update(user_id):
# #     data = {
# #         'id':user_id,
# #         'color':request.form['color'],
# #         'year':request.form['year']
# #     }
# #     print('update data:', data)
# #     User.update(data)
# #     return redirect(f'/users/{user_id}')


# # @app.route("/users/<int:user_id>/destroy")
# # def user_destroy(user_id):
# #     data = {
# #         'id':user_id
# #     }
# #     User.delete(data)
# #     return redirect('/users')


# ###############################################
# ##############################################


# # @app.route('/show_user')
# # def show_user():
# #     user = User.get_user(session['id'])
# #     print("user", user)
# #     render_template('show_user.html', user = user)


# # @app.route('/delete_users', methods =['POST'])
# # def delete_users():
# #     User.delete_users(request.form)
# #     return redirect('/main')
# #     # users = User.create_user()
# #     # return connectToMySQL('users_db').query_db(query, data)




# # @app.route('/pastries/<int:id>/edit')
# # def show_pastry(id):
# #     data = {
# #     'id': id
# #     }
# #     pastry = Pastry.get_one(data)
# #     return render_template('edit_pastry.html', pastry = pastry)






# # showing all pastries

# # edit a pastry - showing the form

# # edit a pastry - actually saving the changes

# # creating a new pastry - showing the form

# # creating a new pastry - actually creates pastry in the database

# # deleting a pastry
