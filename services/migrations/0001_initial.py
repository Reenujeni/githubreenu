# Generated by Django 3.2.20 on 2023-11-07 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_code', models.IntegerField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('basic_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('hra', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pra_gain', models.DecimalField(decimal_places=2, max_digits=10)),
                ('att_bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pra_loss', models.DecimalField(decimal_places=2, max_digits=10)),
                ('esi', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lop', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_card', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payslip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=15)),
                ('year', models.IntegerField(default=2023)),
                ('total_days', models.IntegerField()),
                ('WOF_hrs', models.IntegerField()),
                ('WOF_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_days_worked', models.IntegerField()),
                ('absent_days', models.IntegerField()),
                ('overtime_hrs', models.IntegerField()),
                ('overtime_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_earnings', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gross_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_deductions', models.DecimalField(decimal_places=2, max_digits=10)),
                ('net_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.employee')),
            ],
        ),
    ]
