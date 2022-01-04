import graphene
from graphene_django import DjangoObjectType
#from pkg_resources import require

from apps.core.models import *


# class Queries(graphene.ObjectType):
#     pass
#
#
# class Mutations(graphene.ObjectType):
#     pass
#
#

class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


# Consulta
class Queries(graphene.ObjectType):
    aulas = graphene.List(AulaType)

    def resolve_aulas(self, info, **kwargs):
        return Aula.objects.all()


class CrearAula(graphene.Mutation):
    aula = graphene.Field(AulaType)

    class Arguments:
        # Argumentos de la mutacion
        nombre = graphene.String(required=True)
        grado = graphene.String(required=True)

   # @classmethod
    def mutate(cls, root, info, nombre, grado):
        obj = Aula(nombre=nombre, grado=grado)
        obj.save()
        return CrearAula(aula=obj)


class AllMutation(graphene.ObjectType):
    CrearAula = CrearAula.Field()


schema = graphene.Schema(
    query=Queries,
    mutation=AllMutation,
)