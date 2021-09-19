# Generated by Django 3.2.7 on 2021-09-19 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_alter_продукт_категория'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='продукт',
            name='cрок_действия_скидки_до',
        ),
        migrations.RemoveField(
            model_name='продукт',
            name='cрок_действия_скидки_от',
        ),
        migrations.AlterField(
            model_name='shopcategory',
            name='category_id',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Id категории'),
        ),
        migrations.AlterField(
            model_name='продукт',
            name='описание_укр',
            field=models.TextField(blank=True, db_column='Описание_укр', max_length=6656, null=True),
        ),
        migrations.AlterField(
            model_name='продукт',
            name='скидка',
            field=models.IntegerField(blank=True, db_column='Скидка', default='0', null=True, verbose_name='Скидка (%)'),
        ),
    ]
