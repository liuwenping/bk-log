# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making BK-LOG 蓝鲸日志平台 available.
Copyright (C) 2021 THL A29 Limited, a Tencent company.  All rights reserved.
BK-LOG 蓝鲸日志平台 is licensed under the MIT License.
License for BK-LOG 蓝鲸日志平台:
--------------------------------------------------------------------
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial
portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
We undertake not to change the open source license (MIT license) applicable to the current version of
the project delivered to anyone in the future.
"""
# Generated by Django 2.2.6 on 2021-06-16 14:42

from django.db import migrations, models
import django_jsonfield_backport.models


class Migration(migrations.Migration):

    dependencies = [
        ("log_search", "0033_auto_20210528_1655"),
    ]

    operations = [
        migrations.CreateModel(
            name="AsyncTask",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("request_param", django_jsonfield_backport.models.JSONField(verbose_name="检索请求参数")),
                (
                    "sorted_param",
                    django_jsonfield_backport.models.JSONField(blank=True, null=True, verbose_name="异步导出排序字段"),
                ),
                ("scenario_id", models.CharField(max_length=64, verbose_name="接入场景")),
                ("index_set_id", models.IntegerField(verbose_name="索引集id")),
                ("result", models.BooleanField(default=False, verbose_name="异步导出结果")),
                ("failed_reason", models.TextField(blank=True, null=True, verbose_name="异步导出异常原因")),
                ("file_name", models.CharField(blank=True, max_length=256, null=True, verbose_name="文件名")),
                ("file_size", models.FloatField(blank=True, null=True, verbose_name="文件大小")),
                ("download_url", models.TextField(blank=True, null=True, verbose_name="下载地址")),
                ("is_clean", models.BooleanField(default=False, verbose_name="是否被清理")),
            ],
            options={
                "verbose_name": "异步导出任务",
                "verbose_name_plural": "42_异步导出任务",
            },
        ),
        migrations.CreateModel(
            name="EmailTemplate",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="创建时间")),
                ("created_by", models.CharField(default="", max_length=32, verbose_name="创建者")),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True, null=True, verbose_name="更新时间")),
                ("updated_by", models.CharField(blank=True, default="", max_length=32, verbose_name="修改者")),
                ("name", models.CharField(db_index=True, max_length=128, verbose_name="模板名")),
                ("path", models.TextField(max_length=256, verbose_name="模板路径")),
                ("language", models.CharField(default="", max_length=128, verbose_name="语言级别")),
            ],
            options={
                "verbose_name": "邮件模板",
                "verbose_name_plural": "43_邮件模板",
            },
        ),
    ]
