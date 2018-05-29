# Generated by Django 2.0.5 on 2018-05-29 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("phone", models.CharField(max_length=30, verbose_name="手机")),
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="姓名"
                    ),
                ),
                (
                    "id_card",
                    models.CharField(
                        blank=True,
                        max_length=30,
                        null=True,
                        verbose_name="身份证",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tel", models.CharField(max_length=30, verbose_name="电话")),
                ("name", models.CharField(max_length=30, verbose_name="名称")),
                (
                    "address",
                    models.CharField(max_length=50, verbose_name="地址"),
                ),
                ("summary", models.TextField(verbose_name="简介")),
                ("logo", models.ImageField(null=True, upload_to="images")),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("begin", models.DateField(verbose_name="入住时间")),
                ("end", models.DateField(verbose_name="离店时间")),
                ("totalprice", models.IntegerField(verbose_name="需支付金额")),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("will", "预定中"),
                            ("run", "执行中"),
                            ("end", "已结束"),
                            ("destroyed", "已废弃"),
                        ],
                        max_length=45,
                        verbose_name="订单状态",
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.Customer",
                        verbose_name="顾客",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Poster",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "img",
                    models.ImageField(
                        null=True, upload_to="images", verbose_name="海报"
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=None, to="backend.Hotel", verbose_name="酒店"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=30,
                        primary_key=True,
                        serialize=False,
                        verbose_name="房间号",
                    ),
                ),
                (
                    "area",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="面积"
                    ),
                ),
                ("summary", models.TextField(verbose_name="简介")),
            ],
        ),
        migrations.CreateModel(
            name="RoomType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "detail",
                    models.CharField(
                        choices=[
                            ("standard", "标准间"),
                            ("better", "豪华间"),
                            ("president", "总统间"),
                        ],
                        max_length=30,
                        verbose_name="类型",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="价格"
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=None, to="backend.Hotel", verbose_name="酒店"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="room",
            name="roomtype",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=None,
                to="backend.RoomType",
                verbose_name="房间类型",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="room",
            field=models.ForeignKey(
                on_delete=None, to="backend.Room", verbose_name="酒店"
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="roomtype",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=None,
                to="backend.RoomType",
                verbose_name="房间类型",
            ),
        ),
    ]
