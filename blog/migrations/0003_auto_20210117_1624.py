# Generated by Django 2.2 on 2021-01-17 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210114_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='photo',
            field=models.FileField(default='pp.jpg', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artikel',
            name='isi',
            field=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipisicing elit. Et repudiandae reiciendis quos rem, consequatur debitis eveniet ullam perspiciatis cum eum?', max_length=300),
        ),
    ]