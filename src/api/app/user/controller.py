from api.shared.encrypt_password import encrypt_pass, check_pass
from api.shared.validate_email import check_email
from api.shared.response import success_response, error_response
from api.models.index import db, User
from flask_jwt_extended import create_access_token

def register_user(body):
    try:
        if body is None:
            return error_response("Email o contrseña incorrectos.Por favor inténtalo de nuevo", 400)

        if "email" not in body or len(body["email"]) == 0:
            return error_response("Campo email está vacio. Por favor inténtalo de nuevo.", 400)

        if check_email(body["email"]) == False:
            return error_response("Email invalido. Por favor inténtalo de nuevo.", 400)

        if "password" not in body or len(body["password"]) == 0:
            return error_response("Campo contraseña está vacio. Por favor inténtalo de nuevo.", 400)

        hash_pass = encrypt_pass(body["password"])
        new_user = User(email=body["email"], password=hash_pass)

        db.session.add(new_user)
        db.session.commit()

        return success_response(new_user.serialize(), 201)

    except Exception as err:
        db.session.rollback()
        print("[ERROR REGISTER USER]: ", err)
        return error_response("Internal Server Error. Please, try again later.", 500)