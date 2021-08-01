from api.apps.admin_user.accessor import AdminAccessor, SessionAccessor


class Store:
    def __init__(self):
        self.admin_user = AdminAccessor()
        self.session = SessionAccessor()
