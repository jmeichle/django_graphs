import time

from django.core.management.base import BaseCommand
from django.utils import timezone

from graphs.models import *

from IPython import embed

class Command(BaseCommand):

    help = 'Gimme a shell for graphs'

    def handle(self, *args, **kwargs):
        print("DB Models Loaded. Starting IPython")
        embed(using=False)