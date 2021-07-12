# Generated by Django 3.2.5 on 2021-07-12 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('context', '0001_initial'),
        ('performance', '0002_auto_20210712_0010'),
        ('frase', '0002_alter_frase_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='frase',
            name='contextF',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='context.context'),
        ),
        migrations.AddField(
            model_name='frase',
            name='rendimiento',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='performance.performance'),
        ),
        migrations.AlterField(
            model_name='frase',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
