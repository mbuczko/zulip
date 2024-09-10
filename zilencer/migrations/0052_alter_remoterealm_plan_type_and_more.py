# Generated by Django 4.2.8 on 2023-12-13 23:20

from django.db import migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps

PLAN_TYPE_SELF_HOSTED = 1
PLAN_TYPE_SELF_MANAGED = 100


def renumber_plan_types(apps: StateApps, schema_editor: BaseDatabaseSchemaEditor) -> None:
    RemoteZulipServer = apps.get_model("zilencer", "RemoteZulipServer")
    RemoteRealm = apps.get_model("zilencer", "RemoteRealm")
    RemoteRealm.objects.filter(plan_type=PLAN_TYPE_SELF_HOSTED).update(
        plan_type=PLAN_TYPE_SELF_MANAGED
    )
    RemoteZulipServer.objects.filter(plan_type=PLAN_TYPE_SELF_HOSTED).update(
        plan_type=PLAN_TYPE_SELF_MANAGED
    )


class Migration(migrations.Migration):
    dependencies = [
        ("zilencer", "0051_remoterealm_is_system_bot_realm"),
    ]

    operations = [
        migrations.AlterField(
            model_name="remoterealm",
            name="plan_type",
            field=models.PositiveSmallIntegerField(db_index=True, default=PLAN_TYPE_SELF_MANAGED),
        ),
        migrations.AlterField(
            model_name="remotezulipserver",
            name="plan_type",
            field=models.PositiveSmallIntegerField(default=PLAN_TYPE_SELF_MANAGED),
        ),
        migrations.RunPython(
            renumber_plan_types, reverse_code=migrations.RunPython.noop, elidable=True
        ),
    ]
