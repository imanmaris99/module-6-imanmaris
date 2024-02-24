
from app import db
from app.service.employee_service import Employee_service

# ----------------------START TEST GET EMPLOYEES-----------------------------------

def test_get_employees(test_app, mocker):
    # arrange
    mock_employee_data = [
        {
            "id":1,
            "name": "Salman",
            "email": "salmanan30@gmail.com",
            "phone":89989989990,
            "role": "Staff",
            "schedule": "non-shift => 07.00-16.00"
        }
    ]
    mocker.patch.object(Employee_service, 'get_employees', return_value=mock_employee_data)
    
    # act
    with test_app.test_client() as client:
        response = client.get("/employee/")

    # assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_employee_data)
    assert response.json['data'] == mock_employee_data

# ----------------------END TEST GET EMPLOYEES-----------------------------------
    

# # ----------------------START TEST CREATE/POST EMPLOYEES-----------------------------------
def test_create_employee(test_app, mocker):
    # Arrange
    data ={
            "name": "Sadiq",
            "email": "sadiq20@gmail.com",
            "phone":88889989990,
            "role": "Operator",
            "schedule": "shift-2 => 20.00-05.00"
        }

    mocker.patch.object(Employee_service, 'create_employee', return_value=data)

    # Act
    with test_app.test_client() as client:
        response = client.post("/employee/", json=data)

    # Assert
    assert response.status_code == 201 
    assert response.json['data'] == data 


def test_create_employee_400(test_app):
    # Arrange
    data = {}

    # Act
    with test_app.test_client() as client:
        response = client.post("/employee/", json=data)

    # Assert
    assert response.status_code == 400 
    assert response.json['data'] == {  "contoh inputan ":
                        {
                            "name":"Suherman",
                            "email": "manherman28@rocket.com",
                            "phone": 87767489,
                            "role": "manager",
                            "schedule": "non-shit:07.00-16.00"
                        }                      
                }
# # ----------------------END TEST CREATE EMPLOYEES-----------------------------------
    

# # ----------------------START TEST UPDATE/PUT EMPLOYEES-----------------------------------    
def test_update_employee(test_app, mocker):
    # arrange
    data = {
                "name":"Suherman",
                "email": "manherman28@rocket.com",
                "phone": 87767489,
                "role": "manager",
                "schedule": "non-shit:07.00-16.00"
    }
    mocker.patch.object(Employee_service, 'update_employee', return_value=data)

    # act
    with test_app.test_client() as client:
        response = client.put("/employee/3", json=data)
    
    # assert
    assert response.status_code == 200


def test_update_animal_400(test_app):
    # arrange
    data = {}

    # act
    with test_app.test_client() as client:
        response = client.put("/employee/3", json=data)
        
    # assert
    assert response.status_code == 400

# # ----------------------END TEST UPDATE EMPLOYEES-----------------------------------
    

# # ----------------------START TEST DELETE EMPLOYEES-----------------------------------   
    
def test_delete_animal(test_app, mocker):
    # arrange
    expected_response = {
            "name":"Suherman",
            "email": "manherman28@rocket.com",
            "phone": 87767489,
            "role": "manager",
            "schedule": "non-shit:07.00-16.00"
    } 
    mocker.patch.object(Employee_service, 'delete_employee', return_value=expected_response)
    
    # act
    with test_app.test_client() as client:
        response = client.delete("/employee/3")
    
    # assert                            
    assert response.status_code == 200  
    assert response.json['data'] == expected_response


# # ----------------------END TEST DELETE EMPLOYEES-----------------------------------
    
