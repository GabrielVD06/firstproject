from flask import Flask, jsonify
app = Flask(__name__)
import json


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
            "model": self.model
#            "brand": self.brand.name
        }
  def printCar(self):
     print(f"{self.id} is the ID of the {self.brand} {self.model}")

brandOne = Brand("Peugeot", 1)
brandTwo = Brand("Ferrari", 2)
brandThree = Brand("Mazda", 3)

brandDictionary = {}
brandDictionary["1"] = brandOne
brandDictionary["2"] = brandTwo
brandDictionary["3"] = brandThree

carOne = Car(1, "208", brandOne.name)
carOne.printCar()
carTwo = Car(2, "206", brandOne.name)
carTwo.printCar()
carThree = Car(3, "LaFerrari", brandTwo.name)
carThree.printCar()
carFour = Car(4, "Rx7", brandThree.name)
carFour.printCar()
carFive = Car(5, "Miata", brandThree.name)
carFive.printCar()

carDictionary = {}
carDictionary["1"] = carOne
carDictionary["2"] = carTwo
carDictionary["3"] = carThree
carDictionary["4"] = carFour
carDictionary["5"] = carFive

print(carDictionary["1"])

@app.route('/', methods=['GET'])
def homeall():
    return jsonify(carDictionary)

@app.route('/1', methods=['GET'])
def homebyid1():
    return jsonify('Peugeot', str(brandDictionary["1"]))
@app.route('/2', methods=['GET'])
def homebyid2():
    return jsonify('Peugeot' + str(brandDictionary["2"]))
@app.route('/3', methods=['GET'])
def homebyid3():
    return jsonify('Peugeot' + str(brandDictionary["1"]))


@app.route('/<string:namex>', methods=['POST'])
def home2(namex):
    return jsonify({'data': f'hello world post {namex}'})

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})

if __name__ == '__main__':
    app.run(debug=True)