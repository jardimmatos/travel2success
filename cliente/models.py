from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255, blank=False, null=True, verbose_name='Nome')
    documento = models.CharField(max_length=20, blank=False, null=True, unique=True, 
                    verbose_name='Documento', error_messages={ 
                        "unique": "Já existe um cliente com o documento informado!"
                    })
    cep = models.CharField(max_length=9, blank=True, null=True, verbose_name='CEP')
    endereco = models.CharField(max_length=255, blank=True, null=True, verbose_name='Endereço')
    bairro = models.CharField(max_length=255, blank=True, null=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=255, blank=True, null=True, verbose_name='Cidade')
    uf = models.CharField(max_length=255, blank=True, null=True, verbose_name='U.F.')

    created_at = models.DateTimeField('criado em', auto_now_add=True, auto_now=False, null=True)
    updated_at = models.DateTimeField('alterado em', auto_now_add=False, auto_now=True, null=True)

    def __str__(self):
        return f'{self.documento} {self.nome}'
    
    def clean(self):
        self.nome = self.nome.upper()
        self.endereco = self.endereco.upper()
        self.bairro = self.bairro.upper()
        self.cidade = self.cidade.upper()
    
    
