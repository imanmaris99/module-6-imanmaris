from app.repositories.employee_repo import Employee_repo
from app.models.employee import Employee


class Employee_service:
    def __init__(self):
        self.employee_repo = Employee_repo()
    
    def get_employees(self):
        employees = self.employee_repo.get_list_employee()
        return [employee.as_dict() for employee in employees]

    def create_employee(self, employee_data_dto):
        employee = Employee()

        employee.name = employee_data_dto.name
        employee.email = employee_data_dto.email
        employee.phone = employee_data_dto.phone
        employee.role = employee_data_dto.role
        employee.schedule = employee_data_dto.schedule

        created_employee = self.employee_repo.create_employee(employee)
        return created_employee.as_dict()

    def update_employee(self, id, employee_data_dto):
        update_employee = self.employee_repo.get_update_employee(id, employee_data_dto)
        return update_employee.as_dict
    
    def delete_employee(self, id):
        employee = Employee.query.get(id)
        if not employee:
            return "Employee not available"
        
        delete_employee = self.employee_repo.delete_employee(id)
        return delete_employee.as_dict()
    
    def search_employees(self, name):
        employees = self.employee_repo.search_employees(name)
        return [employee.as_dict() for employee in employees]