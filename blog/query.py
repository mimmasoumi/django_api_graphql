import graphene
from blog.models import Comment, Post

from blog.types import CommentType, PostType


class Query(graphene.ObjectType):
    get_post = graphene.Field(PostType, id=graphene.ID())
    delete_post = graphene.Boolean(id=graphene.ID())

    get_comments = graphene.List(CommentType, id=graphene.ID())
    delete_comment = graphene.Boolean(id=graphene.ID())
    


    def resolve_get_post(self, info, id):
        post = Post.objects.get(id=id)
        if post:
            return post
        else:
            raise Exception("not found.")

    def resolve_delete_post(self, info, id):
        user = info.context.user

        if user.is_authenticated:
            post = Post.objects.get(id=id)
            if post:
                post.delete()
                return True
        return False

    def resolve_get_comments(self, info, id):
        comments = Comment.objects.filter(post_id=id)
        return comments

    def resolve_delete_comment(self, info, id):
        user = info.context.user

        if user.is_authenticated:
            comment = Comment.objects.get(id=id)
            if comment:
                comment.delete()
                return True
        return False



