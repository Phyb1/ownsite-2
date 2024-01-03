# Generated by Django 4.2.1 on 2023-12-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteApp', '0003_comment_projects'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogs',
            options={'verbose_name_plural': 'Blogs'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name_plural': 'Projects'},
        ),
        migrations.AlterModelOptions(
            name='services',
            options={'verbose_name_plural': 'Services'},
        ),
        migrations.AddField(
            model_name='services',
            name='email',
            field=models.EmailField(default='phyb@swd.mi', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='order_type',
            field=models.CharField(choices=[('Website', 'website'), ('chatbot', 'chatbot'), ('digiMarketing', 'digital marketing'), ('restApi', 'restApi')], default='website', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='services',
            name='Orderdate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
