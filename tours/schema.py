import graphene
from graphene_django.types import DjangoObjectType

from .models import Tour, Zona


class TourSchema(DjangoObjectType):
    class Meta:
        model = Tour


class ZonaSchema(DjangoObjectType):
    class Meta:
        model = Zona


class Query(graphene.ObjectType):

    all_tours = graphene.List(TourSchema)
    all_zonas = graphene.List(ZonaSchema)

    def resolve_all_tours(self, info, **kwargs):
        return Tour.objects.all()

    def resolve_all_zonas(self, info, **kwargs):
        return Zona.objects.all()


class CrearZona(graphene.Mutation):
    class Arguments:
        """ Define los argumentos para crear una Zona """
        nombre = graphene.String(required=True)
        descripcion = graphene.String()
        latitud = graphene.Decimal()
        longitud = graphene.Decimal()

    zona = graphene.Field(ZonaSchema)

    def mutate(self, info, nombre, descripcion=None, latitud=None,
        longitud=None):
        zona = Zona(
            nombre=nombre,
            descripcion=descripcion,
            latitud=latitud,
            longitud=longitud
        )
        zona.save()
        return CrearZona(zona=zona)


class EliminarZona(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            # Si la zona existe se elimina sin más
            zona = Zona.objects.get(pk=id)
            zona.delete()
            ok = True
        except Zona.DoesNotExist:
            # Si la zona no existe, se procesa la excepción
            ok = False
        # Se regresa una instancia de esta mutación
        return EliminarZona(ok=ok)


class Mutaciones(graphene.ObjectType):
    crear_zona = CrearZona.Field()
    eliminar_zona = EliminarZona.Field()

schema = graphene.Schema(query=Query, mutation=Mutaciones)
