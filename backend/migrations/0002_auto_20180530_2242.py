# Generated by Django 2.0.5 on 2018-05-30 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("backend", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="code",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="邮编"
            ),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="address",
            field=models.CharField(
                max_length=50, null=True, verbose_name="地址"
            ),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="logo",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="name",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="名称"
            ),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="summary",
            field=models.TextField(blank=True, verbose_name="简介"),
        ),
        migrations.AlterField(
            model_name="hotel",
            name="tel",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="电话"
            ),
        ),
    ]
