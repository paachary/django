from django.shortcuts import render, redirect, get_object_or_404;

from django_tables2 import RequestConfig;

from django.http import HttpResponseRedirect;

from .models import Bank;

from .tables import PersonTable;

## An individual class specific for person whose methods and invoked from the django view
class person:


