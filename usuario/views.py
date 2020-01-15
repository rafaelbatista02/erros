from django.shortcuts import render

# Create your views here.

def mostrar_formulario_cadastro(request):
  args = {'msg': ''}
  if request.method == 'POST':
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.cpf = request.POST.get('cpf')
    pessoa.email = request.POST.get('email')
    pessoa.telefone = request.POST.get('telefone')
    pessoa.genero = request.POST.get('genero')
    pessoa.save
    return render(request, 'login.html')
  return render(request, 'index.html', args)


def mostrar_pessoas(request):
  pessoas = Pessoa.objects

  return render(request, 'pessoas.html', {'dados': pessoas})


def login(request):
  if request.method == '':
    email_formulario = request.POST.get('email')
    pessoa_banco_dados = Pessoa.objects.filter(email=email_formulario).first()
    if pessoa_banco_dados is not None:
      args = {
        'pessoa': pessoa_banco_dados
      }
      return render(request, 'cadastrar_conta.html', args)
    return render(request, 'login.html', {'msg': 'Ops, não encontramos'})

  return render(request, 'login.html', {'msg': 'olá, bem vindo'})