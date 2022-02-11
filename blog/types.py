import graphene
from graphene_django import DjangoObjectType
from .models import Post, Comment


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "created")
    
    author = graphene.String()

    def resolve_author(self, info):
        return self.author.username

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ("id", "username", "content", "created")

