

def test_get_animals(test_app):
    response = test_app.get("/animal/")
    assert len(response.json['data']) == 10

def test_create_animal(test_app):
    data = {
            "age": 3,
            "gender": "Female",
            "special_requirement": "{\"paruh kuning\",\"leher pendek\"}",
            "species": "bebek"
        }
    response = test_app.post("/animal/", json=data)
    assert response.status_code == 201  

def test_create_animal_400(test_app):
    data = {}
    response = test_app.post("/animal/", json=data)
    assert response.status_code == 400 


def test_update_animal(test_app):
    data = {
        "species": "Unta",
        "age": 15,
        "special_requirement":"{2-Punuk,\"kaki panjang\"}"
    }
    response = test_app.put("/animal/3", json=data)
    print(response.json)
    assert response.status_code == 200


def test_update_animal_400(test_app):
    data = {}
    response = test_app.put("/animal/3", json=data)
    print(response.json)
    assert response.status_code == 400

    
def test_delete_animal(test_app):
    data = {
            "age": 5,
            "gender": "Female",
            "special_requirement": "{\"paruh merah\",\"leher panjang\"}",
            "species": "Angsa"
        }
    response = test_app.delete("/animal/15", json=data)
    assert response.status_code == 404  
    assert response.json['message'] == 'Binatang tidak terdaftar'
