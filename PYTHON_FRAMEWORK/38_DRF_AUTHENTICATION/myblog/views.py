from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, APIView
from myblog.models import *
from myblog.serializers import *
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        Post.objects.create(title=title, content=content, author=author)
    
    posts = Post.objects.all().order_by('-created_at') 
    return render(request, 'index.html', {'posts': posts})


class PostAPI(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            allpost = Post.objects.all()
            ser = PostSerializer(allpost, many=True)
            return Response({'Post': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})
        
    def post(self, request):
        try:
            ser = PostSerializer(data=request.data)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'Post':ser.data, 'message':'Post created successfully.'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})


class PostAPIByID(APIView):
    def get(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            ser = PostSerializer(post)
            return Response({'Post':ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})
        
    def patch(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            ser = PostSerializer(post, request.data, partial=True)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'Post':ser.data, 'message':'Post updated successfully.'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})

    def delete(self, request, id):
        try:
            post = Post.objects.get(pk=id)
            post.delete()
            return Response({'message': 'Post deleted successfully.'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})
        









@api_view(['GET'])
def CommentList(request):
    try:
        allcomments = Comment.objects.all()
        ser = CommentSerializer(allcomments, many=True)
        return Response({'Comment': ser.data})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Exception occurred'})
    
@api_view(['POST'])
def CommentAdd(request, pid):
    try:
        post = Post.objects.get(pk = pid)
        data = request.data
        data['post'] = post.id
        ser = CommentSerializer(data=data)
        if not ser.is_valid():
            return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
        else:
            ser.save()
            return Response({'Comment': ser.data, 'message': 'Comment added successfully.'})
    except Exception as e:
        return Response({'errors': str(e), 'message': 'Exception occurred'})
    
class CommentAPIByID(APIView):
    def get(self, request, id):
        try:
            comment = Comment.objects.get(pk=id)
            ser = CommentSerializer(comment)
            return Response({'Comment': ser.data})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})

    def patch(self, request, id):
        try:
            comment = Comment.objects.get(pk=id)
            ser = CommentSerializer(comment, data=request.data, partial=True)
            if not ser.is_valid():
                return Response({'errors': ser.errors, 'message': 'Something went wrong.'})
            else:
                ser.save()
                return Response({'Comment': ser.data, 'message': 'Comment updated successfully.'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})

    def delete(self, request, id):
        try:
            comment = Comment.objects.get(pk=id)
            comment.delete()
            return Response({'message': 'Comment deleted successfully.'})
        except Exception as e:
            return Response({'errors': str(e), 'message': 'Exception occurred'})
  
    