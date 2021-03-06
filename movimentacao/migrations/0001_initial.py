# Generated by Django 4.0 on 2022-01-11 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conteiner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('EMBARQUE', 'EMBARQUE'), ('DESCARGA', 'DESCARGA'), ('GATE IN', 'GATE IN'), ('GATE OUT', 'GATE OUT'), ('REPOSICIONAMENTO', 'REPOSICIONAMENTO'), ('PESAGEM', 'PESAGEM'), ('SCANNER', 'SCANNER')], max_length=20)),
                ('inicio', models.DateTimeField(null=True, verbose_name='inicio')),
                ('fim', models.DateTimeField(null=True, verbose_name='fim')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='alterado em')),
                ('conteiner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='conteineres', to='conteiner.conteiner')),
            ],
            options={
                'verbose_name': 'Movimentação',
                'verbose_name_plural': 'Movimentações',
            },
        ),
    ]
