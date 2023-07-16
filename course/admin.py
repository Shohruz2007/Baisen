from django.contrib import admin
from parler.admin import TranslatableAdmin
import functools
from django.core.paginator import Paginator
from django.db import connection, transaction, OperationalError
