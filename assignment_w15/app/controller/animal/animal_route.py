from flask import Blueprint, jsonify, json, request
from app.models.animal import Animal
from app.utils.database import db
from app.utils.api_response import api_response
from app.service.animal_service import Animal_service
from app.controller.animal.schema.update_animal_request import Update_animal_request
from pydantic import ValidationError

animal_blueprint = Blueprint('animal_endpoint', __name__)

@animal_blueprint.route('/', methods=['POST'])
def create_animal():
    try: 
    # Menerima data JSON yang dikirim oleh klien
        data = request.json

    # Pastikan data yang diperlukan tersedia
        if 'species' not in data or 'age' not in data:
            return jsonify({'error': 'Data binatang tidak lengkap'}), 400

        # Buat objek Customer dari data yang diterima
        animal = Animal()
        animal.species = data['species']
        animal.age = data['age']
        animal.gender = data['gender']
        animal.special_requirement = data['special_requirement']

        # Tambahkan pelanggan ke session database dan commit transaksi
        db.session.add(animal)
        db.session.commit()

        # Kirim respons JSON dengan ID pelanggan yang baru saja dibuat
        # return jsonify({'id': animal.id,'species': animal.species,'age': animal.age, 'gender': animal.gender, 'special_requirement': animal.special_requirement}), 201
        return api_response(
            status_code=201,
            message="success input data",
            data=[animal.as_dict()]
        )
    
    except Exception as e:
        # Tangani kesalahan server jika ada
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500


@animal_blueprint.route('/', methods=['GET'])
def get_animals():
    try:
        animal_service = Animal_service()
        animals = animal_service.get_animals()
        # return [animal.as_dict() for animal in animals], 200
        return api_response(
            status_code=201,
            message="Daftar binatang sukses diakses",
            data=animals
        )  

    except Exception as e:
        return e, 500
    

@animal_blueprint.route('/search', methods=['GET'])
def search_animals():
    try:
        request_data = request.args

        animal_service = Animal_service()
        animals = animal_service.search_animals(request_data['species'])

        # return [animal.as_dict() for animal in animals], 200
        return api_response(
            status_code=200,
            message="Daftar binatang yang dicari sukses diakses",
            data=animals
        )  

    except Exception as e:
        return e, 500
    


@animal_blueprint.route('//<int:animal_id>', methods=['GET'])
def get_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)
        return animal.as_dict(), 200
    except Exception as e:
        return e, 500

@animal_blueprint.route('//<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
    try:
        # Cara pertama tanpa pemakaian DTO-------------
        # data = request.json
        # update_animal_request = Update_animal_request(**data)
        # print(update_animal_request)

        # animal= Animal()
        # animal.species = update_animal_request.species
        # animal.age = update_animal_request.age
        # animal.gender = update_animal_request.gender
        # animal.special_requirement = update_animal_request.special_requirement

        # animal_service = Animal_service()

        # animals = animal_service.update_animal(animal_id, animal)
        # return api_response(
        #     status_code=200,
        #     message="success update data",
        #     data=[animal.as_dict()]
        # )
        # ----------------------------------------------   

        data = request.json
        update_animal_request = Update_animal_request(**data)
        print(update_animal_request)

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
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500

@animal_blueprint.route('//<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)
        if animal:
            db.session.delete(animal)
            db.session.commit()
            # return jsonify({'message': 'Data Binatang berhasil dihapus'}), 200
            return api_response(
            status_code=200,
            message="Data binatang berhasil dihapus",
            data=[animal.as_dict()]
        )
        else:
            return jsonify({'message': 'Binatang tidak terdaftar'}), 404
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500
