import graphene
from blog.models import Post, Comment

from blog.types import CommentType, PostType


class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, title, content):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication Failure: Your must be signed in")
        else:
            post = Post(
                title=title,
                content=content,
                author = user
            )
            post.save()
            return CreatePost(post=post)

class UpdatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String(required=True)
        content = graphene.String(required=True)

    def mutate(self, info, title, content, id):
        user = info.context.user
        if user.is_anonymous:
            raise Exception("Authentication Failure: Your must be signed in")
        else:
            post = Post.objects.get(id=id)
            post.title = title
            post.content = content
            post.save()
            return CreatePost(post=post)

class CreateComment(graphene.Mutation):
    comment = graphene.Field(CommentType)

    class Arguments:
        username = graphene.String(required=True)
        content = graphene.String(required=True)
        post_id = graphene.ID()

    def mutate(self, info, username, content, post_id):
        user = info.context.user

        if user.is_authenticated:
            post = Post.objects.get(id=post_id)
            comment = Comment(
                username = username,
                content = content,
                post = post
            )
            comment.save()
            return CreateComment(comment)



class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()

    create_comment = CreateComment.Field()