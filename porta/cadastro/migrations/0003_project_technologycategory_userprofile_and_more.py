# Generated by Django 4.1.3 on 2024-09-30 04:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cadastro', '0002_auto_20210301_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('stage', models.CharField(choices=[('ideia', 'Ideia'), ('em_progresso', 'Em Progresso'), ('completo', 'Completo')], max_length=50)),
                ('status', models.CharField(choices=[('ativo', 'Ativo'), ('inativo', 'Inativo'), ('concluido', 'Concluído')], default='ativo', max_length=50)),
                ('institution', models.CharField(blank=True, max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('funding_required', models.BooleanField(default=False)),
                ('goals', models.TextField(blank=True, null=True)),
                ('resources_needed', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TechnologyCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('pesquisador', 'Pesquisador'), ('estudante', 'Estudante'), ('empresa', 'Empresa'), ('instituicao', 'Instituição')], max_length=50)),
                ('bio', models.TextField(blank=True, null=True)),
                ('institution_name', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('linkedin', models.URLField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_report', models.TextField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress_updates', to='cadastro.project')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.technologycategory'),
        ),
        migrations.AddField(
            model_name='project',
            name='collaborators',
            field=models.ManyToManyField(blank=True, related_name='collaborations', to='cadastro.userprofile'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='cadastro.userprofile'),
        ),
        migrations.CreateModel(
            name='Patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patent_number', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=255)),
                ('abstract', models.TextField()),
                ('filing_date', models.DateField()),
                ('status', models.CharField(max_length=100)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patents', to='cadastro.project')),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=255)),
                ('partner_email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnership_requests', to='cadastro.project')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnership_requests_made', to='cadastro.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='PartnershipContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_details', models.TextField()),
                ('date_signed', models.DateTimeField(auto_now_add=True)),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.userprofile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='partnership_contracts', to='cadastro.project')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('is_read', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='cadastro.userprofile')),
            ],
        ),
        migrations.CreateModel(
            name='MentorshipRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('is_accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorship_offers', to='cadastro.userprofile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentorship_requests', to='cadastro.project')),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True, null=True)),
                ('contact_email', models.EmailField(max_length=254)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='institution_logos/')),
                ('technologies', models.ManyToManyField(blank=True, related_name='institution_projects', to='cadastro.project')),
            ],
        ),
        migrations.CreateModel(
            name='ImpactReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('views', models.IntegerField(default=0)),
                ('contacts', models.IntegerField(default=0)),
                ('partnerships', models.IntegerField(default=0)),
                ('date_generated', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impact_reports', to='cadastro.project')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='cadastro.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.userprofile')),
            ],
        ),
    ]
