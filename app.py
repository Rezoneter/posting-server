from flask import Flask
from flask_jwt_extended import JWTManager 
from flask_restful import Api
from config import Config
from resources.posting import PostingListResource

from resources.user import UserLoginResource, UserLogoutResource, UserRegisterResource, jwt_blocklist


app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)

@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload): 
    jti = jwt_payload['jti']
    return jti in jwt_blocklist


api = Api(app)

api.add_resource(UserRegisterResource,'/user/register')
api.add_resource(UserLoginResource,'/user/register')
api.add_resource(UserLogoutResource,'/user/logout')
api.add_resource(PostingListResource,'/posting')

if __name__ == '__main__':
    app.run()