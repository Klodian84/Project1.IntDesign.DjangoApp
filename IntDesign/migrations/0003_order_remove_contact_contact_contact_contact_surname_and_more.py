# Generated by Django 5.1.2 on 2024-11-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("IntDesign", "0002_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=100)),
                ("Surname", models.CharField(max_length=100)),
                ("phone", models.IntegerField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "service",
                    models.CharField(
                        choices=[
                            ("Residential Decoration", "Residential Decoration"),
                            ("Ecommercial Decoration", "Ecommercial Decoration"),
                            ("Office Decoration", "Office Decoration"),
                        ],
                        max_length=100,
                    ),
                ),
                ("date_created", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name="contact",
            name="contact",
        ),
        migrations.AddField(
            model_name="contact",
            name="contact_surname",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="datetime",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_description",
            field=models.TextField(verbose_name="Project description"),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_name",
            field=models.CharField(max_length=100, verbose_name="Project NAme"),
        ),
    ]
