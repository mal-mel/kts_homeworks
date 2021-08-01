from aiohttp import web
from aiohttp_apispec import json_schema, response_schema

from api.web.view import BaseView

from .accessor import AdminUser, Login


class AddUserView(BaseView):
    @json_schema(AdminUser.Schema)
    @response_schema(AdminUser.Schema)
    async def post(self):
        data: AdminUser = self.request["json"]
        return self.store.admin_user.add_user(data)


class LoginView(BaseView):
    @json_schema(Login.Schema)
    @response_schema(AdminUser.Schema)
    async def post(self):
        data: Login = self.request["json"]
        session = self.store.session.generate_session(data.username)
        response = web.json_response({"data": AdminUser.Schema().dump(data)})
        response.set_cookie("session_id", session.id)
        return response
