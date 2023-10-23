from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login),

    path('item/',item),
    path('itemdisplay/',item_display),
    path('itemedit/<int:id>',item_edit),
    path('itemdelete/<int:id>',item_delete),

    path('itempoints/',item_points),
    path('itempointsdisplay/',itempoints_display),
    path('itempointsedit/<int:id>',itempoints_edit),
    path('itempointsdelete/<int:id>',itempoints_delete),

    path('school/',school),
    path('schooldisplay/', school_display),
    path('schooledit/<int:id>',school_edit),
    path('schooldelete/<int:id>',school_delete),

    path('schoolpoints/', school_points),
    path('schoolpointsdisplay/', schoolpoints_display,name='school_display'),
    path('schoolpointsedit/<int:id>',schoolpoints_edit),
    path('schoolpointsdelete/<int:id>',schoolpoints_delete),

]