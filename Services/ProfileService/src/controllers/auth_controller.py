from flask import request, Response, json, Blueprint

# user controller blueprint to be registered with api blueprint
auth = Blueprint("auth", __name__)

# route for login api/users/signin
@auth.route('/login', methods = ["POST", "GET"])
def handle_login():
    return Response(
        response=json.dumps({'status': "success"}),
        status=200,
        mimetype='application/json'
    )
