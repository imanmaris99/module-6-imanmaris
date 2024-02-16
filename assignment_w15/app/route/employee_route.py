from flask import Blueprint, jsonify, request
from app.utils.database import db
from app.models.employee import Employee


employee_blueprint = Blueprint('customer_endpoint', __name__)

# @customer_blueprint.route('/', methods=['POST'])
# def create_customer():
#     try:
#         customer = Customer()
#         customer.name = "customer1"
#         customer.phone = 856778903
#         db.session.add(customer)
#         db.session.commit()
#         # return
#         # return 'sukses terdaftar', 200
#         return jsonify({'id': customer.id}),201
#     except Exception as e:
#         return 'Kesalahan server: {}'.format(str(e)), 500


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

        # Tambahkan pelanggan ke session database dan commit transaksi
        db.session.add(employee)
        db.session.commit()

        # Kirim respons JSON dengan ID pelanggan yang baru saja dibuat
        return jsonify({'id': employee.id}), 201
    except Exception as e:
        # Tangani kesalahan server jika ada
        return jsonify({'error': 'Kesalahan server: {}'.format(str(e))}), 500

@employee_blueprint.route('/', methods=['GET'])
def get_employees():
    try:
        employees = Employee.query.all()
        employee_list = [{'id': employee.id, 'name': employee.name, 'email': employee.email ,'phone': employee.phone} for employee in employees]
        return jsonify(employee_list), 200
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500

@employee_blueprint.route('/<int:customer_id>', methods=['DELETE'])
def delete_employee(employee_id):
    try:
        employee = Employee.query.get(employee_id)
        if employee:
            db.session.delete(employee)
            db.session.commit()
            return jsonify({'message': 'Customer deleted successfully'}), 200
        else:
            return jsonify({'message': 'Customer not found'}), 404
    except Exception as e:
        return 'Kesalahan server: {}'.format(str(e)), 500