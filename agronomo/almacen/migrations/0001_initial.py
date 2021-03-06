# Generated by Django 4.0.3 on 2022-03-20 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('establecimiento', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alta_almacen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('abreviatura', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True, max_length=255, null=True)),
                ('almacenes_tipo_id', models.CharField(blank=True, max_length=255, null=True)),
                ('geoposicion', models.CharField(blank=True, max_length=255, null=True)),
                ('observaciones', models.TextField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
                ('establecimiento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='establecimiento.alta_establecimientos')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
