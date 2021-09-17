extends KinematicBody2D

class_name Personagem

# Declaração de variáveis
var velocidade = 200
var direcao = Vector2(0,0)

# Chamado quando o script entra em cena pela primeira vez
func _ready():
	pass # Replace with function body.

# Função para ler as ações e processar elas
func getInput():
	var entrada = Vector2(0,0)
	if Input.is_action_pressed("andar_direita"):
		entrada.x = 1
	if Input.is_action_pressed("andar_esquerda"):
		entrada.x -= 1
	direcao = entrada.normalized() * velocidade

# função que atualiza o estado físico do objeto
func _physics_process(delta):
	getInput()
	move_and_slide(direcao)

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
