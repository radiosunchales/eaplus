# Generated by Django 4.0.3 on 2022-03-20 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        ('insumo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alta_empresas',
            name='rubro',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='insumo.rubros'),
        ),
    ]
