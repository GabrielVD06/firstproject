import json
from flask import Flask, jsonify

app = Flask(__name__)

class Brand:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Car:
    def __init__(self, id, model, brand):
        self.id = id
        self.model = model
        self.brand = brand

    def to_dict(self):
        return {
            "id": self.id,
            "model": self.model,
            "brand": self.brand.name if isinstance(self.brand, Brand) else self.brand
        }

    def printCar(self):
        brand_name = self.brand.name if isinstance(self.brand, Brand) else self.brand
        print(f"{self.id} is the ID of the {brand_name} {self.model}")

# Instancias de Marca
brandOne = Brand("Peugeot", 1)
brandTwo = Brand("Ferrari", 2)
brandThree = Brand("Mazda", 3)

brandDictionary = {
    "1": brandOne,
    "2": brandTwo,
    "3": brandThree
}

# Instancias de Auto (pasando el objeto Brand completo en lugar de solo el string)
carOne = Car(1, "208", brandOne)
carTwo = Car(2, "206", brandOne)
carThree = Car(3, "LaFerrari", brandTwo)
carFour = Car(4, "Rx7", brandThree)
carFive = Car(5, "Miata", brandThree)

carDictionary = {
    "1": carOne,
    "2": carTwo,
    "3": carThree,
    "4": carFour,
    "5": carFive
}

# Endpoints de Flask

@app.route('/', methods=['GET'])
def homeall():
    # Convertimos los objetos Car a diccionarios para que jsonify pueda procesarlos
    cars_json = {car_id: car.to_dict() for car_id, car in carDictionary.items()}
    return jsonify(cars_json)

@app.route('/car/<string:car_id>', methods=['GET'])
def get_car_by_id(car_id):
    car = carDictionary.get(car_id)
    if not car:
        return jsonify({"error": "Auto no encontrado"}), 404
    return jsonify(car.to_dict())

@app.route('/<string:namex>', methods=['POST'])
def home2(namex):
    return jsonify({'data': f'hello world post {namex}'})

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
    app.run(debug=True) 