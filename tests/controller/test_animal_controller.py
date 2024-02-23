
from app import db
from app.service.animal_service import Animal_service

# ----------------------START TEST GET ANIMALS-----------------------------------

def test_get_animals(test_app, mocker):
    # arrange
    mock_animal_data = [
        {
            "age": 3,
            "gender": "Female",
            "id":1,
            "special_requirement": "{\"paruh kuning\",\"leher pendek\"}",
            "species": "bebek"
        }
    ]
    mocker.patch.object(Animal_service, 'get_animals', return_value=mock_animal_data)
    
    # act
    with test_app.test_client() as client:
        response = client.get("/animal/")

    # assert
    assert response.status_code == 200
    assert len(response.json['data']) == len(mock_animal_data)
    assert response.json['data'] == mock_animal_data

# ----------------------END TEST GET ANIMALS-----------------------------------
    

# ----------------------START TEST CREATE/POST ANIMALS-----------------------------------
def test_create_animal(test_app, mocker):
    # Arrange
    data = {
        "age": 3,
        "gender": "Female",
        "special_requirement": "{\"paruh merah\",\"leher panjang\"}",
        "species": "angsa"
    }

    mocker.patch.object(Animal_service, 'create_animal', return_value=data)

    # Act
    with test_app.test_client() as client:
        response = client.post("/animal/", json=data)

    # Assert
    assert response.status_code == 201 
    assert response.json['data'] == data 

def test_create_animal_400(test_app):
    # Arrange
    data = {}

    # Act
    with test_app.test_client() as client:
        response = client.post("/animal/", json=data)

    # Assert
    assert response.status_code == 400 
    assert response.json['data'] == {  "contoh inputan ":
                        {
                            "age":8,
                            "gender": "Male",
                            "special_requirement": "{\"badan cokelat\",\"tanduk-2\"}",
                            "species": "Sapi"
                        }                       
                }
# ----------------------END TEST CREATE ANIMALS-----------------------------------
    

# ----------------------START TEST UPDATE/PUT ANIMALS-----------------------------------    
def test_update_animal(test_app, mocker):
    # arrange
    data = {
        "age": 3,
        "gender": "Male",
        "special_requirement": "{\"paruh merah\",\"leher panjang\"}",
        "species": "angsa"
    }
    mocker.patch.object(Animal_service, 'update_animal', return_value=data)

    # act
    with test_app.test_client() as client:
        response = client.put("/animal/3", json=data)
    
    # assert
    assert response.status_code == 200


def test_update_animal_400(test_app):
    # arrange
    data = {}

    # act
    with test_app.test_client() as client:
        response = client.put("/animal/3", json=data)
        
    # assert
    assert response.status_code == 400

# ----------------------END TEST UPDATE ANIMALS-----------------------------------
    

# ----------------------START TEST DELETE ANIMALS-----------------------------------   
    
def test_delete_animal(test_app, mocker):
    # arrange
    expected_response = {
            "age": 3,
            "gender": "Female",
            "special_requirement": "{\"paruh kuning\",\"leher pendek\"}",
            "species": "bebek"
    }
    mocker.patch.object(Animal_service, 'delete_animal', return_value=expected_response)
    
    # act
    with test_app.test_client() as client:
        response = client.delete("/animal/3")
    
    # assert                            #  )
    assert response.status_code == 200  
    assert response.json['data'] == expected_response


# ----------------------END TEST DELETE ANIMALS-----------------------------------
    
