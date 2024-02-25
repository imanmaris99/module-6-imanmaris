from flask import Blueprint, jsonify, json, request
from app.models.feeding import Feeding
from app.utils.database import db
from app.utils.api_response import api_response
from app.service.feeding_service import Feeding_service
from app.controller.feeding.schema.create_feeding_request import Create_feeding_request
from pydantic import ValidationError

feeding_blueprint = Blueprint('feeding_endpoint', __name__)

@feeding_blueprint.route('/', methods=['POST'])
def create_feeding():
    try: 
        data = request.json
        update_feeding_request = Create_feeding_request(**data)

        feeding_service = Feeding_service()
        feedings = feeding_service.create_feeding(update_feeding_request)
        return api_response(
            status_code=201,
            message="success input data",
            data=feedings
        )
    
    except ValidationError as e:
        return api_response(
            status_code=400,
            message=e.errors(),
            data={  "contoh inputan ":
                    {
                        "animal_id":1,
                        "enclosure_id": 3,
                        "time": "{\"pagi:07.00-8.30\",\"siang:11.00-13.00\",\"malam:17.30-20.00}",
                        "food": "dedaunan"
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

@feeding_blueprint.route('/', methods=['GET'])
def get_feedings():
    try:
        feeding_service = Feeding_service()
        feedings = feeding_service.get_feedings()

        return api_response(
            status_code = 200,
            message ="Daftar semua karyawan sukses diakses",
            data = feedings
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )