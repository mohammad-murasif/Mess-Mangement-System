from import_export import resources
from .models import Person ,Student


class PersonResource(resources.ModelResource):
    class meta:
        model = Person


class StudentResource(resources.ModelResource):
    class meta:
        model=Student