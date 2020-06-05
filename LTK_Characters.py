import LTK_player

class blank(player):
	def __init__(self, name, role):
		pass
	def draw(self, n, deck):
		pass
	def judgementdraw(self, deck):
		pass
	def discard(self, card = None, count = 1):
		pass
	def damaged(self, n):
		pass
	def heal(self, n):
		pass
	def death(self, deck):
		pass
	def beforeplayphase(self, deck):
		pass
	def drawphase(self, deck):
		pass
	def actionphase(self, deck): 
		pass
	def discardphase(self, deck):
		pass
	def afterplayphase(self, deck):
		pass
	def 

class XuChu(player):

	def __init__(self, name, role):
		super().__init__(name,role)
		abilityused = 0

	def drawphase(self,deck):
		num = input("Enter 2 to draw normally, 1 to activate ability.")
		while(True)
			try:
				if(num == 1)
					abilityused = 1
					break
				else if(num == 2)
					break
				except InvalidInput
					num = input("Must enter 1 or 2.")
		draw(num,deck)
	
