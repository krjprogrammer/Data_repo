from django.urls import path
from .views import EditDataModel, DeleteDataModel, CreateDataModel,GetDataModel
urlpatterns = [
    path('create_data_model',CreateDataModel.as_view()),
    path('edit_data_model',EditDataModel.as_view()),
    path('delete_data_model',DeleteDataModel.as_view()),
    path('get_data_model',GetDataModel.as_view())
]