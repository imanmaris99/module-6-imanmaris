from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employee import Employee


employee_blueprint = Blueprint('customer_endpoint', __name__)

@employee_blueprint.route('/', methods=['POST'])
def create_employee():
    try:
        # Ambil data pelanggan dari permintaan POST
        data = request.get_json()

        # Pastikan data yang diperlukan tersedia
        if 'name' not in data or 'phone' not in data:
            return jsonify({'error': 'Data karyawan tidak lengkap'}), 400

        # Buat objek Customer dari data yang diterima
        employee = Employee()
        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']
        employee.role = data['role']
        employee.schedule = data['schedule']

        # Tambahkan pelanggan ke session database dan commit transaksi
        db.session.add(employee)
        db.session.commit()

        # Kirim respons JSON dengan ID pelanggan yang baru saja dibuat
        return jsonify({'id': employee.id,'name': employee.name,'email': employee.email, 'phone': employee.phone, 'role': employee.role}), 201
    except Exception as e:
        # Tangani kesalahan server jika ada
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500

@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        employee_list = [{
            'id': employee.id, 
            'name': employee.name, 
            'email': employee.email ,
            'phone': employee.phone, 
            'role': employee.role,
            'schedule': employee.schedule} 
            for employee in employees]
        return jsonify(employee_list), 200
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500
    
@employee_blueprint.route('//<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)
        employee_list = [{'id': employee.id, 'name': employee.name, 'email': employee.email ,'phone': employee.phone, 'role': employee.role,'schedule': employee.schedule}]
        return jsonify(employee_list), 200
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500

@employee_blueprint.route('//<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)

        if not employee:
            return 'Karyawan tidak terdaftar', 404
        
        data = request.json

        employee.id = data['id']
        employee.name = data['name']
        employee.email = data['email']
        employee.phone = data['phone']
        employee.role = data['role']
        employee.schedule = data['schedule']

        db.session.commit()
        
        # Return success message along with updated customer details
        return {
            'Employee': {
                'id': employee.id,
                'name': employee.name,
                'phone': employee.phone,
                'role': employee.role,
                'schedule': employee.schedule
            }
        }, 200
    
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500


@employee_blueprint.route('/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return jsonify({'message': 'Data karyawan berhasil dihapus'}), 200
        else:
            return jsonify({'message': 'Karyawan tidak terdaftar'}), 404
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500