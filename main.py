import pygame
import random
import copy
from jpres import end, endi

# задаем переменные
kvone = 40
left = 200
up = 100
q = 0
ohv = (left + 30 * kvone, up + 15 * kvone)
xgridl = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К']

pygame.init()

screen = pygame.display.set_mode(ohv)
pygame.display.set_caption("Морской бой")
font = pygame.font.SysFont('comicsans', int(kvone) - 10)
imparea = set()
posaimoves = {(i, j) for i in range(1, 11) for j in range(1, 11)}
babah = set()
alldestroyed = []
notlongago = []
pointers = set()
destrareas = set()
imposglob = set()


class Battleships:
    def __init__(self):
        self.ok = {(i, j) for i in range(1, 11) for j in range(1, 11)}
        self.veh = set()
        self.ships = self.linegr()

    def beginner(self, possib_to_use):
        randxory = random.randint(0, 1)
        rvis = random.choice((-1, 1))
        x, y = random.choice(tuple(possib_to_use))

        return x, y, randxory, rvis

    def create_ship(self, c, v):
        sipxy = []
        x, y, x_or_y, str_rev = self.beginner(v)

        for _ in range(c):
            sipxy.append((x, y))

            if not x_or_y:
                str_rev, x = self.adderr(
                    x, str_rev, x_or_y, sipxy)

            else:
                str_rev, y = self.adderr(
                    y, str_rev, x_or_y, sipxy)
        if self.approved(sipxy):

            return sipxy

        return self.create_ship(c, v)

    def adderr(self, coor, str_rev, x_or_y, spixy):
        if (coor <= 1 and str_rev == -1) or (coor >= 10 and str_rev == 1):
            str_rev *= -1

            return str_rev, spixy[0][x_or_y] + str_rev

        else:

            return str_rev, spixy[-1][x_or_y] + str_rev

    def approved(self, new_ship):
        ship = set(new_ship)

        return ship.issubset(self.ok)

    def addertoslo(self, new_ship):
        for elem in new_ship:

            self.veh.add(elem)

    def newccl(self, new_ship):
        for elem in new_ship:
            for k in range(-1, 2):

                for m in range(-1, 2):

                    if 0 < (elem[0] + k) < 11 and 0 < (elem[1] + m) < 11:
                        self.ok.discard((elem[0] + k, elem[1] + m))

    def linegr(self):
        coordl = []

        for number_of_blocks in range(4, 0, -1):
            for _ in range(5 - number_of_blocks):

                new_ship = self.create_ship(
                    number_of_blocks, self.ok)
                coordl.append(new_ship)
                self.addertoslo(new_ship)
                self.newccl(new_ship)

        return coordl


user = Battleships()
pc = Battleships()

pc_ships = copy.deepcopy(pc.ships)
user_ships = copy.deepcopy(user.ships)


def draw_ships(coor):

    for elem in coor:
        ship = sorted(elem)
        x_start = ship[0][0]
        y_start = ship[0][1]

        if len(ship) > 1 and ship[0][0] == ship[1][0]:
            ship_width = kvone
            ship_height = kvone * len(ship)

        else:
            ship_width = kvone * len(ship)
            ship_height = kvone
        x = kvone * (x_start - 1) + left
        y = kvone * (y_start - 1) + up

        if coor == user.ships:
            x += 15 * kvone
        pygame.draw.rect(
            screen, (0, 0, 0), ((x, y), (ship_width, ship_height)), width=kvone // 10)


class Grid:
    def __init__(self, title, offset):
        self.title = title
        self.offset = offset
        self.grid_painter()
        self.sign_grids()
        self.add_coord()

    def grid_painter(self):
        for i in range(11):
            # отрисовка горизонт. линий
            pygame.draw.line(screen, (0, 0, 0), (left + self.offset, up + i * kvone),
                             (left + 10 * kvone + self.offset, up + i * kvone), 2)
            # отрисовка линий вверх
            pygame.draw.line(screen, (0, 0, 0), (left + i * kvone + self.offset, up),
                             (left + i * kvone + self.offset, up + 10 * kvone), 2)

    def add_coord(self):
        for i in range(10):
            num_ver = font.render(str(i + 1), True, (0, 0, 0))
            letters_hor = font.render(xgridl[i], True, (0, 0, 0))

            vert = num_ver.get_width()
            hei = num_ver.get_height()
            horr = letters_hor.get_width()

            screen.blit(num_ver, (left - (kvone // 2 + vert // 2) + self.offset,
                                  up + i * kvone + (kvone // 2 - hei // 2)))

            screen.blit(letters_hor, (left + i * kvone + (kvone //
                                                          2 - horr // 2) + self.offset,
                                      up + 10 * kvone))

    def sign_grids(self):
        player = font.render(self.title, True, (0, 0, 0))
        sign_width = player.get_width()

        screen.blit(player, (left + 5 * kvone - sign_width //
                             2 + self.offset, up - kvone // 2 - int(kvone)))


def ai_turnss(set_to_shoot_from):
    pygame.time.delay(200)
    destred = random.choice(tuple(set_to_shoot_from))
    posaimoves.discard(destred)
    return check_hit_or_miss(destred, user_ships, True)


def check_hit_or_miss(trdes, aiship, computer_turn, diagonal_only=True):
    for i in aiship:

        if trdes in i:
            ok(
                trdes, computer_turn, diagonal_only=True)
            ind = aiship.index(i)

            if len(i) == 1:
                ok(
                    trdes, computer_turn, diagonal_only=False)

            i.remove(trdes)

            if computer_turn:
                notlongago.append(trdes)
                user.veh.discard(trdes)
                cutr(trdes)
            else:
                pc.veh.discard(trdes)

            if not i:
                ruins(ind, aiship, computer_turn)
                if computer_turn:
                    notlongago.clear()
                    imparea.clear()
                else:
                    alldestroyed.append(pc.ships[ind])

            return True
    pointerre(trdes, computer_turn)
    if computer_turn:
        cutr(trdes, False)

    return False


def pointerre(fired_block, computer_turn=False):
    if not computer_turn:
        pointers.add(fired_block)

    else:
        pointers.add((fired_block[0] + 15, fired_block[1]))
        imposglob.add(fired_block)


def ruins(ind, u, q, diagonal_only=False):
    if u == pc_ships:
        ships_list = pc.ships

    elif u == user_ships:
        ships_list = user.ships
    ship = sorted(ships_list[ind])

    for i in range(-1, 1):
        ok(ship[i], q, diagonal_only)


def cutr(fired_block, computer_hits=True):
    global imparea, posaimoves

    if computer_hits and fired_block in imparea:

        imparea = starv()

    elif computer_hits and fired_block not in imparea:

        executr(fired_block)

    elif not computer_hits:

        imparea.discard(fired_block)

    imparea -= imposglob
    imparea -= destrareas
    posaimoves -= imparea
    posaimoves -= imposglob


def executr(fired_block):
    xhit, yhit = fired_block
    if xhit > 1:
        imparea.add((xhit - 1, yhit))

    if xhit < 10:
        imparea.add((xhit + 1, yhit))

    if yhit > 1:
        imparea.add((xhit, yhit - 1))

    if yhit < 10:
        imparea.add((xhit, yhit + 1))


def starv():
    notlongago.sort()
    new_around_last_hit_set = set()
    for i in range(len(notlongago) - 1):
        x1 = notlongago[i][0]
        x2 = notlongago[i + 1][0]
        y1 = notlongago[i][1]
        y2 = notlongago[i + 1][1]

        if x1 == x2:

            if y1 > 1:
                new_around_last_hit_set.add((x1, y1 - 1))
            if y2 < 10:
                new_around_last_hit_set.add((x1, y2 + 1))

        elif y1 == y2:

            if 1 < x1:
                new_around_last_hit_set.add((x1 - 1, y1))
            if x2 < 10:
                new_around_last_hit_set.add((x2 + 1, y1))

    return new_around_last_hit_set


def ok(fired_block, computer_turn, diagonal_only=True):
    global pointers

    x, y = fired_block
    a, b = 0, 11

    if computer_turn:
        x += 15
        a += 15
        b += 15
        destrareas.add(fired_block)
    babah.add((x, y))

    for i in range(-1, 2):
        for j in range(-1, 2):

            if diagonal_only:
                if i != 0 and j != 0 and a < x + i < b and 0 < y + j < 11:

                    pointers.add((x + i, y + j))
                    if computer_turn:
                        imposglob.add(
                            (fired_block[0] + i, y + j))

            else:
                if a < x + i < b and 0 < y + j < 11:
                    pointers.add((x + i, y + j))
                    if computer_turn:
                        imposglob.add((
                            fired_block[0] + i, y + j))

    pointers -= babah


def wtf(dotted_set):
    for elem in dotted_set:

        pygame.draw.circle(screen, (0, 0, 0), (kvone * (
                elem[0] - 0.5) + left, kvone * (elem[1] - 0.5) + up), kvone // 6)


def hmmmmm(hit_blocks):
    for block in hit_blocks:
        x1 = kvone * (block[0] - 1) + left
        y1 = kvone * (block[1] - 1) + up

        pygame.draw.line(screen, (0, 0, 0), (x1, y1),
                         (x1 + kvone, y1 + kvone), kvone // 6)

        pygame.draw.line(screen, (0, 0, 0), (x1, y1 + kvone),
                         (x1 + kvone, y1), kvone // 6)


def main():
    game_over = False
    computer_turn = False

    screen.fill((255, 255, 255))
    Grid("Компьютер", 0)
    Grid("Игрок", 15 * kvone)
    draw_ships(user.ships)
    pygame.display.update()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if len(alldestroyed) > 9:
                end()
            if len(babah) == 20:
                endi()
            elif not computer_turn and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (left <= x <= left + 10 * kvone) and (
                        up <= y <= up + 10 * kvone):
                    fired_block = ((x - left) // kvone + 1,
                                   (y - up) // kvone + 1)
                computer_turn = not check_hit_or_miss(
                    fired_block, pc_ships, computer_turn)

        if computer_turn:
            if imparea:
                computer_turn = ai_turnss(imparea)
            else:
                computer_turn = ai_turnss(posaimoves)

        wtf(pointers)
        hmmmmm(babah)
        draw_ships(alldestroyed)
        pygame.display.update()


main()
pygame.quit()
