from django.shortcuts import render, redirect
from django.db.models import Q

from app_aula.models import Pessoas
dados = []
# ORM
# O = Object
# R = Relational
# M = Model

def home(request):
    total_cadastrados = Pessoas.objects.all()   
    ponteiro = 0
    dados = []
    for index in total_cadastrados:
         ponteiro += 1         
         if ponteiro > len(total_cadastrados) - 10:
            dados.insert(0, index)
    return render(request, 'app_aula/global/home.html', context={"dados":dados})

def criar(request):
    nome = ""
    email = ""
    nascimento = 0
    pais = ""
    mensagem = ""

    if request.POST:
        nome = request.POST.get("nome")
        email = request.POST.get("email")
        nascimento = request.POST.get("nascimento", 0)
        pais = request.POST.get("pais")
        if nome != '' and email != '' and nascimento != '' and pais != '':
            mensagem = [
                    {"texto": "Usuário " + nome + " cadastrado com sucesso!", 
                     "severidade": "success"}
                ]
            Pessoas.objects.create(nome=nome, email=email, nascimento=nascimento, pais=pais)
            nome = ''
            return render(request, 'app_aula/global/criar.html', context={"nome":nome, "mensagem":mensagem})
        else:
            if nome == '':
                mensagem = [
                    {"texto": "Opa, você esqueceu de preencher o campo 'Nome' !", 
                     "severidade": "warning"}
                ]
            elif nascimento == '':
               mensagem = [
                    {"texto": "Opa, você esqueceu de preencher o campo 'Nascimento' !", 
                     "severidade": "warning"}
                ]
            elif email == '':
                 mensagem = [
                    {"texto": "Opa, você esqueceu de preencher o campo 'Email' !", 
                     "severidade": "warning"}
                ]
            elif pais == '':
               mensagem = [
                    {"texto": "Opa, você esqueceu de preencher o campo 'País' !", 
                     "severidade": "warning"}
                ]
            
    return render(request, 'app_aula/global/criar.html', context={"nome":nome, "mensagem":mensagem, "email":email, "nascimento":nascimento, "pais":pais})


def deletar(request, id=0):
    pessoa = {}
    filtro = Q()
    if id:
        pessoa = Pessoas.objects.get(id=id)
        pessoa.delete()
        return redirect(deletar)
    nome_filter = request.POST.get("nome")
    email_filter = request.POST.get("email")
    nascimento_filter = request.POST.get("nascimento")
    pais_filter = request.POST.get("pais")
    if nome_filter:
        filtro &= Q(nome__icontains=nome_filter)
    if email_filter:
        filtro &= Q(email__icontains=email_filter)
    if nascimento_filter:
        filtro &= Q(nascimento=nascimento_filter)
    if pais_filter:
        filtro &= Q(pais__icontains=pais_filter)
    print(filtro)
    if filtro:
        pessoa["pessoas"] = Pessoas.objects.filter(filtro)
    else:
        pessoa["pessoas"] = Pessoas.objects.all()
    return render(request, 'app_aula/global/deletar.html', context=pessoa)

def atualizar(request, id=0):
    pessoa = {}
    mensagem = ""
    if id:
        if request.POST:
            pessoa = Pessoas.objects.get(id=id)
            pessoa.nome = request.POST.get("nome", pessoa.nome)
            pessoa.email = request.POST.get("email", pessoa.email)
            pessoa.nascimento = request.POST.get("nascimento", pessoa.nascimento)
            pessoa.pais = request.POST.get("pais", pessoa.pais)
            if pessoa.nome != '' and pessoa.email != '' and pessoa.nascimento != '' and pessoa.pais != '':
                pessoa.save()
                return redirect(atualizar)
            
            else:
                if pessoa.nome == '':
                    mensagem = [
                        {"texto": "Opa, você esqueceu de preencher o campo 'Nome' !", 
                        "severidade": "warning"}
                    ]
                elif pessoa.nascimento == '':
                    mensagem = [
                        {"texto": "Opa, você esqueceu de preencher o campo 'Nascimento' !", 
                        "severidade": "warning"}
                    ]
                elif pessoa.email == '':
                    mensagem = [
                        {"texto": "Opa, você esqueceu de preencher o campo 'Email' !", 
                        "severidade": "warning"}
                    ]
                elif pessoa.pais == '':
                    mensagem = [
                        {"texto": "Opa, você esqueceu de preencher o campo 'País' !", 
                        "severidade": "warning"}
                    ]
                pessoa = {}
            
            
            
        pessoa["pessoas"] = Pessoas.objects.get(id=id)
        return render(request, 'app_aula/global/update.html', context={"pessoas":pessoa["pessoas"], "mensagem":mensagem})
    filtro = Q()
    nome_filter = request.POST.get("nome")
    email_filter = request.POST.get("email")
    nascimento_filter = request.POST.get("nascimento")
    pais_filter = request.POST.get("pais")
    if nome_filter:
        filtro &= Q(nome__icontains=nome_filter)
    if email_filter:
        filtro &= Q(email__icontains=email_filter)
    if nascimento_filter:
        filtro &= Q(nascimento=nascimento_filter)
    if pais_filter:
        filtro &= Q(pais__icontains=pais_filter)
    if filtro:
        pessoa["pessoas"] = Pessoas.objects.filter(filtro)
    else:
        pessoa["pessoas"] = Pessoas.objects.all()
        
    return render(request, 'app_aula/global/atualizar.html', context=pessoa)
    
def pesquisar(request):
    pessoa = {}
    filtro = Q()
    nome_filter = request.POST.get("nome")
    email_filter = request.POST.get("email")
    nascimento_filter = request.POST.get("nascimento")
    pais_filter = request.POST.get("pais")
    if nome_filter:
        filtro &= Q(nome__icontains=nome_filter)
    if email_filter:
        filtro &= Q(email__icontains=email_filter)
    if nascimento_filter:
        filtro &= Q(nascimento=nascimento_filter)
    if pais_filter:
        filtro &= Q(pais__icontains=pais_filter)
    if filtro:
        pessoa["pessoas"] = Pessoas.objects.filter(filtro)
    else:
        pessoa["pessoas"] = Pessoas.objects.all()
        
    return render(request, 'app_aula/global/pesquisar.html', context=pessoa)