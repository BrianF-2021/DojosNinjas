from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import ninja

class Dojo:
    db = "dojo_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        dojos_from_db = connectToMySQL(cls.db).query_db(query)
        dojos = []
        for dojo in dojos_from_db:
            dojos.append(dojo)
        return dojos


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return (cls(result[0]))


    @classmethod
    def get_one_complete(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        print('result:', result)
        dojo = (cls(result[0]))
        if len(result) == 0:
            return dojo
        else:
            for i in range(len(result)):
                ninjas_data ={
                    'id' : result[i]['ninjas.id'],
                    'first_name' : result[i]['first_name'],
                    'last_name' : result[i]['last_name'],
                    'age' : result[i]['age'],
                    'created_at' : result[i]['ninjas.created_at'],
                    'updated_at' : result[i]['ninjas.updated_at']
                }
                dojo.ninjas.append(ninja.Ninja(ninjas_data))
        # user.cars.append(car.Car.get_one_complete(car_data))
            return dojo


#####################################
# #######################################

#     @classmethod
#     def get_one_with_user(cls, data):
#         query = "SELECT * FROM dojos JOIN users ON dojos.user_id = users.id WHERE dojos.id = %(id)s;"
#         result = connectToMySQL(cls.db).query_db(query, data)
#         dojo = (cls(result[0]))
#         users_data ={
#             'id' : result[0]['users.id'],
#             'first_name' : result[0]['last_name'],
#             'last_name' : result[0]['last_name'],
#             'email' : result[0]['email'],
#             'created_at' : result[0]['users.created_at'],
#             'updated_at' : result[0]['users.updated_at']
#         }
#         dojo.user = user.User(users_data)
#         return dojo


#     @classmethod
#     def get_one_complete(cls, data):
#         query = "SELECT * FROM dojos JOIN ninjas ON dojos.user_id = users.id JOIN makers ON dojos.maker_id = makers.id WHERE dojos.id = %(id)s;"
#         result = connectToMySQL(cls.db).query_db(query, data)
#         dojo = (cls(result[0]))
#         users_data ={
#             'id' : result[0]['users.id'],
#             'first_name' : result[0]['first_name'],
#             'last_name' : result[0]['last_name'],
#             'email' : result[0]['email'],
#             'created_at' : result[0]['users.created_at'],
#             'updated_at' : result[0]['users.updated_at']
#         }
#         dojo.user = user.User(users_data)

#         makers_data ={
#             'id' : result[0]['makers.id'],
#             'name' : result[0]['name'],
#             'created_at' : result[0]['makers.created_at'],
#             'updated_at' : result[0]['makers.updated_at']
#         }
#         dojo.maker = maker.Maker(makers_data)

#         return dojo


    @classmethod
    def save(cls, data):
        print("data:", data)
        query = "INSERT INTO dojos(name) VALUES(%(name)s);"

        data = {
            'name' : data['name'],
        }
        return connectToMySQL(cls.db).query_db(query, data) # returns id of object created/inserted


#     @classmethod
#     def update(cls, data):
#         query = "UPDATE dojos SET color = %(color)s, year = %(year)s, updated_at = NOW() WHERE dojos.id = %(id)s;"
#         return connectToMySQL(cls.db).query_db(query, data)


#     @classmethod
#     def delete(cls, data):
#         query = "DELETE FROM dojos WHERE id = %(id)s;"
#         return connectToMySQL(cls.db).query_db(query,data)




    # @classmethod
    # def get_user(cls, data):
    #     query = "SELECT * FROM users WHERE id = %(id)s"
    #     user_from_db = connectToMySQL(cls.db).query_db(query,data)
    #     return cls(user_from_db[0])


    # # @classmethod
    # # def save(cls, data):
    # #     query = "INSERT INTO users(first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s,%(email)s);"
    # #     return connectToMySQL(cls.db).query_db(query,data)



    # @classmethod
    # def edit_user(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s;"
    #     data = {
    #         'first_name' : data['first_name'],
    #         'last_name' : data['last_name'],
    #         'email' : data['email']
    #     }
    #     return connectToMySQL(cls.db).query_db(query,data)





    # @classmethod
    # def delete_user(cls, data):
    #     query = "DELETE FROM users WHERE id = %()s"
    #     return connectToMySQL(cls.db).query_db(query,data)


    # @classmethod
    # def delete_users(cls, data):
    #     query = "TRUNCATE TABLE users"
    #     return connectToMySQL(cls.db).query_db(query, data)