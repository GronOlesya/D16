import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Title ')),
                ('text_body', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Text')),
                ('category', models.CharField(choices=[('tanks', 'Танки'), ('healers', 'Хилы'), ('damage dealers', 'ДД'), ('merchants', 'Торговцы'), ('guild masters', 'Гильдмастеры'), ('questgivers', 'Квестгиверы'), ('blacksmiths', 'Администратор'), ('leatherworkers', 'Кожевники'), ('potions makers', 'Зельевары'), ('spell masters', 'Мастера заклинаний')], default='tank', max_length=20)),
                ('upload', models.FileField(upload_to='uploads/')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Publication date ')),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('news_susbscribed', models.BooleanField(default=False, verbose_name='Newsletter subscription')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_body', models.TextField(verbose_name='Comment Text')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('approved_comment', models.BooleanField(blank=True, default=False, null=True)),
                ('author', models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='board.article')),
            ],
        ),
    ]
