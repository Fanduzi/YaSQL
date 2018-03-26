# Generated by Django 2.0.2 on 2018-03-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectManager', '0027_auto_20180321_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='incepmakeexectask',
            name='type',
            field=models.CharField(choices=[('DDL', '数据库定义语言'), ('DML', '数据库操纵语言')], default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='incepmakeexectask',
            name='exec_status',
            field=models.CharField(choices=[('0', '未执行'), ('1', '已完成'), ('2', '处理中'), ('3', '回滚中')], default='0', max_length=10, verbose_name='执行进度'),
        ),
    ]