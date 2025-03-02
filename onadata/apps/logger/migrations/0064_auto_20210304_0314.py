# Generated by Django 2.2.16 on 2021-03-04 08:14

from django.db import migrations

from onadata.apps.logger.models import XForm
from onadata.libs.utils.logger_tools import create_xform_version


def create_initial_xform_version(apps, schema_editor):
    """
    Creates an XFormVersion object for an XForm that has no
    Version
    """
    queryset = XForm.objects.filter(
        downloadable=True,
        deleted_at__isnull=True
    )
    for xform in queryset.iterator():
        if xform.version:
            create_xform_version(xform, xform.user)


class Migration(migrations.Migration):

    dependencies = [
        ('logger', '0063_xformversion'),
    ]

    operations = [
        migrations.RunPython(create_initial_xform_version)
    ]
