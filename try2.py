import random

class Player:
    def __init__(self, username, score=0):
        self.username = username
        self.score = score
        self.scores = []

    def __str__(self):
        resutl_str = self.username+' Score: '+str(self.score)
        return resutl_str

class Node:
    def __init__(self, left=None, right=None):
        self.players = []
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        result = 'Player: '+ self.players[0].username + ' Score: ' + str(self.players[0].score)
        return result



def getHeight(node):
    if not node:
        return 0
    return node.height

# Exercice 4
def isAVL(root):
    return abs(getBalance(root)) <= 1

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def getMinValueNode(root):
    if root is None or root.left is None:
        return root
    return getMinValueNode(root.left)

def getMaxValueNode(root):
    if root is None or root.right is None:
        return root
    return getMaxValueNode(root.right)

def rightRotate(z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    return y

def leftRotate(z):
    y = z.right
    try:
        T2 = y.left
    except:
        print(z)
        print(z.left)
        print(z.left.left)
        print(y)
    y.left = z
    z.right = T2
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    return y

def reverseInOrder(root, player_list):
    if root:
        reverseInOrder(root.right, player_list)
        for i in root.players:
            player_list.append(i)
        reverseInOrder(root.left, player_list)
    return player_list

# Exercice 5
def insertAVL(root, key):
    if not root:
        node = Node()
        node.players.append(key)
        return node
    elif key.score == root.players[0].score:
        root.players.append(key)
        return root
    elif key.score < root.players[0].score:
        root.left = insertAVL(root.left, key)
    else:
        root.right = insertAVL(root.right, key)
    #root.height = 1 + max(getHeight(root.left), getHeight(root.right))
    setHeight(root)
    balance = getBalance(root)
    if balance > 1 and key.score < root.left.players[0].score:
        return rightRotate(root)
    if balance > 1 and key.score > root.left.players[0].score:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and key.score > root.right.players[0].score:
        return leftRotate(root)
    if balance < -1 and key.score < root.right.players[0].score:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def height(node):
    if node is None:
        return 0
    return node.height
def deleteAVL(root, key):
    if not root:
        return root
    if key.score < root.players[0].score:
        root.left = deleteAVL(root.left, key)
    elif key.score > root.players[0].score:
        root.right = deleteAVL(root.right, key)
    else:
        if len(root.players)>1:
            playerToReturn = root.players[len(root.players)-1]
            root.players = root.players[:(len(root.players)-1)]
            return root
        if root.left == None or root.right == None:
            if root.left is None:
                temp = root.right
            else:
                temp = root.left
            if temp is None:
                root = None
            else:
                root = temp
        else:
            temp = getMinValueNode(root.right)
            root.players = temp.players
            root.right = deleteAVL(root.right, temp.players[0])
    if root is None:
        return root
    root.height = max(height(root.left), height(root.right)) + 1

    balance =getBalance(root)
    if balance > 1 and getBalance(root.left)>=0:
        return rightRotate(root)

    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)
    if balance< -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)
    return root

def checkHeight(root, h=-1):
    if root is None:
        return 0
    if height(root) != 1 + max(height(root.left), height(root.right)):
        return -1
    return 1

def setHeight(root):
    if root is None:
        return 0
    else:
        root.height = 1+max(setHeight(root.left), setHeight(root.right))
        return root.height
def meanScore(player):
    sum = 0
    for i in player.scores:
        sum+=i
    return sum/len(player.scores)

class Game:
    def __init__(self, database=None):
        self.database = database
        self.rounds = 0

    def ranking(self):
        '''
        This function eliminate the last 10 players in the database, by searching the one with the lowest value
        and deleting it, and it does that 10 times
        Input: -
        Output: -
        '''
        index = 0
        while index < 10:
            min_score_node = getMinValueNode(self.database)
            player_to_exclude = min_score_node.players[0]
            print()
            root = deleteAVL(self.database, player_to_exclude)
            self.database = root
            index += 1
    def round(self):
        '''
        Here we simulate a game, we take which node by deleteind it, put it temporarily in a list, meanwhile we
        give to each player a score and we do the mean of it
        Input: -
        Output: -
        '''
        players_list = [] #there we are going to put the players while we are attribuiting the scores to them
        self.rounds+=1
        players_list = reverseInOrder(self.database, players_list)
        for i in players_list:
            round_score = random.randint(0,12)
            i.scores.append(round_score)
            i.score = meanScore(i)
        # while self.database is not None:
        #     root = deleteAVL(self.database, self.database.players[0])
        #     self.database = root
        self.database = None
        while len(players_list) > 0:
            root = insertAVL(self.database, players_list[0])
            self.database = root
            players_list = players_list[1:]

    def competition(self):
        '''
        After the game is set up, the competition starts by doing rounds of game and after the 3-th game we start
        ranking and excluding the last 10 players in the database
        Input: -
        Output: -
        '''
        for i in range(11):
            self.round()
            if self.rounds>2:
                self.ranking()

    def podium(self):
        '''
        This function is going to display the players that last until the end of the competitions
        '''
        print("Top 10 players are:")
        player = []
        player = reverseInOrder(self.database, player)
        j = 1
        for i in player:
            print('The place ' + str(j) + ' for ' + i.username + ' which has the score ' + str(i.score))
            j+=1
    def start(self):
        '''
        This function is going to start our game by setting up the database with 100 players
        which initailly all of them are going to have score 0
        Input: -
        Output: -
        '''
        for i in range(1,101):
            username = "Player"+str(i)
            player = Player(username)
            root = insertAVL(self.database, player)
            self.database = root
        #after seting the database with player we can start the competition
        self.competition()
        self.podium()



tree = None
game = Game(tree)
game.start()

def test_delete_insert():
    root = Node()
    player = Player('name1', 4)
    root.players.append(player)
    player2 = Player('name2', 5)
    player3 = Player('name3', 6)
    node2 = Node()
    node2.players.append(player2)
    root = insertAVL(root, player2)
    print(root.players[0])
    root = insertAVL(root, player3)
    print(root.players[0])
    root = deleteAVL(root, player2)
    print(root.players[0])
    root = deleteAVL(root, player)
    print(root.players[0])
    root = deleteAVL(root, player3)
    print(root.players[0])

def test_revInOrder():
    root = Node()
    player = Player('name1', 4)
    root.players.append(player)
    player2 = Player('name2', 5)
    player3 = Player('name3', 6)
    node2 = Node()
    node2.players.append(player2)
    root = insertAVL(root, player2)

    root = insertAVL(root, player3)
    players_list = []
    players_list = reverseInOrder(root, players_list)
    for i in players_list:
        print(i)

def test_delete():
    root = Node()
    player = Player('name1', 4)
    root.players.append(player)
    player2 = Player('name2', 5)
    player3 = Player('name3', 6)
    player4 = Player('name4', 6)

    root = insertAVL(root, player2)
    root = insertAVL(root, player3)
    root = insertAVL(root, player4)
    print(root)
    ceva = deleteAVL(root, player4)
    print(ceva)

def test_balanced():
    root = None
    player = Player("p1", 7)
    player2 = Player("p2", 8)
    player3 = Player("p3", 8)
    player4 = Player("p4", 8)
    root = insertAVL(root, player)
    root = insertAVL(root, player2)
    root = insertAVL(root, player3)
    root = insertAVL(root, player4)
    print(str(root.height))

#test_balanced()

def test_setHeight():
    root = Node()
    node = Node()
    root.right = node
    node1 = Node()
    root.left = node1
    node2 = Node()
    root.left.left = node2
    print(setHeight(root))
    mama = 1
#test_setHeight()


