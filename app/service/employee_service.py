from app.repositories import employee_repo

def get_employees():
    employees = employee_repo.get_list_employee()
    return [employee.as_dict() for employee in employees], 200

def update_employee(employee_id):
    employee = employee_repo.get_update_employee(employee_id)
    return employee