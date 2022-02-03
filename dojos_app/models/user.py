from dojos_app.config.mysqlconnection import connectToMySQL
from dojos_app.models import car

class User:
    db = 'cars_db'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        users_from_db = connectToMySQL(cls.db).query_db(query)
        users = []
        for user in users_from_db:
            #(cls(user))
            users.append(cls(user))
        return users


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM makers WHERE users.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        # (cls(car))
        return cls(result)


    @classmethod
    def get_one_complete(cls, data):
        query = "SELECT * FROM users LEFT JOIN cars ON cars.user_id = users.id WHERE users.id = %(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)
        user = (cls(result[0]))
        if result[0]['cars.id'] == None:
            return user
        else:
            for car_dic in result:
                car_data ={
                    'id' : car_dic['cars.id'],
                    'color' : car_dic['color'],
                    'year' : car_dic['year'],
                    'created_at' : car_dic['cars.created_at'],
                    'updated_at' : car_dic['cars.updated_at']
                }
                user.cars.append(car.Car.get_one_complete(car_data))
        return user
