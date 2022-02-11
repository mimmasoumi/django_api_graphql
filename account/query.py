import graphene

from account.types import UserType


class Query(graphene.ObjectType):
    whoami = graphene.Field(UserType)

    def resolve_whoami(self, info):
        user = info.context.user
        # Check to to ensure  user is signed in or not
        if user.is_anonymous:
            raise Exception('Authentication Failure: Your must be signed in')
        return user


