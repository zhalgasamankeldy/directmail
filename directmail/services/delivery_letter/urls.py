
from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.LetterListView.as_view(),
        name='type-list'
    ),
    url(
        regex=r'^delivery/$',
        view=views.LetterFormView.as_view(),
        name='delivery'
    ),

]
