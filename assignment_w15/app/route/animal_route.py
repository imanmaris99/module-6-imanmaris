from flask import Blueprint, jsonify, json, request


animal_blueprint = Blueprint('animal_endpoint', __name__)

animals = 'Temukan jenis-jenis Animals disini :', [
    {
        'id': 1,
        'Name':'Gajah',
        'Age': 20,
        'Gender':'Male',
        'Special Requirements':'Red Ivory'
    },
        
    {
        'id': 2,
        'Name':'Panda',
        'Age': 10,
        'Gender':'Female',
        'Special Requirements':'Black Belly'
    }
]

@animal_blueprint.route('/', methods=['GET'])
def get_animal():
    return jsonify(animals)

@animal_blueprint.route('/', methods=['POST'])
def create_animal():
    # Menerima data JSON yang dikirim oleh klien
    new_animal = request.json
    if new_animal:  # Pastikan data diterima
        animals.append(new_animal)
        return jsonify({'message': 'Animal baru berhasil ditambahkan'}), 201
    else:
        return jsonify({'error': 'Data Animal tidak ditemukan'}), 400

@animal_blueprint.route('/<int:animal_id>', methods=['PUT'])
def update_animal(animal_id):
        # Mendapatkan data JSON yang dikirim oleh klien
    updated_animal = request.json
    if updated_animal:  # Pastikan data diterima

        for animal in animals[1]:  # Melakukan iterasi melalui daftar Pokemon
            if animal['id'] == animal_id:  # Mencocokkan id dari animal

                animal.update(updated_animal)
                return jsonify({'message': 'Animal berhasil diperbarui'}), 200
        return jsonify({'error': 'Animal tidak ditemukan'}), 404
    else:
        return jsonify({'error': 'Data Animal tidak ditemukan'}), 400


@animal_blueprint.route('/<int:animal_id>', methods=['DELETE'])
def delete_animal(animal_id):
    for animal in animals:
        if animal['id'] == animal_id:

            animals.remove(animal)
            return jsonify({'message': 'Animal berhasil dihapus'}), 200
    return jsonify({'error': 'Animal tidak ditemukan'}), 404
