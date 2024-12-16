# Generated by Django 5.1.2 on 2024-12-04 19:27

from django.db import migrations

def add_new_allergen(apps, schema_editor):
    # Get the Allergen model
    Allergen = apps.get_model('recipes', 'Allergen')

    # Add the new allergen
    new_allergen = "Sesame"
    Allergen.objects.get_or_create(name=new_allergen)


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_preload_allergens_and_restrictions'),
    ]

    operations = [
        migrations.RunPython(add_new_allergen)
    ]