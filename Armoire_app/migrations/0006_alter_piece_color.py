# Generated by Django 4.0.1 on 2022-02-12 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Armoire_app', '0005_alter_piece_category_alter_piece_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='color',
            field=models.CharField(choices=[('Red', 'Red'), ('Pink', 'Pink'), ('Orange', 'Orange'), ('Yellow', 'Yellow'), ('Green', 'Green'), ('Blue', 'Blue'), ('Indigo', 'Indigo'), ('Violet', 'Violet'), ('Beige', 'Beige'), ('Tan', 'Tan'), ('White', 'White'), ('Black', 'Black'), ('Brown', 'Brown'), ('Gray', 'Gray'), ('Multi-Color', 'Multi-Color')], default='White', max_length=32),
        ),
    ]
