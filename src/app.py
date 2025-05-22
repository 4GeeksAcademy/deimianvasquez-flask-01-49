from flask import Flask, request, jsonify


# instancia de la aplicación 
app = Flask(__name__)


# simulación de db
people = [
    {
        "id":1,
        "name":"Deimian Vásquez",
        "age": 18
    },
    {
        "id":2,
        "name":"Antonio Capra",
        "age": 21
    }
]


@app.route("/health_check") # decorador 
def health_check():
    return "ok", 200


@app.route("/person", methods=["POST"])
def add_person():
    if request.method == "POST":
        data = request.json

        if data.get("name") is None :
            return {"message": "debe contener name, age"}, 400
        if data.get("age") is None:
            return {"message": "debe contener name, age"}, 400

        
        data.update({"id": len(people)+1})
        people.append(data)

        return {"message": "El usuario se agrego exitosamente"}, 201


@app.route("/person", methods=["GET"])
def get_people():

    # aquí iria la lógica en caso de estar conectados a una db
    return jsonify(people), 200


@app.route("/person/<int:the_id>", methods=["GET"])
def get_one_people(the_id):
    
    result = list(filter(lambda item: item["id"] == the_id, people))
    
    if result:
        return jsonify(result[0]), 200
    else:
        return jsonify({"message":"NO se encontro la persona"}), 404

  
@app.route("/person/<int:the_id>", methods=["PUT"])
def update_person(the_id=None):
    data = request.json

    if data.get("name") is None :
        return {"message": "debe contener name, age"}, 400
    if data.get("age") is None:
        return {"message": "debe contener name, age"}, 400


    person = list(filter(lambda item: item["id"] == the_id, people))
 
    if person:
        new_person = person[0]
        new_person["name"] = data["name"]
        new_person["age"] = data.get("age")
        return jsonify(people), 201
    else:
        return jsonify({"message":"NO se encontro la persona"}), 404
    

@app.route("/person/<int:the_id>", methods=["DELETE"])
def delete_person(the_id=None):
    person = list(filter(lambda item: item["id"] == the_id, people))
    
    if person:
        people.remove(person[0])
        return [], 204
    else:
         return jsonify({"message":"NO se encontro la persona"}), 404



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True )

"""
    1.- Consultar todos los person --> /person --> GET ended
    2.- Consultar un usuario por id --> /person/id --> GET ended
    3.- Agregar una persona -->  /person --> POST ended
    4.- Eliminar un usuario --> /person --> DELETE 
    5.- Editar usuario --> /person/id --> PUT ended
"""