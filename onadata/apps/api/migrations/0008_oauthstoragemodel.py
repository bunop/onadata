# Generated by Django 2.2.23 on 2021-07-28 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('api', '0007_odktoken_expires'),
    ]

    operations = [
        migrations.CreateModel(
            name='OauthStorageModel',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('credential', jsonfield.fields.JSONField(null=True)),
            ],
        ),
    ]
