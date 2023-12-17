from django.apps import AppConfig

import builtins
from pdb import set_trace

builtins.st = set_trace

class Base_AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_app'
