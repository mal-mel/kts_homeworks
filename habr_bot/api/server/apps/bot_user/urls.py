from aiohttp import web

from server.apps.bot_user import views


def setup_urls(app: web.Application):
    app.router.add_view("/bot_user/register", views.RegisterView)
    app.router.add_view("/bot_user/get", views.GetUserView)
    app.router.add_view("/bot_user/set_shedule", views.SetSheduleView)
    app.router.add_view("/bot_user/get_tags", views.GetTagsView)
    app.router.add_view("/bot_user/add_tags", views.AddTagsView)
