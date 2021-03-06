# Generated by Django 3.1.7 on 2021-03-10 07:06

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Categoria de produto', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome do comprador', max_length=200)),
                ('endereco', models.CharField(help_text='Endereço para entrega da compra', max_length=200)),
                ('email', models.EmailField(help_text='E-mail de contato do comprador', max_length=200)),
                ('cpf', models.IntegerField(help_text='CPF do comprador')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nome', models.CharField(help_text='Nome do produto', max_length=200)),
                ('descricao', models.TextField(help_text='Descrição do produto', max_length=1000)),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço do produto', max_digits=9)),
                ('estoque', models.IntegerField(help_text='Quantidade em estoque do produto')),
                ('categoria', models.ManyToManyField(help_text='Categoria ao qual pertence o produto', to='catalogo.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('data', models.DateField(help_text='Data em que a compra foi realizada')),
                ('quantidade', models.IntegerField(help_text='Quantidade comprada do produto')),
                ('produto', models.ForeignKey(help_text='Produto comprado', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.produto')),
                ('usuario', models.ForeignKey(help_text='Usuário responsável pela compra', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalogo.usuario')),
            ],
        ),
    ]
