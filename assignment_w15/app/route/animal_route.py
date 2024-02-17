from flask import Blueprint, jsonify, json, request
from app.models.animal import Animal
from app.utils.database import db


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
        return jsonify({'id': animal.id,'species': animal.species,'age': animal.age, 'gender': animal.gender, 'special_requirement': animal.special_requirement}), 201
    except Exception as e:
        # Tangani kesalahan server jika ada
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500


@animal_blueprint.route('/', methods=['GET'])
def get_animals():
    try:
        animals = Animal.query.all()
        return [animal.as_dict() for animal in animals], 200
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
        # Cari animal berdasarkan ID
        animal = Animal.query.get(animal_id)

        # Periksa apakah animal ditemukan
        if not animal:
            return jsonify({'error': 'Animal tidak ditemukan'}), 404

        # Terima data JSON dari klien
        data = request.json

        # Periksa dan update data yang diberikan
        if 'species' in data:
            animal.species = data['species']
        if 'age' in data:
            animal.age = data['age']
        if 'gender' in data:
            animal.gender = data['gender']
        if 'special_requirement' in data:
            animal.special_requirement = data['special_requirement']

        # Commit perubahan ke database
        db.session.commit()

        # Kirim respons JSON bahwa animal telah diperbarui
        return jsonify({'id': animal.id,'species': animal.species,'age': animal.age,'gender': animal.gender,'special_requirement': animal.special_requirement}), 201
    except Exception as e:
        # Tangani kesalahan server jika terjadi
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500

@animal_blueprint.route('//<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    try:
        animal = Animal.query.get(animal_id)
        if animal:
            db.session.delete(animal)
            db.session.commit()
            return jsonify({'message': 'Data Binatang berhasil dihapus'}), 200
        else:
            return jsonify({'message': 'Binatang tidak terdaftar'}), 404
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500
