from django.urls import path, include
from wiki.views import PageListView, PageDetailView
from accounts.views import SignupView

urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]
