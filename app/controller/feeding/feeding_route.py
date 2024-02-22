from flask import Blueprint, jsonify, json, request
from app.models.feeding import Feeding
from app.utils.database import db
from app.utils.api_response import api_response
from app.service import feeding_service


feeding_blueprint = Blueprint('feeding_endpoint', __name__)

@feeding_blueprint.route('/', methods=['POST'])
def create_feeding():
    try: 
    # Menerima data JSON yang dikirim oleh klien
        data = request.json

    # Pastikan data yang diperlukan tersedia
        if 'animal_id' not in data or 'enclosure_id' not in data:
            return api_response(
                status_code=400,
                message="Data kurang lengkap",
                data={  "contoh inputan ":
                        {
                            "animal_id":1,
                            "enclosure_id": 3,
                            "time": "{\"pagi:07.00-8.30\",\"siang:11.00-13.00\",\"malam:17.30-20.00}",
                            "food": "dedaunan"
                        }                       
                }
            )   
        # Buat objek Customer dari data yang diterima
        feeding = Feeding()
        feeding.animal_id = data['animal_id']
        feeding.enclosure_id = data['enclosure_id']
        feeding.time = data['time']
        feeding.food = data['food']

        # Tambahkan pelanggan ke session database dan commit transaksi
        db.session.add(feeding)
        db.session.commit()

        # Kirim respons JSON dengan ID pelanggan yang baru saja dibuat
        # return jsonify({'id': animal.id,'species': animal.species,'age': animal.age, 'gender': animal.gender, 'special_requirement': animal.special_requirement}), 201
        return api_response(
            status_code=201,
            message="success input data",
            data=[feeding.as_dict()]
        )
    except Exception as e:
        # Tangani kesalahan server jika ada
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )       

@feeding_blueprint.route('/', methods=['GET'])
def get_feedings():
    try:
        feedings = feeding_service.get_feedings()
        # return employees
        return api_response(
            status_code = 200,
            message ="Daftar semua karyawan sukses diakses",
            data = feedings
        )
    
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500