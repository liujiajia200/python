class Game(object):

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("游戏帮助信息")

    @classmethod
    def show_top_score(cls):
        print(f"最高分数是{cls.top_score}")

    def start_game(self):
        print("%s开始当前玩家游戏" % self.player_name)


# 1. 查看帮助信息
Game.show_help()

# 2. 查看历史最高分
Game.show_top_score()
# 3. 创建游戏对象， 开始游戏
zhangsan = Game("张三")

zhangsan.start_game()





