from django.urls import path
from . import views

# Setting up a name_space for template tagging.
app_name='basic_app' # this will tell django to go look for a view in this app_name(basic_app) when using relative urls

urlpatterns=[
  path('relative/', views.relative_url_templates, name="relative"),
  path('other/', views.other, name='other'),

]