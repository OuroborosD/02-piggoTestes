from django.core.checks.messages import Error
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.models import UserManager, User

from django.contrib import auth # para login de usuario. verifica se o email e senha são de algum usuario.
# Create your views here.

from django.contrib.auth.decorators import login_required


def cadastrar(request):
    
    if request.method == 'POST':
        print(request.POST)
        dados = request.POST
        dados_listak = list(dados.keys())
       
        for i in dados_listak:
       
            if dados[i] == '' or dados[i] == None:
                print('é vazio o :',i)
                return HttpResponseRedirect(request,'user/cadastro.html')
       
       # FORMA com try e exept      
       #
       #try:#tenta pegar o objeto com o username no banco de dados, se tiver aparece nome já existe
       #     User.objects.get(username=dados['nome'])
       #     print('usuario já existe,') 
       # except:# se não tiver da um erro, e entre nessa parte e salva o usuario e senha no banco
       #     User.objects.create(username=dados['nome'], password=dados['senha'])

        
       #forma com o .exists() 
        
        if  User.objects.filter(username=dados['nome']).exists():#verifica se o usario existe
            print('usuario já existe,') 
        else:
            User.objects.create_user(username=dados['nome'], password=dados['senha'])
            return redirect('user_login')

        
    
    return render(request,'user/cadastro.html')

def login(request):

    if request.method == 'POST':#verificar se os dados são post.
        usuario = request.POST.get('nome')# pega o valor do input com name='nome'
        senha = request.POST.get('senha')        

        print(usuario,senha)

        user = auth.authenticate(request, username=usuario,password=senha)#se o id e senha estverem lá, o user receberar um TRUE

        if user:
            print('usuario encontrado')
            auth.login(request,user)
            return redirect('user_dashboard')
        else:
            print('não existe usuario')
            return render(request,'user/login.html')            

    else:
        pass
    return render(request,'user/login.html')

@login_required(redirect_field_name='user_login')
def dashboard(request):
        return render(request,'user/dashboard.html')