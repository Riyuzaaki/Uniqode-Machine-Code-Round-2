from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.utils import timezone
from api.schemas import CreatePostRequestData, CreatePostResponse
from api.models import Post, User, Vote
import traceback
from datetime import datetime
from django.db.models import Count




@api_view(['GET'])
def health_check(request):
    """
    Health check endpoint that returns the status of the application.
    
    Returns:
        JSON response with status and timestamp
    """
    return Response({
        'status': 'healthy',
        'timestamp': timezone.now().isoformat(),
        'service': 'Django API'
    }, status=status.HTTP_200_OK)


class PostView(APIView):
    def fetch_create_user(self, uuid):
        # import pdb
        # pdb.set_trace()
        user, _ = User.objects.get_or_create(username = uuid)
        return user
            
    def post(self, request):
        uuid = request.headers.get('id')
        user = self.fetch_create_user(uuid)
        request_data = CreatePostRequestData(**request.data)
        post = Post.objects.create(
            description = request_data.description,
            plans =  request_data.plans,
            category = request_data.category,
            user = user
        )
        return Response(CreatePostResponse(post_id=post.id).dict(), status=status.HTTP_200_OK)

class VoteView(APIView):
    def fetch_create_user(self, uuid):
        user, _ = User.objects.get_or_create(username = uuid)
        return user

    def validate_timestamp(self, post):
        return post.timestamp.date() == datetime.now().date()
        
    
    def post(self, request):
        uuid = request.headers.get('id')
        user = self.fetch_create_user(uuid)
        post_id = request.data.get("post_id")
        post = Post.objects.get(pk = post_id)
        if not self.validate_timestamp(post):
            return Response({"message": "Out of Time"}, status=status.HTTP_400_BAD_REQUEST)
        Vote.objects.create(user = user, post = post)
        return Response({"message": "Voted Added successfully"}, status=status.HTTP_201_CREATED)
        

class LeadbaordView(APIView):
    def get(self, request):
        top_posts = (
            Vote.objects
            .values('post_id')
            .annotate(num_of_vote=Count('user_id'))
            .order_by('-num_of_vote')[:10]
        )
        
        return Response({"data": top_posts}, status=status.HTTP_200_OK)
    

