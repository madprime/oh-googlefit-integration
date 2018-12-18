# Generated by Django 2.1.4 on 2018-12-18 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openhumans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleFitMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=512)),
                ('refresh_token', models.CharField(max_length=512)),
                ('expiry_date', models.DateTimeField()),
                ('scope', models.CharField(max_length=512)),
                ('last_updated', models.DateTimeField(null=True)),
                ('last_submitted_for_update', models.DateTimeField(null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='googlefit_member', to='openhumans.OpenHumansMember')),
            ],
        ),
    ]
