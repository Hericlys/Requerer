from django.db import models
from utils.random_generator import random_letters


class Responsavel(models.Model):
    nome_completo = models.CharField(max_length=255)
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome_completo


class Requerente(models.Model):
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    RACA_COR_CHOICES = [
        ('BR', 'Branca'),
        ('PR', 'Preta'),
        ('PA', 'Parda'),
        ('AM', 'Amarela'),
        ('IN', 'Indígena'),
        ('ND', 'Não Declarada'),
    ]

    SANGUE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    UF_CHOICES = [
        ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
        ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
        ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
        ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'),
        ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')
    ]

    CID_CHOICES = [
        ('CID-10', 'CID-10'), ('CID-11', 'CID-11')
    ]

    STATUS_CHOICES = [
        ('Em-analise', 'Em análise'),
        ('Deferido', 'Deferido'),
        ('Indeferido', 'Indeferido'),
        ('Pendente', 'Pendente'),
        ('Agendado', 'Agendado'),
        ('Impresso', 'Impresso'),
    ]

    nome_completo = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    nome_mae = models.CharField(max_length=255)
    nome_pai = models.CharField(max_length=255, blank=True, null=True)
    rg = models.CharField(max_length=20)
    orgao_emissor = models.CharField(max_length=50)
    data_emissao_rg = models.DateField()
    uf_rg = models.CharField(max_length=2, choices=UF_CHOICES)
    local_nascimento = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    raca_cor = models.CharField(max_length=2, choices=RACA_COR_CHOICES)
    tipo_sanguineo = models.CharField(max_length=3, choices=SANGUE_CHOICES)
    
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    
    deficiencia_tipo_cid = models.CharField(max_length=6, choices=CID_CHOICES)
    deficiencia_cid = models.CharField(max_length=10)
    deficiencia_tipo = models.CharField(max_length=50)
    
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=2, choices=UF_CHOICES)

    responsavel = models.ForeignKey(
        Responsavel,
        on_delete=models.SET_NULL, null=True, blank=True
    )

    token = models.CharField(max_length=6, default=random_letters())
    status = models.CharField(max_length=25, choices=STATUS_CHOICES)
    data_solicitacao = models.DateField(auto_now_add=True)
    data_impressao = models.DateTimeField(blank=True, null=True)
    is_printed = models.BooleanField(default=False)


    def __str__(self):
        return self.nome_completo
    

class Documentos(models.Model):
    requerente = models.OneToOneField(Requerente, on_delete=models.CASCADE)
    foto_3x4 = models.ImageField(upload_to='documentos/foto_3x4/%M/')
    rg_frente = models.ImageField(upload_to='documentos/rg_frente/%M/')
    rg_verso = models.ImageField(upload_to='documentos/rg_verso/%M/')
    cpf = models.ImageField(upload_to='documentos/cpf/%M/')
    comprovante_residencia = models.ImageField(upload_to='documentos/comprovante_residencia/%M/')
    comprovante_tipo_sanguineo = models.ImageField(upload_to='documentos/comprovante_tipo_sanguineo/%M/')
    laudo_frente = models.ImageField(upload_to='documentos/laudo_frente/%M/')
    laudo_verso = models.ImageField(upload_to='documentos/laudo_verso/%M/')
    audiometria = models.ImageField(upload_to='documentos/audiometria/%M/', blank=True, null=True)
    boletim_ocorrencia = models.ImageField(upload_to='documentos/boletim_ocorrencia/%M/', blank=True, null=True)

    def __str__(self):
        return f'Documentos de {self.requerente.nome_completo}'
