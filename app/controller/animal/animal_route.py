from flask import Blueprint, jsonify, json, request
from app.models.animal import Animal
from app.utils.database import db
from app.utils.api_response import api_response
from app.service.animal_service import Animal_service
from app.controller.animal.schema.update_animal_request import Update_animal_request
from app.controller.animal.schema.create_animal_request import Create_animal_request
from pydantic import ValidationError

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route('/', methods=['POST'])
def create_animal():
    try: 
    # Menerima data JSON yang dikirim oleh klien
        data = request.json

    # # Pastikan data yang diperlukan tersedia
    #     if 'species' not in data or 'age' not in data:
    #         return api_response(
    #             status_code=400,
    #             message="Data kurang lengkap",
    #             data={  "contoh inputan ":
    #                     {
    #                         "age":8,
    #                         "gender": "Male",
    #                         "special_requirement": "{\"badan cokelat\",\"tanduk-2\"}",
    #                         "species": "Sapi"
    #                     }                       
    #             }
    #         )   

        create_animal_request = Create_animal_request(**data)

        animal_service = Animal_service()

        animals = animal_service.create_animal(create_animal_request)

        return api_response(
            status_code=201,
            message="success input data",
            data=animals
        )
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={  "contoh inputan ":
                    {
                        "age":8,
                        "gender": "Male",
                        "special_requirement": "{\"badan cokelat\",\"tanduk-2\"}",
                        "species": "Sapi"
                    }                       
                }
        )
    except Exception as e:
        # Tangani kesalahan server jika ada
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )       


@animal_blueprint.route('/', methods=['GET'])
def get_animals():
    try:
        animal_service = Animal_service()
        animals = animal_service.get_animals()

        return api_response(
            status_code=200,
            message="Daftar binatang sukses diakses",
            data=animals
        )  
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )       
    

@animal_blueprint.route('/search', methods=['GET'])
def search_animals():
    try:
        request_data = request.args
        
        animal_service = Animal_service()
        animals = animal_service.search_animals(request_data['species'])
        if animals:
        # return [animal.as_dict() for animal in animals], 200
            return api_response(
                status_code=200,
                message="Daftar binatang yang dicari sukses diakses",
                data=animals
            )  
        else:
            return api_response(
                status_code=400,
                message="Data binatang yang dicari tidak ditemukan",
                data={}
            )   
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )       


@animal_blueprint.route('//<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)
        if animal:
            return api_response(
                status_code=200,
                message="Data dari id binatang berhasil ditampilkan",
                data=[animal.as_dict()]
            )  
        else:
            return api_response(
                status_code=400,
                message="Data binatang tidak ditemukan",
                data={}
            )  
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )   
    
@animal_blueprint.route('//<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        data = request.json
        update_animal_request = Update_animal_request(**data)

        animal_service = Animal_service()
        animals = animal_service.update_animal(animal_id, update_animal_request)

        return api_response(
            status_code=200,
            message="success update data",
            data=animals
        )    

    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={}
        )     
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )   
    
@animal_blueprint.route('//<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    try:
        # animal = Animal.query.get(animal_id)
        animal_service = Animal_service()

        animal = animal_service.delete_animal(animal_id)
         
        if animal == "Animal not available":
            return api_response(
                status_code=404,
                message=animal,
                data={}
            )
        return api_response(
            status_code=200,
            message="Data binatang berhasil dihapus",
            data=animal
        )
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        ) 