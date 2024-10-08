# Generated by Django 5.1.1 on 2024-09-07 16:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='building_type',
            field=models.CharField(choices=[('home', 'Home'), ('outbuilding', 'Outbuilding')], default='home', max_length=15),
        ),
        migrations.CreateModel(
            name='BuildingDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='building_documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='buildings.building')),
            ],
        ),
    ]
