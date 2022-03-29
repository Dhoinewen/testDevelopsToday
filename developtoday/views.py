from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .models import Post, Comments
from .serializers import PostSerializer, CommentsSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class CommentsAPIView(APIView):
    def get(self, request):
        comments = Comments.objects.all()
        return Response({'comments': CommentsSerializer(comments, many=True).data})

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'comment': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Put now allowed'})

        try:
            instance = Comments.objects.get(pk=pk)
        except:
            return Response({'error': 'Object not exists'})

        serializer = CommentsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self,  request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Put now allowed'})

        try:
            post = Comments.objects.get(pk=pk)
            post.delete()
            return Response({"Yep": 'Yep'})
        except:
            return Response({"error": 'Comment doest exist'})


# class PostAPIView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         return Response({'posts': PostSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method Put now allowed'})
#
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object not exists'})
#
#         serializer = PostSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self,  request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method Put now allowed'})
#
#         try:
#             post = Post.objects.get(pk=pk)
#             post.delete()
#             return Response({"Yep": 'Yep'})
#         except:
#             return Response({"error": 'Post doest exist'})
