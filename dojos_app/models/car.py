from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import maker, user

class Car:
    db = "cars_db"

    def __init__(self, data):
        self.id = data['id']
        self.color = data['color']
        self.year = data['year']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.maker = None
        self.user = None


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars"
        cars_from_db = connectToMySQL(cls.db).query_db(query)
        cars = []
        for car in cars_from_db:
            cars.append(car)
        return cars


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM cars WHERE cars.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        return (cls(result[0]))


    @classmethod
    def get_one_with_maker(cls, data):
        query = "SELECT * FROM cars JOIN makers ON cars.maker_id = makers.id WHERE cars.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        car = (cls(result[0]))
        makers_data ={
            'id' : result[0]['makers.id'],
            'name' : result[0]['name'],
            'created_at' : result[0]['makers.created_at'],
            'updated_at' : result[0]['makers.updated_at']
        }
        car.maker = maker.Maker(makers_data)
        return car


    @classmethod
    def get_one_with_user(cls, data):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id WHERE cars.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        car = (cls(result[0]))
        users_data ={
            'id' : result[0]['users.id'],
            'first_name' : result[0]['last_name'],
            'last_name' : result[0]['last_name'],
            'email' : result[0]['email'],
            'created_at' : result[0]['users.created_at'],
            'updated_at' : result[0]['users.updated_at']
        }
        car.user = user.User(users_data)
        return car


    @classmethod
    def get_one_complete(cls, data):
        query = "SELECT * FROM cars JOIN users ON cars.user_id = users.id JOIN makers ON cars.maker_id = makers.id WHERE cars.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        car = (cls(result[0]))
        users_data ={
            'id' : result[0]['users.id'],
            'first_name' : result[0]['first_name'],
            'last_name' : result[0]['last_name'],
            'email' : result[0]['email'],
            'created_at' : result[0]['users.created_at'],
            'updated_at' : result[0]['users.updated_at']
        }
        car.user = user.User(users_data)

        makers_data ={
            'id' : result[0]['makers.id'],
            'name' : result[0]['name'],
            'created_at' : result[0]['makers.created_at'],
            'updated_at' : result[0]['makers.updated_at']
        }
        car.maker = maker.Maker(makers_data)

        return car


    @classmethod
    def save(cls, data):
        print("data:", data)
        query = "INSERT INTO cars(color, year, created_at, updated_at, maker_id, user_id) VALUES(%(color)s, %(year)s, NOW(), NOW(), %(maker_id)s,  %(user_id)s);"

        data = {
            'color' : data['color'],
            'year' : data['year'],
            'maker_id' : data['maker_id'],
            'user_id' : data['user_id']
        }
        return connectToMySQL(cls.db).query_db(query, data) # returns id of object created/inserted


    @classmethod
    def update(cls, data):
        query = "UPDATE cars SET color = %(color)s, year = %(year)s, updated_at = NOW() WHERE cars.id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM cars WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)




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