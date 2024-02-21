
from app.models.employee import Employee

def get_list_employee():
    employees = Employee.query.all()
    return employees

def get_update_employee(employee_id):
    employee = Employee.query.get(employee_id)
    return employee