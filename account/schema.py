import graphene

from .mutation import Mutation

from .query import Query



schema = graphene.Schema(mutation=Mutation, query=Query)