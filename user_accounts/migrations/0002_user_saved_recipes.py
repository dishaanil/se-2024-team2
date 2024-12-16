# Generated by Django 5.1.2 on 2024-12-03 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_allergen_dietaryrestriction_remove_recipe_rating_and_more'),
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_recipes',
            field=models.ManyToManyField(blank=True, related_name='saved_by', to='recipes.recipe'),
        ),
    ]