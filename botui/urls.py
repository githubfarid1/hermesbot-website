from django.urls import path
from botui import views
# print(__package__)
prefix = __package__ + "_"
urlpatterns = [
    path(route='urls', view=views.show_urls, name=prefix + "show_urls"),
    path(route='url_list', view=views.url_list, name=prefix + "url_list"),
    path(route='add_url', view=views.add_url, name=prefix + "add_url"),
    path(route='url/<int:pk>/edit', view=views.edit_url, name=prefix + "edit_url"),
    path(route='url/<int:pk>/remove', view=views.remove_url, name=prefix + 'remove_url'),

    path(route='settings', view=views.show_settings, name=prefix + "show_settings"),
    path(route='setting_list', view=views.setting_list, name=prefix + "setting_list"),
    path(route='setting/<int:pk>/edit', view=views.edit_setting, name=prefix + "edit_setting"),
    path(route='add_setting', view=views.add_setting, name=prefix + "add_setting"),

]