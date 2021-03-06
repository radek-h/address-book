# Generated by Django 2.2 on 2019-06-03 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address_book', '0010_auto_20190603_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='email',
            name='person',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='address_book.Person'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='person',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='address_book.Person'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]
