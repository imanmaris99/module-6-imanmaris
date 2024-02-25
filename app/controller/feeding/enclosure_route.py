from flask import Blueprint, jsonify, json, request
from app.models.enclosure import Enclosure
from app.utils.database import db
from app.utils.api_response import api_response
from app.service.animal_service import Enclosure_service
from app.controller.feeding.schema.create_enclosure_request import Create_enclosure_request
from pydantic import ValidationError

enclosure_blueprint = Blueprint('enclosure_endpoint', __name__)

@enclosure_blueprint.route('/', methods=['POST'])
def create_enclosure():
    try: 
    # # Menerima data JSON yang dikirim oleh klien
    #     data = request.json

    # # Pastikan data yang diperlukan tersedia
    #     if 'location' not in data:
    #         return api_response(
    #             status_code=400,
    #             message="Lokasi harus diisi",
    #             data={  "contoh inputan ":
    #                     {
    #                         "location":"blok timur"
    #                     }                       
    #             }
    #         )   
    #     # Buat objek Customer dari data yang diterima
    #     enclosure = Enclosure()
    #     enclosure.location = data['location']

    #     # Tambahkan pelanggan ke session database dan commit transaksi
    #     db.session.add(enclosure)
    #     db.session.commit()
        
        data = request.json
        update_enclosure_request = Create_enclosure_request(**data)
        enclosure_service = Enclosure_service()
        enclosures = enclosure_service.create_enclosure(update_enclosure_request)

        return api_response(
            status_code=201,
            message="success input data",
            data=enclosures
        )
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={  "contoh inputan ":
                    {
                        "location":"blok timur"
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


@enclosure_blueprint.route('/', methods=['GET'])
def get_enclosures():
    try:
        enclosure_service = Enclosure_service()
        enclosures = enclosure_service.get_enclosures()

        return api_response(
            status_code=200,
            message="Daftar lokasi kandang sukses diakses",
            data=enclosures
        )  
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )  