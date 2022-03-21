# Generated by Django 4.0.3 on 2022-03-20 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0002_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoria_usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('tipo_accion', models.CharField(max_length=255)),
                ('tabla_modificada', models.CharField(blank=True, max_length=255, null=True)),
                ('registro_modificado', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol_descripcion', models.CharField(blank=True, max_length=255, null=True)),
                ('tipo_acceso_id', models.CharField(max_length=255)),
                ('menu_acceso', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alta_usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('nombre', models.CharField(blank=True, max_length=255, null=True)),
                ('apellido', models.CharField(blank=True, max_length=255, null=True)),
                ('dni', models.IntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(db_column='activo', default=True, verbose_name='activo')),
                ('is_staff', models.BooleanField(db_column='rol', default=False, verbose_name='rol')),
                ('fecha_alta', models.DateField(auto_now_add=True)),
                ('fecha_baja', models.DateField(blank=True, null=True)),
                ('empresa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='empresa.alta_empresas')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
