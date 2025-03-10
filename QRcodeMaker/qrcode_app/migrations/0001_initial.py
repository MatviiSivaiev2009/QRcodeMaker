# Generated by Django 4.2.6 on 2025-02-28 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreateQr',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='images')),
                ('date', models.DateField()),
                ('link', models.TextField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
