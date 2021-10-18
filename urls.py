from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('cotizador',views.cotizador,name='cotizador'),
    
    path('Recetas',views.recetas,name='recetas'),
    path('Recetas/add',views.RecetaAdd,name='Recetasadd'),
    path('Recetas/delete',views.RecetaDelete,name='Recetadelete'),
    path('Recetas/delete/<int:idre>',views.RecetaDeleteID,name='RecetadeleteID'),
    path('Recetas/get/<int:idre>',views.recetaGetId,name='recetaGetId'),
    path('Recetas/update/<int:recetaid>',views.RecetaUpdate,name='RecetaUpdate'),

    path('Ingredientes',views.ingredientes,name='ingredientes'),
    path('Ingredientes/add',views.ingredientesAdd,name='ingredientesAdd'),
    path('Ingredientes/delete',views.ingredientesDelete,name='ingredientesDelete'),
    path('Ingredientes/delete/<int:idIn>',views.ingredientesDeleteID,name='ingredientesDeleteID'),
    path('Ingredientes/<int:idin>',views.ingredientesGetId,name='ingredientesGetId'),
    path('Ingredientes/update/<int:in_id>',views.ingredientesUpdate,name='ingredientesUpdate'),
]