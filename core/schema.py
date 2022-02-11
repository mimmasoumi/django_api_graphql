import graphene
import graphql_jwt
import account.schema as account
import blog.schema as blog

class Mutation(account.Mutation, blog.Mutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
    delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()

    pass

class Query(account.Query, blog.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)