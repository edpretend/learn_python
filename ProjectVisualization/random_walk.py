from random import choice

class RandomWalk():
    """生成随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        #从0开始漫步
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        n_direction = choice([1, -1])
        n_distance = choice([1, 2, 3, 4])
        n_step = int(n_direction*n_distance)
        return n_step

    def fill_walk(self):
        """计算随机漫步的点，添加到value列表中"""
        i = len(self.x_values)
        while True:
            if i < int(self.num_points):
                #x轴的上的随机规则生成的步长
                x_step = self.get_step()
                #y轴的上的随机规则生成的步长
                y_step = self.get_step()
                #拒绝原地踏步
                if x_step == 0 and y_step == 0:
                    continue
                #计算下一个点的坐标
                next_x = self.x_values[-1] + x_step
                next_y = self.y_values[-1] + y_step
                #将最新的坐标添加进列表
                self.x_values.append(next_x)
                self.y_values.append(next_y)
                i += 1
                continue
            break

