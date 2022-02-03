from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import dojo

class Ninja:
    db = "dojo_and_ninjas"

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas"
        ninjas_from_db = connectToMySQL(cls.db).query_db(query)
        ninjas = []
        for ninja in ninjas_from_db:
            ninjas.append(ninja)
        return ninjas


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM ninjas WHERE ninjas.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return (cls(result[0]))


    @classmethod
    def get_one_complete(cls, data):
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        print('result:', result)
        ninja = (cls(result[0]))
        if len(result) == 0:
            return ninja
        else:
            ninjas_data ={
            'id' : result[0]['dojos.id'],
            'name' : result[0]['name'],
            'created_at' : result[0]['dojos.created_at'],
            'updated_at' : result[0]['dojos.updated_at']
            }
            ninja.dojo = dojo.Dojo(ninjas_data)
            return ninja


    # @classmethod
    # def get_one_with_user(cls, data):
    #     query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojo.id WHERE ninjas.id = %(id)s;"
    #     result = connectToMySQL(cls.db).query_db(query, data)
    #     ninja = (cls(result[0]))
    #     users_data ={
    #         'id' : result[0]['users.id'],
    #         'first_name' : result[0]['last_name'],
    #         'last_name' : result[0]['last_name'],
    #         'email' : result[0]['email'],
    #         'created_at' : result[0]['users.created_at'],
    #         'updated_at' : result[0]['users.updated_at']
    #     }
    #     ninja.user = user.User(users_data)
    #     return ninja


    # @classmethod
    # def get_one_complete(cls, data):
    #     query = "SELECT * FROM ninjas JOIN users ON ninjas.user_id = users.id JOIN makers ON ninjas.maker_id = makers.id WHERE ninjas.id = %(id)s;"
    #     result = connectToMySQL(cls.db).query_db(query, data)
    #     ninja = (cls(result[0]))
    #     users_data ={
    #         'id' : result[0]['users.id'],
    #         'first_name' : result[0]['first_name'],
    #         'last_name' : result[0]['last_name'],
    #         'email' : result[0]['email'],
    #         'created_at' : result[0]['users.created_at'],
    #         'updated_at' : result[0]['users.updated_at']
    #     }
    #     ninja.user = user.User(users_data)

    #     makers_data ={
    #         'id' : result[0]['makers.id'],
    #         'name' : result[0]['name'],
    #         'created_at' : result[0]['makers.created_at'],
    #         'updated_at' : result[0]['makers.updated_at']
    #     }
    #     ninja.maker = maker.Maker(makers_data)

    #     return ninja


    # @classmethod
    # def save(cls, data):
    #     print("data:", data)
    #     query = "INSERT INTO ninjas(name) VALUES(%(name)s);"

    #     data = {
    #         'name' : data['name'],
    #     }
    #     return connectToMySQL(cls.db).query_db(query, data) # returns id of object created/inserted


    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE ninjas SET color = %(color)s, year = %(year)s, updated_at = NOW() WHERE ninjas.id = %(id)s;"
    #     return connectToMySQL(cls.db).query_db(query, data)


    # @classmethod
    # def delete(cls, data):
    #     query = "DELETE FROM ninjas WHERE id = %(id)s;"
    #     return connectToMySQL(cls.db).query_db(query,data)




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