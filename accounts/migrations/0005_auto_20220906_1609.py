# Generated by Django 3.2.15 on 2022-09-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220906_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCartItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('item_id', models.IntegerField()),
                ('name_uk', models.CharField(blank=True, max_length=200, null=True)),
                ('name_en', models.CharField(blank=True, max_length=200, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=45, null=True)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='usercart',
            options={'managed': True},
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]