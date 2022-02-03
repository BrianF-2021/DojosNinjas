# from flask_app import app
# from flask import render_template,redirect,request,session,flash
# from flask_app.config.mysqlconnection import connectToMySQL
# from flask_app.models.user import User

from dojos_app import app
from flask import render_template, redirect, request
from dojos_app.models.dojo import Dojo


@app.route('/')
def dojo_index():
    #return render_template('main.html')
    return redirect('/dojos')

@app.route('/dojos')
def dojo_home():
    dojos = Dojo.get_all()
    print('dojos', dojos)
    return render_template("dojos_home.html", dojos = dojos)


# @app.route('/dojos/new')
# def new_dojo():
#     return render_template('new_dojo.html')#show form


@app.route('/dojos/create', methods = ['POST'])
def create_dojo():
    print("request.form:",request.form)
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/<int:dojo_id>')
def dojo_show(dojo_id):
    data = {
        'id':dojo_id
    }
    dojos = Dojo.get_one_complete(data)
    #dojo = Car.get_one_with_user(data)
    #dojo = Car.get_one_with_maker(data)
    #dojo = Car.get_one(data)
    print('dojos', dojos)
    
    return render_template('dojos_view.html', dojos = dojos)


# @app.route("/dojos/<int:dojo_id>/edit")
# def dojo_edit(dojo_id):
#     data = {
#         'id':dojo_id
#     }
#     dojo = Dojo.get_one(data)
#     return render_template('dojos_edit.html', dojo = dojo)


# @app.route("/dojos/<int:dojo_id>/update", methods=['POST'])
# def dojo_update(dojo_id):
#     data = {
#         'id':dojo_id,
#         'color':request.form['color'],
#         'year':request.form['year']
#     }
#     print('update data:', data)
#     Dojo.update(data)
#     return redirect(f'/dojos/{dojo_id}')


# @app.route("/dojos/<int:dojo_id>/destroy")
# def dojo_destroy(dojo_id):
#     data = {
#         'id':dojo_id
#     }
#     Dojo.delete(data)
#     return redirect('/dojos')





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
