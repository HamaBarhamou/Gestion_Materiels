from django.contrib import admin
from .models import TypeMateriel,Personne,Gerant,Magasin,Materiel,Demande
# Register your models here.


admin.site.register(TypeMateriel)
admin.site.register(Personne)
admin.site.register(Gerant)
admin.site.register(Magasin)
admin.site.register(Materiel)
admin.site.register(Demande)
