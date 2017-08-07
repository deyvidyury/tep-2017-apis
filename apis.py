import requests;
import json;

# SWAPI - Star Wars API
# All the Star Wars data:
# Planets, Spaceships, Vehicles, People, Films and Species
# From all SEVEN Star Wars films
# 
# Only get requests
# endpoint: https://swapo.co/api
#
# Site: http://swapi.co/

# Retorna informacoes sobre todos os resources disponiveis
def getRoot():
	url = 'http https://swapi.co/api/'
	r = requests.get(url, verify = False)
	print(r.text)

# Retorna informacoes sobre algum personagem dos filmes
def getPeople(inputString):
	url = ('http https://swapi.co/api/people/%s' %(inputString))
	r = requests.get(url, verify = False)
	print(r.text)


# =========================

# API que implementei para uma aplicacao em AngularJS 2
# A aplicacao gerencia os alunos de uma turma.
# A API possibilita fazer CRUD dos estudantes.
#
# END-POINTS
# Todos os estundantes: GET https://fierce-island-41854.herokuapp.com/api/estudantes
# Estudante por id: GET https://fierce-island-41854.herokuapp.com/api/estudante/:id
# Adicionar estudante: POST https://fierce-island-41854.herokuapp.com/api/estudante, {name:string}
# Deletar estudante: DELETE https://fierce-island-41854.herokuapp.com/api/estudante/:id
# Atualizar estudante: PUT https://fierce-island-41854.herokuapp.com/api/estudante/:id, {newName:string}

def getEstudantes():
	url = 'https://fierce-island-41854.herokuapp.com/api/estudantes'
	r = requests.get(url, verify = False)
	print(r.text)

def getEstudante(id):
	url = ('https://fierce-island-41854.herokuapp.com/api/estudante/%s' %(id))
	r = requests(url, verify = False)
	print(r.text)

def addEstdante(name):
	url = 'https://fierce-island-41854.herokuapp.com/api/estudante'
	r = requests.post(url, data = {'name': 'Mariana'})
	print(r.text)

def deleteEstudate(id):
	url = 'https://fierce-island-41854.herokuapp.com/api/estudante'
	r = requests.delete(url, data = {'_id': id})
	print(r.text)

def updateEstudante(id,newName):
	url = 'https://fierce-island-41854.herokuapp.com/api/estudante'
	r = requests.post(url, data = { '_id': id,'name': newName})
	print(r.text)

#+++++++++++++++++++++++++++++

# API OpenWeatherMap
# Previsoes do tempo para uma determinada cidade, ou varias também.
# Site: https://openweathermap.org/
# É necessario usar uma chave para utilizar os servicos (tambem chamada de appid pelo site). 
# Tem plano gratuito.

# Retorna informacoes sobre o tempo no momento para uma cidade
def getWeatherByCityName(city):
	appid = 'b1b15e88fa797225412429c1c50c122a1'
	url = ('https://api.openweathermap.org/data/2.5/weather?q=%s' %(city))
	r = requests(url, verify = False)
	print(r.text)

# Previsao do tempo para os proximos cinco dias para cada 3 horas.
def getWeatherFiveDays(city):
	appid = 'b1b15e88fa797225412429c1c50c122a1'
	url = ('https://api.openweathermap.org/data/2.5/forecast?q=%s' %(city))
	r = requests(url, verify = False)
	print(r.text)