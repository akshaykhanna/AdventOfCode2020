print('day3')


def find(a: []):
    lr = len(a);
    lc = len(a[0]);

    def getCount(right, down):
        r = 0;
        c = 0;
        count = 0;
        while r < lr - down:
            c += right;
            if c >= lc:
                c = c - lc;
            r += down;
            if a[r][c] == '#':
                count += 1;
        return count

    print('1,1:', getCount(1, 1));
    print('3,1:', getCount(3, 1));
    print('5,1', getCount(5, 1));
    print('7,1', getCount(7, 1));
    print('1,2', getCount(1, 2));
    return getCount(1, 1) * getCount(3, 1) * getCount(5, 1) * getCount(7, 1) * getCount(1, 2);


b = [
    "..##.........##.........##.........##.........##.........##.......",
    "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
    ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
    "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
    ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
    "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
    ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
    ".#........#.#........#.#........#.#........#.#........#.#........#",
    "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
    "#...##....##...##....##...##....##...##....##...##....##...##....#",
    ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#",
]
a = [
    "..#..#......#..#.......#...#.#.",
    "...##.....##..#..#....#.##.##.#",
    "...#...#.##...##.....#.....#.#.",
    "..#....#.....#...##.##.###.#...",
    ".#.....#......#..#.##.#...###..",
    "#..#..#.#......#...........###.",
    "#......####.#....##........##..",
    ".#.......#.....#......#...#....",
    "...#...#.....#.......##.....##.",
    "#...##.........#.#..##..#..#.##",
    "#.#.##.........#.#..#.#.....###",
    ".##..##...#....##.....#..#.....",
    "........#.......###.#.#.....#.#",
    "...#.#....#.##..#...##..##..#..",
    "......#....#........######.#...",
    ".##...#.#...###......#.#.#..#.#",
    "........#.##...##.#...#..#...##",
    ".#..#.#..##....###..#.#.......#",
    "..#..##..#.#...#.##......#.....",
    "##.....#..##.#.#..#......##...#",
    "......................#..#..#..",
    "..#.##....####.........###.##..",
    "##..###..#...#....#..#.#...#...",
    ".##.#......#..#....#........#..",
    ".#.....#..#..#.#.#....#.....##.",
    "..........#..#....#..##...#..##",
    ".#...#.#....#.##..#.....#....#.",
    "#..............#.#.#..#..#....#",
    "...#.#...............##........",
    "#.#.##...#.##..##.....#........",
    "...#.......###..###..#...#..#..",
    "####..#.#..##.....##.#.#......#",
    ".#.#.......#..##.......#.......",
    "#....#...#.##.#.......#..#.....",
    ".#...##..#..#..##.......##...#.",
    ".#..#......#.........#.........",
    "#.##.#.....#....#..##..#.....#.",
    "#.#....#.#....#...#.#..#....#..",
    "#..#.....#.##..#.....#...##...#",
    "#....#...##.#.........#.#....##",
    ".......##.##......##.......##..",
    "#.....#..#........#........#...",
    "#....#.#..#.#........##.#...#..",
    "#.......#.#.#.#....#.......##.#",
    "...#..###..........#...#.#.###.",
    "....#..#....#...#....##.#.....#",
    ".#..##.....#..#....##..##...#.#",
    "#.........#....#.#..###...##...",
    ".#.#.........#.#.......#.#.#..#",
    "..........#........##..#.......",
    ".....#.......#...#.....#..##.##",
    "...#.........#.............####",
    "##..#...#..#.#......#...#......",
    ".#..###...#.#.#.#...#...#......",
    "....#..##.#....#..#.#..##..##.#",
    "..#.......#......#..#.......#..",
    "....###......#...##...#....#...",
    "..#..#.....#...#..###....#.#..#",
    ".........##..#.##....#..##..#..",
    "##...#...#.#.........##......#.",
    "###..#.#....#......##..##.#...#",
    ".##...##..#.#.#.#......#..#....",
    "###......#..#..#.....#..#....#.",
    ".#.#..##....##........##..#.#..",
    "###...####.#....#.......###....",
    "..#....###..#.#.#..#.......##..",
    ".......#.#...#.....#.#....##.#.",
    "......#......#.#....#..##..###.",
    "....####..........#.....#......",
    ".###.....#...#..#...##.#...###.",
    "...##....##....###....#.#..#.#.",
    "##.#..........##.........#.##..",
    "..#..#.#.###..##..#....##.....#",
    "..#....##.....#...##....###..##",
    "....#.......##..#..#..........#",
    "............#..#.###..#.#......",
    "...........##......#.#.#...#..#",
    "...##.##....#...##.##.....#.#..",
    ".####...#....###...#.....#....#",
    ".##........#..##..#.#.....#....",
    "..................#.....#..##..",
    "..###.....#.##..#..#....##...#.",
    "...#.##.#.####.#.###.#....#..##",
    ".#....##..##......####.#####...",
    "#...#.#....##.........##....#..",
    "..#.##.....##.............#.##.",
    "###.....#.#..#..#......#.##.#..",
    "...#..##.....#...##...#......#.",
    ".##.#...#......##.#..##....#...",
    ".....##.....#......#.#.........",
    "#.....#.....#........##........",
    ".#......##...#..#.#....###.#..#",
    "#.####...#....#.........#..#...",
    "#..##.#.....#.##.##.#....#...#.",
    "#########..#....#..#...#......#",
    "..##..##...###.######...##.##..",
    "##.......#.......#.#....###..#.",
    ".....#...#.######..#.....#.....",
    ".#......#..#.............#.##.#",
    "..###.#.#......##...###........",
    ".......####.#..##....#........#",
    "..#......#.##....##.##....#....",
    "....#......#.#....#..#.#.....##",
    "####.....#....#.#......#.#.#.##",
    "#...##....#.#.##.........#....#",
    "....#..###......#......#...#...",
    ".....##.#..#..#...#..#.#.#.....",
    ".##............#.....#.........",
    "##...#..#.....##.#..#..........",
    "#.....#####.......#..#....#.#..",
    ".........#..#.....###........#.",
    "#....#..#...###........#..#.#..",
    "...##...#..#...#.##..#.........",
    ".........#.#.....#.......#...#.",
    ".#.....#..####....#.##.......##",
    "...............##....##.##..##.",
    "............#....#....#...##.#.",
    "..#...#........#.......#..#....",
    "##....####....#.##...#..##..#.#",
    ".#.#.....#......#.#........#.#.",
    "....#......#.#....##..##.......",
    ".#..#.#..#..##.....#...........",
    "..#........#.##..#......##..#..",
    "...##.#...#...#..#........#....",
    "##..##....#......#...#..#.#.#.#",
    "......#.....#..#..#....#.......",
    ".....##......#..#.#.##...#.....",
    "...#.....#.#..........#..##...#",
    ".####.##....#...........#.....#",
    ".....###..##...#....##..#...#..",
    "..##...#.#...#..........#..#.#.",
    "...#..#..............#.##.#....",
    "##.#....#...#..#....#..........",
    ".##..........#..#........#.....",
    "#...#.#......#...#.....##..#...",
    ".##...#.#.#....###.####..#....#",
    ".#......#.#...#.#....#.#...#...",
    "#....##.###.............#.#....",
    "....#.###..##..##.##...##......",
    "##....#..###.##.##.....#......#",
    "..#..#..#......#..#..#.........",
    "#.##......#.#....#..#..#.......",
    "....#.#...#..###......##.......",
    ".###.......##.......#....###...",
    "..#..#.##..#.#....#..#.#.....#.",
    ".#..##.##..............#....#..",
    "#...#.#...#..#.##..##.#.#......",
    "#...#..#..##..##.###......#....",
    ".#..#.....#...#....#.....#...#.",
    ".....#....#..#.....###...#.####",
    ".#.....#......#...##...#..#....",
    ".#......#............#.#.......",
    "....##....#.#..#..#...#..#.#...",
    "#...#.....###...##...#.##.....#",
    ".......#.....#....#.......#...#",
    "#.......###.......#.#..........",
    "...#.#.###.#........#.###...#..",
    "....#............#....#..#.....",
    "#......#.##.#...##.......#..#.#",
    ".....#....#....#.#.#...###..#..",
    ".....#.#...#...#.#..#....#.#..#",
    ".#.......#.#..#...###.......##.",
    ".......#..#.##.........#.......",
    ".##.#........#.##...##....#....",
    ".#....#..#...#......####...#..#",
    "...#.....#..##.#..#.#....#....#",
    "...##....#........#.#........#.",
    ".....#....##..#.##..........#..",
    "#.....#.#.#......##....##.#..#.",
    ".#.#.##..#.#....##.#....##.....",
    ".....#.....#..#.#....#..#....##",
    "...#........#....#......###.#..",
    ".....##...#.....##.##.#.#.##...",
    "...#.....#####....##.#.#.###.#.",
    ".#..#.#..##...###.........#.#.#",
    "#...#...#.#..#...#...........#.",
    ".##..............#...#..#....#.",
    "....###.........#.#.#....#.....",
    "..#...##.#.#....##.#..#...#..#.",
    "..#.....#.#......#....#......#.",
    ".......##....#.#.##....#...#..#",
    "##.#.#...#..#......#..#..#....#",
    "...#.#......#............###.##",
    "..###..#..##..#...##........#..",
    ".#...#...##...#....#....##.#..#",
    "..##...####....#....#..#....#.#",
    "...#......##....#.........##.#.",
    "##.#.......#..#..#.............",
    "..#.#.#.#......#...#.#..##.....",
    ".#..##.....###...##.#..#......#",
    "##...#..........#.####....##...",
    "#..........#...#..##....#......",
    "....##...#....#..####...#.##.##",
    ".#.######...##...#..##.........",
    "....##.........#.......##.##...",
    ".#.....#.#..........##......#..",
    "...#..#.#.###..#........#.....#",
    "..##..#............##.......#..",
    "......##....##..#.##..#.......#",
    ".......##....#.......#..#...#.#",
    "#.#......#.###.....#.##........",
    ".#..##..........#..#.....#.##..",
    "..#.#...#....#.........#..##..#",
    ".#......#.......#...#..#..###..",
    "......#.##.....#.#......#....#.",
    "....#....#...#.......#...##.##.",
    "#....#...##...#..##........###.",
    "##......#.#..#.......#.......#.",
    "...##.##..#......#.###..#.#.##.",
    ".............#..#.............#",
    "..#.......##..#..#....##...#...",
    "...............##..##........#.",
    "##...#.##.......#....#.......##",
    "....##.##.#.#.....##.....##.##.",
    "#.#......#.......#..#.#..#.....",
    "....##....#.##........##.##.#..",
    "......##....#..##..#..##....##.",
    ".............#.....#.......#...",
    ".......###.......#..........#..",
    "......##.#..#.....#.#...#.#...#",
    ".#...#..#..###.###...#....##...",
    "#......#..#.#...#...#.....#..##",
    ".###.....#..#.#......##..#.##..",
    ".##.#.....#..#.#..#....##......",
    "#......#..............#.....#.#",
    "...#..#....#.....#.....##.#...#",
    "......#..##..##.....#...#......",
    ".....####..#..#.##.......#..#.#",
    "###.#.#........#.......#.....##",
    "..#.#.#.#...#...#........#....#",
    "....##.#.#..#...##.....#......#",
    "#..#.##....#..#.##..####.......",
    "...####.#...#......#......##..#",
    "#....#.#..###......#..#..##..#.",
    "...........#....#...#......#...",
    "......###.#.....#.#....#.#...#.",
    ".......#.##..............#..##.",
    "..##...........#..#.#...#.....#",
    "#..#............##.........#.#.",
    ".......###.#...#.#...#.#.#...#.",
    "..#...##.......#..#......#.#.##",
    "#.#...#.....#...##.#.#.......##",
    ".#.#.##...#..##.#......#.......",
    "#.......#.......#.#....#.....#.",
    ".....#..#..#.......#..#........",
    "##...##...##......#..##.###....",
    "..#...#.###.#.###..#.....###...",
    ".....####.......#.#.....##....#",
    "....#....#.#....#...#..#.#..#..",
    "..##.....#....#.#.#.###...#....",
    "......#.#....#.#..#....#.#..#..",
    "#...#...#....#.......#......#.#",
    "#..#.#......#..#...........#.##",
    "...............#....#.....#...#",
    ".#.#.#...#.##...#.#.#..#....#..",
    "...#.#.####..##.#...##.........",
    "##.........##.##.....##....#...",
    "................#...#.##.#.#..#",
    ".#..#....#...#..#..#..###.#..#.",
    "...#..#.##.#.####..........#..#",
    "........#....##......#..#.#....",
    "........##.........#..#..#..#.#",
    "#......#.#...#...#...##.....#..",
    "#...#.....#..#..##.#...#.#.#...",
    "....#..##...##.....#...#.#.....",
    "..#..##....#....#...#....#.....",
    ".#..#...##.......###...#...#...",
    ".#......#......#..##..#..##....",
    "....##....#..#.#....#.#..##....",
    "###......#...........#.....###.",
    ".....#...#..##.#..#..#.....#..#",
    "#.#....#...........#.##..#..###",
    "#....#...###.#...#..##..#.....#",
    ".#....#......##.#..#....#.#....",
    "....#.#....#..#.#....#..#..#...",
    "..#......#..#.#.#....#.........",
    ".#...#.#.....#........#.#...###",
    "....#..##.......#.###....##....",
    "#.#.......#......#.###........#",
    "#.........#.....####.##..#..#..",
    ".#.#..##...#.#.....##.#.#..#...",
    ".#..#..#..#.##..#...###.#...#..",
    ".....##..##..##..#.#.#.....###.",
    ".#..#...#..#......##.#.........",
    "....#..##....#.##.........#...#",
    "........#...#...###.........##.",
    "#.........#..##....#.#...#.....",
    ".......#.......#..#.......#....",
    "#......##......#.#.##..........",
    ".#..##..####...#.....####.....#",
    "........#.#....#..##..###.#...#",
    ".#...#...#.........###..#...#.#",
    "#.........#....##...#..........",
    ".#.#....#..........#...........",
    ".#.#..........#.##.....#.##....",
    "..#....#...##..###..........##.",
    ".#.#..#.##..#..#.##.##..##.....",
    "........#...#....#...#.#..##...",
    "......#......##..#..#.....#..#.",
    ".##.#....#...#....#...#..##..##",
    "##............#..........###...",
    "....#.......#.#..#.#####.....#.",
    "#......#.....#...#........#....",
    "..##.....###..#.#.#.#....#....#",
    "#...#...#.#..#..#....#..#......",
    "......#....#...#..#....#####...",
    "....#.......##....#....##......",
    ".....##...#.##.#.....##....#...",
    ".#....###.#..##...##.##.......#",
    "....#.#.#.##.............#..##.",
    "...........##......#...#.#.##..",
    "....##......#....#....##..##.#.",
    ".#.#...#.....##.....#.........#",
    "#.#..........#.......#.##...#..",
    "....#.##..#.#....#.....#...#...",
    "##.............##.......#.##.#.",
    "....#...#.....##...#..........#",
    "##..#...#...#.#.##...#.......##",
    "..#........#.....###...##..##.#",
    ".....#...##.#.#.##.....#...#...",
    "####.###...##..##...#..#..#..##",
    "......#..#..#.........#...#.#..",
    "....###.....##.##....#.##.....#",
];
print(find(a));
