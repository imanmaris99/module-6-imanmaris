from flask import Blueprint, jsonify, request, json
# from app.utils.database import db
from app.models.employee import Employee
from app.service.employee_service import Employee_service
from app.utils.api_response import api_response
from app.controller.employee.schema.create_employee_request import Create_employee_request
from app.controller.employee.schema.update_employee_request import Update_employee_request
from pydantic import ValidationError

employee_blueprint = Blueprint('customer_endpoint', __name__)

@employee_blueprint.route('/', methods=['POST'])
def create_employee():
    try:
        # Ambil data pelanggan dari permintaan POST
        data = request.json

        # Pastikan data yang diperlukan tersedia
        if 'name' not in data or 'phone' not in data:
            return api_response(
                status_code=400,
                message="Data kurang lengkap",
                data={  "contoh inputan ":
                        {
                            "name":"Suherman",
                            "email": "manherman28@rocket.com",
                            "phone": 87767489,
                            "role": "manager",
                            "schedule": "non-shit:07.00-16.00"
                        }                       
                }
            )  
        # # Buat objek Customer dari data yang diterima
        # employee = Employee()
        # employee.name = data['name']
        # employee.email = data['email']
        # employee.phone = data['phone']
        # employee.role = data['role']
        # employee.schedule = data['schedule']

        # # Tambahkan pelanggan ke session database dan commit transaksi
        # db.session.add(employee)
        # db.session.commit()

        Update_employee_request = Create_employee_request(**data)

        employee_service = Employee_service()

        employees = employee_service.create_employee(Update_employee_request)

        return api_response(
            status_code=201,
            message="success input data",
            data=employees
        )
    
    except Exception as e:
        # Tangani kesalahan server jika ada
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )  
    
@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    try:
        
        employee_service = Employee_service()
        employees = employee_service.get_employees()
        # return employees
        return api_response(
            status_code = 200,
            message ="Daftar semua karyawan sukses diakses",
            data = employees
        )
    
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )   
    
@employee_blueprint.route('//<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)
        if employee:
            return api_response(
                status_code=200,
                message="Daftar data dari id karyawan berhasil ditampilkan",
                data=[employee.as_dict()]
            )  
        else:
            return api_response(
                status_code=400,
                message="Data karyawan tidak ditemukan",
                data={}
            )  
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        ) 

@employee_blueprint.route('//<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:

        data = request.json
        update_employee_request = Update_employee_request(**data)
        print(update_employee_request)

        employee_service = Employee_service()
        employees = employee_service.update_employee(employee_id, update_employee_request)

        return api_response(
            status_code=200,
            message="succes update employee data",
            data=employees
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

@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        employe_service = Employee_service()
        employee = employe_service.delete_employee(employee_id)
        if employee == "Employee not available":
            return api_response(
            status_code=404,
            message=employee,
            data={}
        )
        return api_response(
            status_code=200,
            message="Data karyawan berhasil dihapus (sudah resign)",
            data=employee
        )    
        
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        ) 
    
@employee_blueprint.route('/search', methods=['GET'])
def search_employees():
    try:
        request_data = request.args
        
        employee_service = Employee_service()
        employees = employee_service.search_employees(request_data['name'])
        if employees:
        # return [animal.as_dict() for animal in animals], 200
            return api_response(
                status_code=200,
                message="Daftar data karyawan yang dicari sukses diakses",
                data=employees
            )  
        else:
            return api_response(
                status_code=400,
                message="Data karyawan yang dicari tidak ditemukan",
                data={}
            )   
    except Exception as e:
        return api_response(
            status_code=500,
            message=str(e),
            data={}
        )       
