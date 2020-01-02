from django.urls import path
from . import views

urlpatterns=[
    path("",views.index),
    path("/onCharPress",views.onCharPress),
    path("/onFilePress",views.onFilePress),
    path("/after_fileInput",views.after_fileInput),
    path("/after_fileInput_updt",views.after_fileInput_updt),
    path("/after_charInput",views.after_charInput),
    path("/after_charInput_updt",views.after_charInput_updt),
    path("/after_updt",views.after_updt),
    path("/show_updates",views.show_updt),




]