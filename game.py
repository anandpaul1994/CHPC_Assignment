from random import randint

class attributes(object):
	"""Attributes of player"""
	def __init__(self,power,life,group,position):
		self.power = power
		self.life = life
		self.group = group
		self.position = position
	def print_pos(self):
		print self.position
	def change_pos_player(self,i,n,size):
		if((self.position[i]==0 and n<0) or (self.position[i]==size and n>0)):
			print 'Operation is out of the matrix'
		else:
			self.position[i]=self.position[i]+n
	def change_pos_enemy(self,i,n,size):
		if((self.position[i]==0 and n<0) or (self.position[i]==size and n>0)):
			self.position[i]=self.position[i]-n
		else:
			self.position[i]=self.position[i]+n
	def power_ret(self):
		return self.power


class players(attributes):
	"""docstring for players"""
	def __init__(self, p_id,name,power,life,group,position):
		self.p_id = p_id
		self.name = name
		super(players, self).__init__(power, life, group, position)
	def fight(self,env,enemy):
		for t in range(24):
			for x in range(2):
				if player[x].position==enemy[t].position:
					if (enemy[t].power_ret() >self.power_ret()):
						self.life=self.life-1
						if(self.life==0):
							print self.name +' died'
							exit()
						else:
							print self.name +' encountered an enemy, Life Remaining: '+ str(self.life)
							print ' killed Titan'+ enemy[t].e_id

class enimies(attributes):
	"""docstring for players"""
	def __init__(self, e_id,power,life,group,position,env):
		self.e_id = e_id
		super(enimies, self).__init__(power, life, group, position)

class Environment():
	enemy_pos={}
	"""docstring for Environment"""
	def __init__(self, matrix_size):
		self.matrix_size = matrix_size
		

def title_display():
	k=raw_input('')
	return k

def list_player():
	print '0.Zeus, Power:200, Type:God'
	print '1.Presaiden, Power:200, Type:God'
	k=input('Enter the player no to Choose :')
	return k

size=32
env = Environment(size)
player_no = list_player()
player = []
player.append(players(1,'Zeus',200,3,'God',[0,0]))
player.append(players(2,'Presaiden',200,3,'God',[0,0]))
enemy = []
enemy.append(enimies(1,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(2,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(3,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(4,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(5,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(6,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(7,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(8,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(9,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(10,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(11,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(12,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(13,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(14,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(15,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(16,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(17,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(18,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(19,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(20,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(21,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(22,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(23,100,1,'Titans',[randint(1,31),randint(1,31)],env))
enemy.append(enimies(24,100,1,'Titans',[randint(1,31),randint(1,31)],env))
print "Welcome to Python Game, Use 'w' 'a' 's' 'd' for controls and 'q' to quit"
k=''
print 'Current Position = ',player[player_no].print_pos() 
while (k!='q'):
	for t in range(24):
		p=randint(0,1)
		q=randint(-1,1)
		enemy[t].change_pos_enemy(p,q,size)
	k=title_display()
	print player[player_no].name +" Position:"
	if k=='w':
		player[player_no].change_pos_player(1,-1,size)
		player[player_no].print_pos()
		player[player_no].fight(env,enemy)

	elif k=='a':
		player[player_no].change_pos_player(0,-1,size)
		player[player_no].print_pos()
		player[player_no].fight(env,enemy)

	elif k=='s':
		player[player_no].change_pos_player(1,1,size)
		player[player_no].print_pos()
		player[player_no].fight(env,enemy)

	elif k=='d':
		player[player_no].change_pos_player(0,1,size)
		player[player_no].print_pos()
		player[player_no].fight(env,enemy)
	for t in range(24):
		print "Titan "+str(t+1)+":"+str(enemy[t].position)
	player_no = input('Enter the player no to Choose :')
