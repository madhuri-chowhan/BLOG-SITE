# Generated by Django 3.2.9 on 2021-11-29 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0003_auto_20211129_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='blogpage',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='app_blog.name'),
        ),
    ]