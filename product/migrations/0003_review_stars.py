# Generated by Django 4.1.7 on 2023-03-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_review_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(choices=[(1, '* '), (2, '* * '), (3, '* * * '), (4, '* * * * '), (5, '* * * * * ')], null=True),
        ),
    ]
