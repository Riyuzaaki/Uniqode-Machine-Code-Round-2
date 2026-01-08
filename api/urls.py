from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('create-post/', views.PostView.as_view(), name="create-post" ),
    path('add-vote/', views.VoteView.as_view(), name="add-vote" ),
    path('leaderboard/', views.LeadbaordView.as_view(), name="leaderboard" )
]

