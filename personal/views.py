from . import person_view;

################################
"""
Start - Person specific functions
"""

def person_list( request, template_name='personal/person_list.html'):
    person = person_view.person();
    return (person.person_list(request=request, template_name=template_name));

def person_create(request, template_name='personal/person_form.html'):
    # create a form instance and populate it with data from the request:
    person = person_view.person();
    pk = None;
    return (person.person_upsert( request, template_name, pk ));

def person_update(request, pk, template_name='personal/person_form.html'):
    person = person_view.person();
    return (person.person_upsert( request=request, template_name=template_name, person_id=pk ));

def person_delete(request, pk, template_name='personal/person_delete.html'):
    person = person_view.person();
    return (person.person_delete(request, pk, template_name));

"""
End - Person specific functions
"""
################################

