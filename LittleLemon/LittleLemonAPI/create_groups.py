from django.contrib.auth.models import Group

def create_groups():
    Group.objects.get_or_create(name='Manager')
    Group.objects.get_or_create(name='Delivery Crew')

# Call the function to create the groups
create_groups()