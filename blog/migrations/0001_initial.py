# Generated by Django 3.2.8 on 2022-05-13 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('follower', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='dssdf sdjdsjfskdfsdfs dshfj', max_length=355, verbose_name='MAQOLA NOMI')),
                ('text', models.TextField(default="Text yo'q", max_length=8000, verbose_name='MAQOLA Matni')),
                ('view', models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(upload_to='')),
                ('checked', models.BooleanField(default=False)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='follower.fallower')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('article_qty', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='follower.fallower')),
                ('incomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category'),
        ),
    ]
