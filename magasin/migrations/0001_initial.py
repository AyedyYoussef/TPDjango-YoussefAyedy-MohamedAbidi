# Generated by Django 4.2 on 2023-04-26 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libellé', models.CharField(max_length=100)),
                ('description', models.TextField(default='non définie')),
                ('prix', models.DecimalField(decimal_places=3, default=0, max_digits=10)),
                ('type', models.CharField(choices=[('em', 'emballé'), ('fr', 'Frais'), ('cs', 'Conserve')], default='em', max_length=2)),
            ],
        ),
    ]
