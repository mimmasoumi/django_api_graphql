import graphene
from django.contrib.auth import get_user_model
from account.types import UserType
from account.utils import compare_password
from graphql_jwt.shortcuts import create_refresh_token, get_token

class CreateUserMutation(graphene.Mutation):
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        password2 = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, password2, email):
        if compare_password(password, password2):
            user = get_user_model()(
            username=username,
            email=email,
            )
            user.set_password(password)
            user.save()

            token = get_token(user)
            refresh_token = create_refresh_token(user)
            
            return CreateUserMutation(token=token, refresh_token=refresh_token)
        else:
            raise Exception("Password is not equal.")

class Mutation(graphene.ObjectType):
    # for create user
    create_user = CreateUserMutation.Field()
