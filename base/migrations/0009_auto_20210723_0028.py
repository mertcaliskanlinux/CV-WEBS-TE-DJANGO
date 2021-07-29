# Generated by Django 3.2.4 on 2021-07-23 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_contact_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='mert çalışkan', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='image',
            field=models.ImageField(default='media/kırmızıtsihrt.jpeg', upload_to='post/%Y%m%d/', verbose_name='BÜYÜK RESİMLER'),
        ),
    ]