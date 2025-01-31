import math
import re

print('day7')


def getBagNameKey(s):
    w = s.strip().split(' ');
    return w[0] + '-' + w[1]


def getNameCount(sae):
    bd = sae.strip().split(' ');
    return bd[1] + '-' + bd[2], int(bd[0])


def getBagNameValue(ss):
    ss = ss.strip()
    if ss.startswith("no other bags."):
        return None
    sa = ss.split(',')
    values = []
    for sae in sa:
        k, v = getNameCount(sae)
        values.append({'k': k, 'v': v});
    print('values', values)
    return values


def find(s):
    l = s.split("\n")
    print('len(l): ', len(l))
    d = {}

    def creatBagDicElement(egs):
        temp = egs.split('contain');
        # print('lG:', temp)
        key = getBagNameKey(temp[0])
        values = getBagNameValue(temp[1])
        # d.append({key: values})
        d[key] = values;

    tc = 0;
    for el in l:
        creatBagDicElement(el)
    print('d: ', d)

    def getKeyValue(obj):
        q, w = b.items()[0]
        return obj['key'], obj['value']

    def presentInList(bagKey, bags):
        if bagKey in bags:
            return True
        return False

    def getCount(searchBag, dd, c=0):
        hv = {}
        nh = {}
        c = 0
        # direct
        for bagKey in dd:
            if dd[bagKey] is None:
                nh[bagKey] = 1;
                continue;
            if searchBag in dd[bagKey]:
                c += 1;
                hv[bagKey] = 1;
        # indirect
        for bagKey in dd:
            if presentInList(bagKey, {**nh, **hv}):
                continue;
            stack = [bagKey]
            isPresent = False
            while len(stack) > 0:
                searchKey = stack.pop()
                if searchKey in hv or searchBag in dd[searchKey]:
                    c += 1
                    # hv[bagKey] = 1;
                    isPresent = True;
                    break;
                else:
                    for newSearchKey in dd[searchKey]:
                        if not presentInList(newSearchKey, nh):
                            stack.append(newSearchKey);
            if isPresent:
                hv[bagKey] = 1
            else:
                nh[bagKey] = 1

        # q = [bbs];
        # while len(q) > 0:
        #     bs = q.pop(0)
        #     for k in dd:
        #         flag = False;
        #         if dd[k] is None:
        #             nh[k] = 1;
        #             continue;
        #         if k in nh:
        #             continue;
        #         if bs in dd[k]:
        #             c += 1
        #             hv[k] = 1;
        #         else:
        #             for kk in dd[k]:
        #                 # ddd = dd[kk]
        #                 if kk in hv:
        #                     c += 1
        #                     hv[k] = 1;
        #                     flag = True
        #                     break;
        #                 elif kk in nh:
        #                     continue;
        #                 elif kk not in q:
        #                     q.append(kk);
        #             if flag:
        #                 break;

        print('dewbs :', hv)
        print('len(dewbs) :', len(hv))
        return c;

    def createObj(sb, t):
        # q, w = sb['k']
        return {'k': sb['k'], 'v': sb['v'], 't': t}

    def totalBag(sb, dd):
        stack = [createObj({'k': sb, 'v': 1}, 1)]
        tc = 0
        while len(stack) > 0:
            bagObj = stack.pop()
            tc += bagObj['v'] * bagObj['t']
            ddd = dd[bagObj['k']]
            if ddd is None:
                continue
            for elBag in ddd:
                stack.append(createObj(elBag, bagObj['v']* bagObj['t']));
        return tc

    return totalBag("shiny-gold", d) - 1;


a = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""
b = """light beige bags contain 5 dark green bags, 5 light gray bags, 3 faded indigo bags, 2 vibrant aqua bags.
faded purple bags contain 4 shiny green bags, 2 mirrored olive bags.
drab tomato bags contain 4 shiny coral bags.
mirrored crimson bags contain 4 bright maroon bags.
faded magenta bags contain 2 clear bronze bags, 5 dim brown bags, 3 striped cyan bags.
vibrant beige bags contain 1 pale silver bag.
plaid lavender bags contain 5 striped teal bags, 2 vibrant tan bags, 3 clear bronze bags, 3 light black bags.
posh maroon bags contain no other bags.
dotted yellow bags contain 4 plaid turquoise bags, 2 plaid lavender bags, 1 dotted violet bag.
posh fuchsia bags contain 5 mirrored gold bags, 2 faded bronze bags, 2 faded coral bags, 1 vibrant maroon bag.
dotted chartreuse bags contain 1 pale magenta bag.
muted beige bags contain 2 drab cyan bags.
dark olive bags contain 4 dull gold bags.
posh yellow bags contain no other bags.
dotted turquoise bags contain 5 striped indigo bags, 2 pale cyan bags, 5 light violet bags, 2 plaid silver bags.
wavy black bags contain 1 light cyan bag, 3 pale tomato bags.
striped plum bags contain 5 wavy maroon bags, 2 dim violet bags, 5 shiny tan bags.
shiny olive bags contain 5 vibrant aqua bags.
dim indigo bags contain 3 dull indigo bags, 2 light crimson bags, 2 dark magenta bags, 2 vibrant tomato bags.
drab tan bags contain 4 vibrant lime bags, 1 faded turquoise bag.
muted black bags contain 4 dull crimson bags, 2 posh tan bags, 4 shiny blue bags.
plaid red bags contain 5 clear blue bags, 3 plaid white bags, 4 dark magenta bags, 1 dark purple bag.
pale black bags contain 2 faded beige bags, 1 striped black bag.
striped red bags contain 3 vibrant green bags, 4 plaid blue bags, 2 drab brown bags.
dotted fuchsia bags contain 1 striped orange bag, 5 dotted maroon bags, 4 posh turquoise bags, 2 drab white bags.
plaid green bags contain 3 posh magenta bags, 4 dark black bags, 3 clear chartreuse bags.
dark violet bags contain 2 clear teal bags, 5 muted cyan bags, 2 shiny coral bags, 5 faded teal bags.
striped gray bags contain 3 bright salmon bags, 5 mirrored brown bags.
dull aqua bags contain 5 mirrored cyan bags, 1 mirrored olive bag.
light indigo bags contain 4 dotted salmon bags, 5 faded lavender bags, 1 dark teal bag, 2 dull purple bags.
dark aqua bags contain 1 clear tan bag, 5 muted turquoise bags, 3 drab orange bags.
drab orange bags contain 5 mirrored gray bags, 5 muted red bags, 3 muted gray bags.
wavy beige bags contain 1 light beige bag, 5 wavy coral bags.
dark gray bags contain 4 shiny violet bags, 3 dull tomato bags.
dull indigo bags contain 4 wavy coral bags, 3 dim plum bags, 2 shiny cyan bags, 2 vibrant bronze bags.
drab gray bags contain 4 drab silver bags, 1 vibrant bronze bag, 3 faded red bags.
dotted gold bags contain 2 faded silver bags.
muted chartreuse bags contain 3 clear turquoise bags, 5 muted turquoise bags, 4 dark crimson bags.
dark orange bags contain 4 shiny coral bags, 5 mirrored fuchsia bags, 5 mirrored teal bags.
light olive bags contain 4 shiny coral bags, 1 pale purple bag, 2 posh yellow bags, 5 shiny gray bags.
dotted silver bags contain 3 dotted purple bags.
muted bronze bags contain 4 striped silver bags, 1 posh plum bag, 1 muted blue bag, 5 shiny violet bags.
striped magenta bags contain 4 dark purple bags, 2 dull tomato bags, 4 mirrored lavender bags.
vibrant violet bags contain 1 plaid purple bag, 2 mirrored olive bags, 3 dotted bronze bags, 2 posh turquoise bags.
muted cyan bags contain 2 dotted crimson bags, 1 muted red bag, 1 plaid lavender bag.
striped black bags contain 1 plaid white bag, 5 pale cyan bags, 4 posh plum bags.
wavy blue bags contain 3 plaid plum bags, 1 shiny bronze bag, 1 shiny magenta bag, 2 vibrant cyan bags.
bright gold bags contain 2 mirrored indigo bags, 3 faded cyan bags, 3 posh beige bags, 1 faded indigo bag.
dim magenta bags contain 1 dark black bag.
dotted magenta bags contain 1 posh tomato bag, 4 striped white bags, 2 posh fuchsia bags, 1 mirrored tan bag.
light lime bags contain 1 mirrored fuchsia bag, 1 dull cyan bag, 1 mirrored chartreuse bag, 2 dotted beige bags.
faded crimson bags contain 1 muted blue bag.
dim tomato bags contain 2 plaid black bags, 3 striped black bags.
wavy tan bags contain 3 wavy gray bags, 2 striped indigo bags.
plaid beige bags contain 2 bright yellow bags, 1 dark gray bag, 5 dotted gray bags.
bright coral bags contain 2 drab white bags, 3 bright maroon bags, 2 dotted tan bags, 4 shiny salmon bags.
plaid tomato bags contain 3 clear white bags, 2 clear coral bags, 1 mirrored blue bag.
striped chartreuse bags contain 4 pale green bags, 2 muted crimson bags.
dim salmon bags contain 5 posh magenta bags, 5 dark red bags, 4 dull teal bags, 4 plaid gray bags.
plaid aqua bags contain 5 dark black bags, 1 light chartreuse bag, 1 dotted maroon bag.
faded silver bags contain 2 plaid silver bags, 1 shiny teal bag, 3 clear purple bags.
drab red bags contain 2 mirrored brown bags.
faded brown bags contain 5 shiny plum bags.
vibrant indigo bags contain 2 vibrant bronze bags, 2 wavy orange bags.
pale salmon bags contain 5 dull cyan bags, 2 wavy orange bags.
drab olive bags contain 1 striped beige bag.
vibrant white bags contain 4 shiny gold bags.
striped teal bags contain 4 faded green bags, 3 mirrored brown bags.
posh beige bags contain 3 posh yellow bags, 1 dull yellow bag, 2 posh maroon bags.
pale violet bags contain 3 shiny teal bags, 5 drab purple bags, 5 light turquoise bags, 4 pale tan bags.
light turquoise bags contain 4 dim lavender bags.
muted yellow bags contain 4 dim crimson bags, 2 wavy gray bags.
mirrored maroon bags contain 5 wavy silver bags, 5 dull aqua bags, 1 faded black bag, 1 faded cyan bag.
drab lavender bags contain 4 drab tan bags, 4 pale violet bags, 2 wavy indigo bags.
light salmon bags contain 2 dim magenta bags, 5 dull orange bags.
drab turquoise bags contain 5 shiny gold bags.
vibrant magenta bags contain 5 wavy maroon bags, 4 dotted gray bags.
clear violet bags contain 1 bright red bag, 2 faded plum bags.
clear beige bags contain 5 faded purple bags.
light silver bags contain 4 vibrant gray bags, 2 wavy gray bags, 4 drab salmon bags.
dark coral bags contain 5 bright plum bags.
pale white bags contain 3 posh tomato bags, 1 clear purple bag, 2 posh crimson bags.
vibrant yellow bags contain 5 posh gold bags, 2 plaid turquoise bags, 5 muted blue bags.
drab yellow bags contain 3 bright salmon bags, 3 clear blue bags, 1 faded indigo bag.
pale red bags contain 5 drab olive bags.
muted lime bags contain 1 vibrant fuchsia bag, 1 shiny coral bag, 2 mirrored violet bags, 5 wavy gray bags.
faded chartreuse bags contain 2 muted tomato bags, 5 dotted gray bags, 1 faded cyan bag, 1 dotted plum bag.
dark beige bags contain 3 dotted violet bags, 5 bright silver bags, 4 posh magenta bags, 4 faded fuchsia bags.
pale olive bags contain 3 plaid red bags, 5 posh maroon bags.
vibrant brown bags contain 1 plaid white bag, 3 dotted gold bags, 2 faded chartreuse bags.
bright orange bags contain 2 shiny magenta bags.
light coral bags contain 3 faded black bags, 4 faded coral bags, 4 plaid teal bags, 1 dull aqua bag.
dull silver bags contain 2 drab salmon bags, 2 shiny violet bags, 1 dull aqua bag, 5 faded black bags.
striped cyan bags contain 1 faded purple bag.
dim beige bags contain 5 wavy violet bags.
dotted coral bags contain 4 dim salmon bags, 5 clear beige bags, 2 shiny bronze bags, 2 light tan bags.
faded aqua bags contain 3 bright magenta bags, 3 posh olive bags.
mirrored tan bags contain 5 plaid silver bags, 5 striped gray bags.
striped beige bags contain 4 dull yellow bags.
wavy coral bags contain no other bags.
dark indigo bags contain 1 drab olive bag, 2 faded cyan bags, 5 dim yellow bags.
dark white bags contain 1 vibrant gray bag, 3 mirrored plum bags, 5 clear lavender bags, 1 shiny purple bag.
muted maroon bags contain 1 dim blue bag, 1 pale silver bag.
dotted gray bags contain 1 mirrored teal bag, 2 shiny gold bags, 5 drab gold bags.
dull tan bags contain 4 bright silver bags, 4 pale lavender bags, 3 wavy gray bags.
dark chartreuse bags contain 2 wavy tan bags, 1 striped orange bag, 1 posh salmon bag.
wavy gray bags contain no other bags.
drab brown bags contain no other bags.
dotted red bags contain 2 shiny yellow bags, 1 muted yellow bag, 2 pale lime bags.
bright black bags contain 4 striped gray bags, 2 dull yellow bags.
clear tan bags contain 3 shiny gold bags, 1 dark magenta bag, 5 bright aqua bags, 1 clear maroon bag.
dim silver bags contain 2 pale green bags, 3 clear orange bags, 2 pale white bags, 1 posh yellow bag.
mirrored chartreuse bags contain 1 wavy gray bag, 5 shiny magenta bags, 2 plaid purple bags, 2 dotted beige bags.
striped indigo bags contain 5 pale bronze bags, 1 muted blue bag.
dull plum bags contain 2 plaid red bags, 5 bright plum bags.
striped tan bags contain 3 vibrant aqua bags, 2 muted blue bags.
dotted teal bags contain 3 vibrant tan bags, 3 bright plum bags.
wavy white bags contain 2 muted black bags, 2 muted tomato bags, 4 bright gold bags.
muted lavender bags contain 3 clear beige bags.
striped salmon bags contain 1 faded coral bag, 1 clear green bag.
vibrant tomato bags contain 3 shiny violet bags.
dim olive bags contain 2 faded tan bags, 3 mirrored maroon bags, 3 dark crimson bags, 5 muted cyan bags.
dotted lime bags contain 5 muted violet bags, 3 light beige bags, 2 drab brown bags.
striped purple bags contain 2 dull gray bags.
wavy tomato bags contain 1 posh crimson bag, 5 vibrant tan bags, 3 bright maroon bags.
bright lavender bags contain 2 mirrored lavender bags, 4 shiny cyan bags.
faded turquoise bags contain 3 dull gray bags, 5 dull yellow bags, 5 dotted bronze bags, 4 vibrant aqua bags.
vibrant olive bags contain 4 dull violet bags, 5 dark coral bags.
bright cyan bags contain 3 bright turquoise bags.
pale aqua bags contain 5 shiny green bags, 3 clear silver bags, 4 muted tan bags.
vibrant cyan bags contain 2 vibrant maroon bags, 5 plaid magenta bags, 1 light black bag, 5 bright maroon bags.
striped lime bags contain 4 faded red bags, 3 mirrored brown bags, 4 dim plum bags, 4 wavy silver bags.
pale gold bags contain 5 posh plum bags, 1 dull tomato bag, 3 dark teal bags, 4 shiny black bags.
drab black bags contain 5 pale brown bags.
wavy maroon bags contain 1 dull yellow bag, 4 dim crimson bags, 1 dim lavender bag, 2 drab brown bags.
plaid gold bags contain 2 dotted gray bags, 2 pale orange bags, 5 mirrored brown bags.
shiny gray bags contain 3 faded lavender bags, 3 drab yellow bags, 3 wavy green bags.
bright beige bags contain 2 drab turquoise bags.
muted red bags contain 4 wavy gray bags, 5 mirrored lime bags.
bright violet bags contain 5 striped cyan bags, 2 pale blue bags, 1 clear plum bag.
plaid bronze bags contain 5 muted green bags, 5 posh gray bags, 1 dull silver bag, 4 faded black bags.
shiny gold bags contain 4 wavy green bags, 2 mirrored teal bags, 4 dark tomato bags, 2 faded beige bags.
plaid cyan bags contain 5 bright green bags.
posh green bags contain 5 mirrored beige bags.
dull purple bags contain 5 dull blue bags.
pale fuchsia bags contain 4 mirrored cyan bags, 1 faded red bag, 5 wavy green bags.
wavy olive bags contain 5 dotted olive bags, 3 shiny tan bags, 4 dotted magenta bags, 2 clear violet bags.
faded tan bags contain 3 plaid teal bags, 5 muted tomato bags.
pale blue bags contain 4 faded plum bags, 5 wavy green bags, 3 shiny violet bags, 2 faded black bags.
vibrant blue bags contain 1 shiny yellow bag, 2 clear tan bags, 5 posh crimson bags.
mirrored beige bags contain 5 shiny magenta bags, 3 pale blue bags.
dark maroon bags contain 4 bright green bags, 5 faded bronze bags, 1 faded indigo bag, 3 dotted teal bags.
plaid violet bags contain 4 posh yellow bags, 3 faded cyan bags, 1 mirrored lime bag, 2 striped black bags.
wavy indigo bags contain 5 dotted aqua bags, 1 drab salmon bag, 5 bright cyan bags, 4 dotted purple bags.
dull violet bags contain 1 vibrant tomato bag, 4 plaid blue bags, 5 shiny plum bags, 2 dotted aqua bags.
dotted salmon bags contain 5 plaid gray bags.
drab salmon bags contain 4 faded yellow bags.
light maroon bags contain 5 bright cyan bags.
drab cyan bags contain 2 dark beige bags, 1 dotted purple bag, 5 dark coral bags.
faded salmon bags contain 4 clear bronze bags, 4 muted green bags, 1 faded plum bag, 4 bright silver bags.
clear turquoise bags contain 5 shiny silver bags, 5 striped maroon bags, 5 posh chartreuse bags.
clear silver bags contain 5 vibrant fuchsia bags, 5 vibrant lime bags, 5 faded red bags.
muted magenta bags contain 3 dotted teal bags, 3 wavy orange bags.
striped aqua bags contain 4 bright green bags, 2 mirrored maroon bags, 5 muted gold bags, 2 pale brown bags.
drab magenta bags contain 5 vibrant tomato bags, 1 wavy violet bag.
clear yellow bags contain 4 drab salmon bags.
striped gold bags contain 3 dull salmon bags.
posh black bags contain 2 dim black bags, 4 plaid crimson bags.
drab fuchsia bags contain 1 drab turquoise bag.
mirrored fuchsia bags contain 5 shiny cyan bags, 4 dim crimson bags, 2 drab brown bags.
pale lavender bags contain 1 shiny lavender bag, 4 mirrored fuchsia bags, 1 wavy silver bag, 1 bright black bag.
light teal bags contain 2 vibrant fuchsia bags, 4 mirrored indigo bags.
light cyan bags contain 5 mirrored cyan bags, 1 faded fuchsia bag.
wavy lavender bags contain 1 faded gray bag.
clear purple bags contain 4 light red bags, 3 shiny teal bags.
mirrored coral bags contain 2 bright tomato bags, 4 drab fuchsia bags, 4 pale salmon bags, 1 wavy teal bag.
muted crimson bags contain 2 faded lime bags, 2 wavy plum bags, 5 bright gold bags.
plaid silver bags contain 4 wavy coral bags, 3 shiny violet bags, 5 faded beige bags.
posh orange bags contain 4 dim blue bags, 4 mirrored lime bags, 1 muted chartreuse bag.
dotted olive bags contain 4 dim plum bags, 5 bright aqua bags.
vibrant black bags contain 3 dark purple bags.
dim turquoise bags contain 3 shiny coral bags, 4 dotted indigo bags, 4 muted yellow bags, 4 dull bronze bags.
light gray bags contain 1 plaid silver bag, 4 faded purple bags, 3 faded green bags.
muted white bags contain 2 faded yellow bags, 4 dark white bags, 3 drab green bags, 4 dim yellow bags.
pale gray bags contain 4 pale brown bags, 3 dotted indigo bags, 1 mirrored indigo bag, 1 bright silver bag.
dull brown bags contain 1 plaid silver bag, 2 pale bronze bags, 3 dark magenta bags, 5 posh yellow bags.
bright indigo bags contain 4 dull red bags, 5 dark yellow bags.
dotted purple bags contain 2 muted yellow bags.
bright salmon bags contain 2 vibrant orange bags, 4 vibrant bronze bags, 4 shiny coral bags, 3 drab brown bags.
shiny chartreuse bags contain 1 dotted red bag, 4 wavy lavender bags, 2 muted aqua bags.
light brown bags contain 3 dark teal bags, 3 faded lime bags, 5 bright coral bags, 5 plaid red bags.
dim orange bags contain 4 clear lime bags, 2 plaid teal bags, 4 plaid lavender bags.
wavy teal bags contain 3 drab chartreuse bags.
posh purple bags contain 4 striped salmon bags, 2 mirrored black bags.
dim cyan bags contain 5 mirrored fuchsia bags, 5 dotted bronze bags, 1 light violet bag.
clear fuchsia bags contain 3 dim yellow bags, 1 pale yellow bag.
muted fuchsia bags contain 2 mirrored beige bags, 4 dull black bags, 5 mirrored red bags.
striped bronze bags contain 3 muted violet bags, 4 dull brown bags, 4 drab silver bags, 5 dotted maroon bags.
bright silver bags contain 2 drab gray bags, 3 wavy coral bags, 4 posh yellow bags.
light tomato bags contain 1 muted green bag, 3 bright indigo bags, 1 wavy blue bag.
dark red bags contain 1 dim brown bag.
vibrant fuchsia bags contain 1 shiny gold bag.
vibrant crimson bags contain 4 dull olive bags, 1 striped orange bag.
clear lime bags contain 5 dull crimson bags.
clear lavender bags contain 2 dotted gold bags, 3 light crimson bags, 3 mirrored red bags, 2 dark purple bags.
dark silver bags contain 4 muted silver bags.
posh white bags contain 3 light maroon bags, 5 dotted brown bags, 5 light yellow bags.
dark gold bags contain 4 muted plum bags, 4 posh silver bags.
dotted cyan bags contain 4 shiny magenta bags, 3 drab red bags.
plaid chartreuse bags contain 3 posh fuchsia bags, 4 light white bags.
dim lime bags contain 2 dull green bags, 5 posh magenta bags.
shiny indigo bags contain 5 light violet bags, 3 plaid orange bags, 2 drab turquoise bags, 5 striped beige bags.
bright tan bags contain 3 dotted fuchsia bags, 1 dim yellow bag, 2 mirrored violet bags, 2 plaid silver bags.
mirrored green bags contain 2 plaid turquoise bags, 5 bright turquoise bags, 5 light lime bags, 5 plaid white bags.
light purple bags contain 2 striped silver bags.
shiny violet bags contain 4 dull yellow bags, 1 faded red bag, 3 pale lime bags, 4 drab brown bags.
pale coral bags contain 5 drab indigo bags.
faded olive bags contain 4 posh tan bags, 3 striped orange bags, 3 wavy gold bags.
wavy cyan bags contain 3 mirrored teal bags.
wavy magenta bags contain 5 bright coral bags, 2 dark black bags, 1 muted beige bag.
wavy green bags contain 2 light violet bags.
shiny purple bags contain 5 wavy orange bags, 3 striped turquoise bags.
wavy orange bags contain 2 bright turquoise bags, 3 mirrored lime bags, 5 light violet bags.
shiny crimson bags contain 5 plaid olive bags, 2 mirrored turquoise bags, 3 posh lavender bags, 4 muted bronze bags.
dark tomato bags contain 3 posh maroon bags, 5 dotted purple bags, 1 shiny violet bag, 2 drab silver bags.
clear green bags contain 1 light black bag.
clear indigo bags contain 5 vibrant crimson bags.
muted coral bags contain 2 mirrored black bags, 4 dull silver bags.
clear teal bags contain 1 posh tan bag, 3 faded plum bags, 3 wavy maroon bags, 1 mirrored lavender bag.
shiny tomato bags contain 1 clear tomato bag, 5 bright gray bags, 1 striped cyan bag, 5 vibrant lavender bags.
shiny silver bags contain 2 dim violet bags, 2 striped teal bags, 2 mirrored beige bags, 3 drab turquoise bags.
posh indigo bags contain 5 drab fuchsia bags.
dull lime bags contain 5 vibrant cyan bags, 5 vibrant chartreuse bags.
mirrored lavender bags contain 2 drab gold bags, 5 vibrant aqua bags, 1 plaid teal bag.
faded coral bags contain 2 clear tan bags, 4 faded green bags, 2 faded fuchsia bags, 3 drab brown bags.
mirrored purple bags contain 1 plaid black bag, 5 dim teal bags, 4 muted bronze bags.
bright lime bags contain 1 light lavender bag.
pale turquoise bags contain 2 striped silver bags, 2 muted tan bags, 4 vibrant lime bags, 4 faded lime bags.
posh cyan bags contain 4 bright salmon bags.
wavy bronze bags contain 1 drab olive bag, 5 plaid orange bags, 1 wavy silver bag, 2 faded bronze bags.
light tan bags contain 3 faded violet bags.
mirrored brown bags contain 2 pale lime bags, 2 dull gray bags, 5 dotted bronze bags.
posh lime bags contain 4 dotted beige bags.
drab maroon bags contain 5 wavy gray bags, 4 posh magenta bags, 2 dull gray bags.
light yellow bags contain 4 striped lime bags, 3 faded purple bags, 1 plaid silver bag, 2 muted violet bags.
vibrant silver bags contain 3 posh purple bags.
mirrored plum bags contain 1 muted salmon bag, 4 light salmon bags, 2 faded brown bags.
mirrored gray bags contain 1 wavy silver bag, 1 dotted maroon bag, 4 posh maroon bags, 3 muted blue bags.
light blue bags contain 5 striped magenta bags, 2 dim plum bags, 4 muted tomato bags.
dim violet bags contain 4 dotted maroon bags, 1 pale lime bag, 2 mirrored brown bags, 2 bright salmon bags.
dotted violet bags contain 2 dim maroon bags, 3 faded beige bags.
shiny red bags contain 1 wavy gray bag, 3 clear bronze bags.
dotted black bags contain 4 pale fuchsia bags.
mirrored gold bags contain 3 pale cyan bags, 1 dark green bag, 5 plaid white bags, 1 drab black bag.
shiny plum bags contain 1 posh crimson bag, 5 bright yellow bags, 1 dull indigo bag.
dotted brown bags contain 5 dotted black bags, 2 clear yellow bags, 1 mirrored violet bag, 4 shiny gold bags.
faded orange bags contain 3 posh indigo bags, 3 bright magenta bags, 2 light teal bags, 2 bright turquoise bags.
mirrored tomato bags contain 1 dim bronze bag, 1 bright salmon bag, 4 dark purple bags, 4 light olive bags.
dotted orange bags contain 3 faded brown bags.
dull red bags contain 1 plaid black bag.
dim purple bags contain 3 vibrant purple bags, 2 dim cyan bags, 3 clear tan bags, 5 wavy beige bags.
dull coral bags contain 5 drab chartreuse bags.
dull black bags contain 1 vibrant bronze bag.
pale crimson bags contain 4 striped brown bags.
faded green bags contain 2 shiny gold bags, 5 dim maroon bags.
shiny bronze bags contain 4 dull turquoise bags.
dotted tomato bags contain 3 clear teal bags, 2 wavy crimson bags, 4 clear tan bags.
pale purple bags contain 2 shiny aqua bags.
bright teal bags contain 2 drab salmon bags, 4 dim yellow bags, 1 drab maroon bag.
pale tomato bags contain 3 striped black bags, 2 mirrored fuchsia bags.
striped silver bags contain 1 wavy turquoise bag.
dim gold bags contain 5 dim crimson bags, 4 dim violet bags, 2 striped bronze bags.
light orange bags contain 2 mirrored turquoise bags, 5 bright crimson bags, 4 pale tan bags, 1 drab teal bag.
wavy salmon bags contain 3 plaid orange bags, 2 faded cyan bags, 3 clear purple bags, 5 dotted orange bags.
vibrant chartreuse bags contain 2 plaid red bags, 3 dull aqua bags, 1 mirrored brown bag.
striped orange bags contain 4 dim crimson bags, 2 wavy coral bags, 1 dim plum bag.
light black bags contain 2 clear bronze bags, 2 posh cyan bags, 1 vibrant fuchsia bag.
dark salmon bags contain 2 vibrant tan bags, 1 shiny chartreuse bag.
drab gold bags contain 4 dim crimson bags, 2 light violet bags, 1 vibrant orange bag.
bright bronze bags contain 3 clear green bags.
dim coral bags contain 3 dark red bags, 5 dim lavender bags.
dull orange bags contain 5 drab black bags, 1 dotted violet bag, 3 dim blue bags.
clear brown bags contain 2 dark red bags, 1 dull turquoise bag, 1 mirrored red bag, 5 wavy beige bags.
muted tan bags contain 3 dotted teal bags, 3 mirrored cyan bags, 5 faded fuchsia bags, 2 drab white bags.
faded lavender bags contain 1 muted silver bag, 1 mirrored brown bag, 3 dark tomato bags, 3 pale lime bags.
dim bronze bags contain 1 bright yellow bag.
wavy lime bags contain 4 bright aqua bags, 5 wavy silver bags.
dark black bags contain 4 dark green bags.
faded lime bags contain 1 faded lavender bag, 5 plaid gray bags, 3 posh turquoise bags, 5 faded bronze bags.
drab lime bags contain 1 light cyan bag, 4 dotted red bags.
dull olive bags contain 3 dim plum bags, 3 pale lime bags, 4 posh yellow bags, 5 shiny violet bags.
clear black bags contain 1 faded fuchsia bag, 3 posh aqua bags.
dark crimson bags contain 2 dotted beige bags.
faded cyan bags contain 5 clear blue bags.
pale tan bags contain 4 posh aqua bags, 5 dim yellow bags, 2 light chartreuse bags.
light red bags contain 3 faded fuchsia bags, 5 dotted purple bags, 2 mirrored indigo bags, 3 shiny violet bags.
muted olive bags contain 5 posh tan bags, 4 faded tan bags.
plaid yellow bags contain 4 faded coral bags.
clear tomato bags contain 3 plaid salmon bags, 2 faded lavender bags.
vibrant maroon bags contain 3 muted lime bags, 4 vibrant fuchsia bags, 4 drab yellow bags.
posh red bags contain 5 posh cyan bags, 2 faded black bags, 1 bright crimson bag, 5 wavy plum bags.
mirrored silver bags contain 5 dull aqua bags.
wavy yellow bags contain 3 faded white bags, 1 dotted fuchsia bag.
light plum bags contain 1 vibrant bronze bag, 4 vibrant green bags, 1 plaid turquoise bag, 4 posh cyan bags.
shiny lime bags contain 1 posh tomato bag, 4 mirrored cyan bags, 2 plaid white bags, 3 shiny aqua bags.
light gold bags contain 1 drab silver bag, 3 clear brown bags, 2 wavy fuchsia bags.
dotted indigo bags contain 2 plaid teal bags, 1 dull yellow bag.
bright fuchsia bags contain 3 faded teal bags, 2 faded silver bags, 3 dim red bags, 1 muted lime bag.
mirrored black bags contain 5 muted violet bags.
dark magenta bags contain 5 dim crimson bags.
shiny yellow bags contain 3 clear tan bags.
muted orange bags contain 3 striped bronze bags.
dull bronze bags contain 1 dotted gray bag, 2 clear bronze bags, 5 light turquoise bags.
mirrored blue bags contain 3 shiny coral bags.
vibrant turquoise bags contain 2 pale blue bags, 4 shiny beige bags.
pale green bags contain 1 posh crimson bag, 2 drab gold bags, 3 drab brown bags.
striped yellow bags contain 5 mirrored red bags, 4 plaid salmon bags, 4 muted salmon bags, 5 faded tan bags.
faded tomato bags contain 5 clear blue bags.
faded teal bags contain 2 posh teal bags, 3 light violet bags, 5 dotted olive bags, 3 shiny teal bags.
clear blue bags contain 3 dull yellow bags, 3 light violet bags, 2 wavy coral bags, 4 shiny cyan bags.
dotted blue bags contain 5 muted coral bags, 4 muted salmon bags.
shiny lavender bags contain 2 dotted crimson bags, 4 light lime bags, 1 posh cyan bag.
mirrored magenta bags contain 3 mirrored fuchsia bags, 3 clear teal bags, 4 muted fuchsia bags.
faded yellow bags contain 1 dim crimson bag, 3 dull cyan bags.
muted teal bags contain 3 dull red bags.
light lavender bags contain 4 striped orange bags, 2 mirrored beige bags.
posh chartreuse bags contain 2 dark purple bags.
pale beige bags contain 4 pale silver bags, 2 striped crimson bags.
pale lime bags contain no other bags.
faded blue bags contain 1 mirrored red bag, 3 drab cyan bags, 3 dull yellow bags, 5 plaid plum bags.
dull maroon bags contain 5 light blue bags, 3 dull crimson bags, 3 clear yellow bags.
dim plum bags contain no other bags.
drab beige bags contain 5 light black bags, 1 striped teal bag, 4 mirrored violet bags.
pale orange bags contain 4 clear chartreuse bags.
dotted beige bags contain 4 dark yellow bags, 3 light black bags, 5 bright aqua bags.
plaid salmon bags contain 3 posh silver bags, 2 wavy violet bags, 3 striped tan bags.
clear gray bags contain 4 wavy purple bags.
drab coral bags contain 2 faded silver bags, 3 light fuchsia bags, 2 dull indigo bags, 3 drab cyan bags.
dark yellow bags contain 2 mirrored fuchsia bags.
posh turquoise bags contain 2 dim lavender bags, 1 muted yellow bag, 4 bright plum bags.
bright tomato bags contain 5 striped orange bags, 3 bright turquoise bags, 3 dull yellow bags.
drab silver bags contain 2 light turquoise bags, 3 mirrored indigo bags, 4 vibrant orange bags.
clear cyan bags contain 4 muted cyan bags, 2 faded silver bags, 3 faded yellow bags, 4 faded crimson bags.
mirrored orange bags contain 3 dark green bags, 5 drab salmon bags, 4 posh gray bags.
muted gray bags contain 2 mirrored lime bags.
pale brown bags contain 4 dull gray bags.
wavy silver bags contain 5 faded red bags, 5 muted silver bags.
dull blue bags contain 1 dotted olive bag, 4 muted violet bags.
dull magenta bags contain 4 muted silver bags, 4 posh salmon bags, 4 plaid tomato bags.
dark cyan bags contain 5 shiny purple bags, 3 vibrant coral bags, 1 posh green bag, 2 dull cyan bags.
shiny turquoise bags contain 3 pale white bags, 5 dotted black bags.
dark green bags contain 4 dim maroon bags.
posh magenta bags contain 2 pale brown bags.
dull salmon bags contain 5 posh magenta bags, 5 dotted indigo bags, 4 drab orange bags, 5 mirrored gray bags.
dull gray bags contain 5 wavy coral bags, 5 vibrant tan bags, 5 mirrored olive bags.
dull turquoise bags contain 3 clear black bags, 5 striped indigo bags, 3 shiny white bags, 2 faded fuchsia bags.
striped violet bags contain 2 faded white bags.
muted brown bags contain 2 dim cyan bags, 4 drab black bags, 5 clear bronze bags, 1 shiny green bag.
drab plum bags contain 2 dark teal bags, 5 plaid lavender bags, 4 mirrored blue bags.
striped green bags contain 1 mirrored olive bag, 3 clear green bags, 3 dim yellow bags, 3 muted red bags.
bright white bags contain 5 shiny coral bags, 5 faded fuchsia bags.
vibrant tan bags contain no other bags.
faded white bags contain 4 pale crimson bags, 1 plaid green bag, 5 faded bronze bags.
clear orange bags contain 3 bright cyan bags, 4 dotted green bags, 3 faded purple bags, 3 faded black bags.
drab chartreuse bags contain 5 wavy gray bags, 4 muted turquoise bags.
mirrored aqua bags contain 2 bright crimson bags, 4 mirrored magenta bags, 3 clear teal bags.
wavy crimson bags contain 5 posh yellow bags, 3 clear blue bags, 1 striped lime bag, 2 faded cyan bags.
shiny black bags contain 4 dim cyan bags, 3 striped beige bags, 3 posh beige bags, 4 bright gold bags.
wavy brown bags contain 2 wavy coral bags, 3 shiny yellow bags.
pale plum bags contain 3 drab olive bags, 1 light turquoise bag.
drab green bags contain 1 mirrored orange bag, 5 dark turquoise bags, 5 posh chartreuse bags, 2 pale magenta bags.
drab teal bags contain 5 faded silver bags, 4 striped brown bags, 4 drab purple bags.
dull gold bags contain 1 dark orange bag, 4 faded lime bags.
posh gray bags contain 1 posh cyan bag, 2 plaid crimson bags, 1 plaid olive bag, 2 bright yellow bags.
dim red bags contain 3 posh chartreuse bags, 4 drab white bags, 2 bright green bags, 4 drab yellow bags.
dull chartreuse bags contain 1 drab fuchsia bag, 2 dull crimson bags, 4 light coral bags.
plaid magenta bags contain 1 mirrored silver bag.
drab crimson bags contain 3 faded tan bags.
faded bronze bags contain 4 dim plum bags, 4 faded fuchsia bags, 4 bright aqua bags, 2 vibrant orange bags.
plaid gray bags contain 3 light fuchsia bags, 1 dotted turquoise bag.
vibrant bronze bags contain 1 wavy green bag, 2 muted yellow bags.
clear maroon bags contain 3 dim plum bags, 4 light red bags, 5 wavy silver bags.
drab blue bags contain 1 plaid gray bag, 5 mirrored gray bags, 5 shiny magenta bags.
posh bronze bags contain 3 muted crimson bags, 5 wavy gray bags.
dim black bags contain 1 bright green bag, 3 dim maroon bags, 4 mirrored cyan bags, 4 faded black bags.
vibrant green bags contain 4 vibrant blue bags, 4 wavy gold bags, 5 vibrant fuchsia bags, 3 muted yellow bags.
dim teal bags contain 5 faded fuchsia bags, 3 striped lavender bags, 2 pale lime bags, 4 clear maroon bags.
posh silver bags contain 2 shiny magenta bags.
plaid blue bags contain 2 pale brown bags, 4 drab brown bags, 2 drab plum bags, 1 wavy maroon bag.
dim fuchsia bags contain 3 dark purple bags, 4 shiny red bags, 1 clear chartreuse bag, 2 pale gold bags.
muted turquoise bags contain 4 striped maroon bags, 1 dim lavender bag, 2 clear beige bags, 3 wavy maroon bags.
shiny beige bags contain 4 shiny red bags, 1 vibrant bronze bag, 5 plaid chartreuse bags, 3 mirrored teal bags.
muted blue bags contain 3 pale lime bags, 4 dim crimson bags.
faded black bags contain 4 striped beige bags, 4 muted blue bags.
muted plum bags contain 5 drab white bags, 2 dull cyan bags, 1 light gray bag.
dark tan bags contain 2 light aqua bags.
clear white bags contain 5 dotted plum bags.
dotted aqua bags contain 4 posh turquoise bags, 5 bright aqua bags.
posh gold bags contain 5 pale crimson bags, 4 light fuchsia bags, 4 plaid turquoise bags.
bright turquoise bags contain 3 mirrored brown bags, 2 dotted black bags, 3 dull indigo bags, 4 plaid white bags.
light white bags contain 5 mirrored brown bags, 2 dim magenta bags.
posh crimson bags contain 1 bright green bag, 3 posh yellow bags, 4 posh turquoise bags, 4 vibrant aqua bags.
muted silver bags contain 1 dotted purple bag, 2 posh yellow bags, 5 mirrored indigo bags, 4 shiny violet bags.
pale indigo bags contain 2 mirrored aqua bags, 1 vibrant tomato bag, 5 striped violet bags, 2 shiny white bags.
vibrant aqua bags contain 5 pale bronze bags, 5 posh yellow bags, 2 dull cyan bags, 2 bright silver bags.
posh brown bags contain 2 bright green bags, 4 mirrored fuchsia bags, 4 dotted salmon bags.
shiny orange bags contain 2 faded lavender bags, 3 dull yellow bags.
shiny fuchsia bags contain 2 striped teal bags.
dark lavender bags contain 4 mirrored teal bags, 5 plaid gray bags.
vibrant teal bags contain 3 drab orange bags, 1 plaid red bag, 4 clear cyan bags.
dotted lavender bags contain 5 pale gray bags.
plaid lime bags contain 5 bright maroon bags, 2 dim tomato bags, 2 mirrored teal bags.
dim white bags contain 3 plaid turquoise bags, 2 faded red bags, 5 striped orange bags.
shiny coral bags contain 2 posh turquoise bags.
posh coral bags contain 4 bright salmon bags, 4 dim coral bags, 1 pale fuchsia bag.
drab aqua bags contain 1 vibrant maroon bag, 4 muted green bags, 5 muted red bags.
dim crimson bags contain no other bags.
vibrant purple bags contain 5 dark teal bags, 3 muted crimson bags.
dull fuchsia bags contain 5 dull aqua bags, 3 clear silver bags.
dotted green bags contain 3 dull tomato bags, 3 drab black bags, 5 dim red bags.
muted green bags contain 4 light cyan bags, 2 light red bags, 3 posh turquoise bags, 3 dark orange bags.
wavy aqua bags contain 4 faded white bags, 5 dim brown bags, 2 plaid salmon bags.
light magenta bags contain 4 dotted black bags, 3 posh blue bags, 2 bright coral bags.
light aqua bags contain 1 light yellow bag, 1 plaid gray bag, 1 vibrant cyan bag, 4 dotted aqua bags.
dark purple bags contain 2 plaid silver bags, 2 muted gray bags, 1 clear maroon bag.
wavy violet bags contain 4 plaid white bags, 5 dull red bags.
faded plum bags contain 5 posh beige bags, 2 light turquoise bags, 5 vibrant orange bags.
dull beige bags contain 2 dark blue bags, 2 shiny green bags.
clear crimson bags contain 1 vibrant salmon bag.
drab violet bags contain 4 faded purple bags, 4 plaid turquoise bags.
dull white bags contain 4 striped brown bags, 5 wavy black bags.
dark teal bags contain 3 faded fuchsia bags, 2 dotted maroon bags, 4 plaid orange bags.
dark blue bags contain 3 shiny bronze bags, 4 bright yellow bags, 1 vibrant bronze bag, 5 dull blue bags.
vibrant salmon bags contain 4 drab aqua bags.
plaid coral bags contain 2 drab salmon bags.
vibrant gray bags contain 3 dark purple bags, 3 vibrant green bags, 2 clear teal bags.
clear gold bags contain 3 mirrored green bags, 4 plaid gray bags, 1 bright gray bag.
posh salmon bags contain 2 shiny bronze bags, 3 faded coral bags, 3 mirrored chartreuse bags, 3 vibrant green bags.
wavy red bags contain 1 posh brown bag.
faded red bags contain 5 dim lavender bags, 4 bright plum bags, 4 striped orange bags.
striped lavender bags contain 4 dull black bags, 4 dark crimson bags, 1 posh turquoise bag, 4 light beige bags.
dull tomato bags contain 2 wavy silver bags, 3 muted yellow bags, 3 wavy maroon bags, 2 dotted black bags.
shiny salmon bags contain 1 wavy turquoise bag, 4 dull green bags, 5 dull aqua bags.
pale yellow bags contain 1 dull gray bag.
clear olive bags contain 1 posh crimson bag, 4 pale crimson bags.
clear coral bags contain 4 dark orange bags, 4 dim crimson bags.
dark bronze bags contain 4 mirrored silver bags, 3 light plum bags.
bright aqua bags contain 1 vibrant tan bag, 3 clear blue bags, 2 shiny violet bags.
striped blue bags contain 5 muted tomato bags, 5 muted magenta bags, 5 drab white bags, 3 pale crimson bags.
dim lavender bags contain 2 posh yellow bags.
dim green bags contain 2 mirrored chartreuse bags, 5 plaid orange bags.
plaid maroon bags contain 1 dark magenta bag, 1 posh beige bag, 5 drab plum bags, 5 bright aqua bags.
pale maroon bags contain 1 clear bronze bag, 1 plaid blue bag.
clear salmon bags contain 1 dark coral bag.
shiny magenta bags contain 3 vibrant aqua bags, 3 dim maroon bags.
mirrored yellow bags contain 4 wavy black bags, 4 pale gray bags, 4 mirrored magenta bags.
shiny green bags contain 3 striped lime bags, 2 posh yellow bags.
dim aqua bags contain 4 dotted aqua bags.
mirrored olive bags contain 1 muted blue bag, 5 vibrant tan bags, 5 posh yellow bags.
mirrored violet bags contain 1 plaid orange bag, 4 drab salmon bags.
pale chartreuse bags contain 2 muted tomato bags, 3 faded indigo bags.
striped maroon bags contain 4 shiny lime bags.
muted indigo bags contain 4 dim magenta bags, 3 muted orange bags, 2 dim beige bags, 4 vibrant purple bags.
dim maroon bags contain 2 pale bronze bags, 4 bright aqua bags.
pale teal bags contain 5 dark gray bags, 2 dark tomato bags, 1 dull red bag.
posh aqua bags contain 3 mirrored lavender bags.
vibrant lime bags contain 2 wavy silver bags.
dark turquoise bags contain 2 wavy black bags.
vibrant gold bags contain 2 striped brown bags, 2 faded indigo bags.
faded maroon bags contain 4 mirrored tan bags, 3 posh beige bags, 5 posh orange bags.
faded fuchsia bags contain 1 bright salmon bag.
light fuchsia bags contain 2 dull black bags.
striped coral bags contain 1 dull green bag, 2 muted beige bags, 2 bright coral bags, 5 wavy orange bags.
bright brown bags contain 4 plaid gold bags.
plaid olive bags contain 2 dim coral bags.
dull yellow bags contain 3 drab brown bags.
posh tomato bags contain 3 dotted purple bags.
clear magenta bags contain 1 mirrored brown bag, 5 dotted plum bags, 1 light coral bag, 2 drab maroon bags.
faded indigo bags contain 1 drab gold bag.
plaid white bags contain 5 mirrored fuchsia bags.
bright green bags contain 1 posh beige bag, 5 dark green bags, 4 dull aqua bags.
bright gray bags contain 3 light lavender bags.
posh violet bags contain 2 vibrant tan bags, 5 pale magenta bags, 3 posh white bags, 5 mirrored gray bags.
dull teal bags contain 1 dull brown bag, 2 drab gray bags, 2 shiny cyan bags, 1 mirrored lavender bag.
shiny cyan bags contain 1 bright plum bag, 1 shiny violet bag.
posh plum bags contain 4 drab brown bags, 4 mirrored olive bags, 4 dim maroon bags, 4 striped orange bags.
plaid fuchsia bags contain 5 drab blue bags.
dull green bags contain 1 mirrored red bag, 1 bright turquoise bag, 2 dark beige bags.
bright chartreuse bags contain 5 dim white bags, 2 faded red bags.
faded beige bags contain 5 posh turquoise bags, 5 vibrant tan bags, 2 posh yellow bags, 4 mirrored indigo bags.
dim chartreuse bags contain 1 posh magenta bag, 2 dotted crimson bags, 5 clear black bags, 4 striped olive bags.
drab indigo bags contain 5 striped orange bags, 1 pale chartreuse bag, 2 mirrored indigo bags, 4 clear purple bags.
light bronze bags contain 4 muted red bags.
shiny teal bags contain 3 faded beige bags, 2 striped beige bags, 2 mirrored olive bags, 5 plaid white bags.
shiny white bags contain 2 wavy silver bags, 3 plaid turquoise bags, 1 dim plum bag, 4 posh plum bags.
pale silver bags contain 2 pale cyan bags, 5 muted teal bags, 5 plaid turquoise bags, 2 clear coral bags.
dim yellow bags contain 2 vibrant tomato bags, 3 bright salmon bags, 4 dull gray bags.
mirrored indigo bags contain 5 posh yellow bags, 5 faded red bags.
clear bronze bags contain 1 posh turquoise bag, 3 faded black bags, 3 shiny coral bags.
mirrored turquoise bags contain 2 mirrored teal bags, 4 striped black bags, 4 dull teal bags, 4 clear black bags.
mirrored red bags contain 3 clear purple bags, 5 light red bags, 5 mirrored beige bags.
bright olive bags contain 3 vibrant plum bags.
drab white bags contain 4 dim lavender bags.
clear red bags contain 5 dark gray bags, 1 shiny green bag, 2 striped brown bags, 3 plaid olive bags.
vibrant red bags contain 2 dull bronze bags, 2 dotted magenta bags, 5 dark red bags, 1 drab magenta bag.
striped crimson bags contain 4 dull silver bags, 4 dark gray bags, 4 light red bags, 2 posh chartreuse bags.
dotted tan bags contain 4 shiny lime bags.
plaid orange bags contain 1 wavy maroon bag, 2 drab brown bags, 5 dull black bags.
clear plum bags contain 2 muted yellow bags, 5 faded turquoise bags, 1 faded beige bag, 1 dull aqua bag.
mirrored bronze bags contain 5 posh magenta bags.
mirrored cyan bags contain 4 striped orange bags, 3 wavy gray bags, 1 mirrored olive bag, 2 dim lavender bags.
striped white bags contain 4 striped aqua bags.
bright red bags contain 4 dotted gray bags, 4 dark green bags, 4 shiny aqua bags, 4 shiny indigo bags.
dim blue bags contain 1 dull black bag, 4 dotted turquoise bags.
dotted bronze bags contain 5 mirrored indigo bags, 4 wavy coral bags.
muted gold bags contain 4 wavy plum bags.
clear aqua bags contain 2 clear teal bags, 4 mirrored crimson bags, 1 dull silver bag, 3 bright crimson bags.
dim brown bags contain 3 clear green bags, 5 bright cyan bags.
bright plum bags contain 3 striped orange bags, 2 pale lime bags.
bright blue bags contain 1 shiny violet bag, 4 wavy gold bags.
bright maroon bags contain 1 striped indigo bag, 3 striped beige bags, 1 shiny teal bag.
pale cyan bags contain 1 dull gray bag, 2 mirrored lime bags.
wavy chartreuse bags contain 5 dark red bags, 5 plaid fuchsia bags, 2 dim salmon bags.
dull cyan bags contain 2 dim lavender bags, 3 dull yellow bags, 5 dim crimson bags, 5 dull gray bags.
shiny brown bags contain 3 wavy aqua bags, 2 faded lime bags.
dim tan bags contain 5 pale orange bags, 2 mirrored blue bags.
drab purple bags contain 1 vibrant bronze bag, 4 pale magenta bags.
wavy fuchsia bags contain 3 bright aqua bags, 2 dim lavender bags, 4 pale lime bags.
mirrored teal bags contain 4 dull yellow bags, 2 faded black bags, 3 pale blue bags, 5 wavy coral bags.
plaid brown bags contain 4 posh chartreuse bags, 2 dark beige bags.
plaid tan bags contain 3 pale turquoise bags, 3 dark teal bags.
posh tan bags contain 2 faded yellow bags, 3 dim tomato bags, 1 dotted olive bag, 1 light violet bag.
plaid plum bags contain 5 muted yellow bags, 2 dim crimson bags.
plaid purple bags contain 2 posh magenta bags.
wavy gold bags contain 2 shiny teal bags, 2 mirrored lime bags.
striped tomato bags contain 5 shiny maroon bags, 3 mirrored lime bags.
vibrant lavender bags contain 1 bright turquoise bag.
muted violet bags contain 2 dull tomato bags, 4 mirrored lavender bags.
light crimson bags contain 4 drab violet bags.
bright crimson bags contain 3 drab silver bags.
muted purple bags contain 3 dim aqua bags.
posh lavender bags contain 4 mirrored magenta bags.
posh olive bags contain 2 bright salmon bags, 2 faded violet bags, 2 wavy indigo bags, 2 vibrant yellow bags.
muted aqua bags contain 4 bright red bags, 3 vibrant crimson bags, 3 dotted red bags.
shiny aqua bags contain 2 mirrored lavender bags.
bright yellow bags contain 2 muted gray bags, 4 plaid turquoise bags, 1 dull yellow bag, 5 wavy green bags.
light chartreuse bags contain 5 vibrant bronze bags, 5 posh magenta bags, 2 dotted salmon bags, 3 plaid red bags.
striped fuchsia bags contain 4 dull plum bags, 5 mirrored silver bags.
dull lavender bags contain 4 mirrored lavender bags, 2 plaid crimson bags, 4 dotted turquoise bags, 2 drab purple bags.
mirrored lime bags contain 2 pale lime bags, 4 light turquoise bags, 5 bright plum bags.
wavy turquoise bags contain 1 pale bronze bag.
pale magenta bags contain 2 dull teal bags, 2 muted red bags.
dotted plum bags contain 5 light red bags.
drab bronze bags contain 5 muted blue bags, 1 faded teal bag, 3 faded yellow bags.
plaid teal bags contain 4 wavy maroon bags, 5 pale brown bags.
plaid indigo bags contain 5 light olive bags, 4 clear salmon bags, 1 wavy lime bag, 4 drab black bags.
shiny blue bags contain 3 bright turquoise bags, 3 mirrored red bags, 1 pale brown bag, 2 dark violet bags.
striped turquoise bags contain 4 pale tomato bags, 1 light turquoise bag.
mirrored white bags contain 4 dim chartreuse bags.
dark fuchsia bags contain 2 dotted lavender bags, 5 pale gray bags, 5 light crimson bags, 5 shiny lavender bags.
posh blue bags contain 5 dark orange bags.
shiny tan bags contain 5 bright magenta bags, 2 clear beige bags, 1 pale lime bag.
dark lime bags contain 1 shiny magenta bag, 2 muted cyan bags.
bright magenta bags contain 3 clear blue bags, 3 wavy indigo bags.
dotted crimson bags contain 2 wavy turquoise bags.
dotted maroon bags contain 5 dark green bags, 1 striped lime bag, 1 dotted black bag, 5 striped beige bags.
dark brown bags contain 3 pale white bags.
vibrant coral bags contain 5 plaid olive bags, 5 dim maroon bags.
posh teal bags contain 5 shiny white bags.
plaid crimson bags contain 1 dark coral bag, 2 dotted beige bags, 1 dotted gray bag.
mirrored salmon bags contain 1 plaid lavender bag, 2 striped orange bags, 4 clear purple bags.
vibrant orange bags contain no other bags.
vibrant plum bags contain 1 pale red bag, 2 drab plum bags.
dim gray bags contain 5 dull salmon bags.
shiny maroon bags contain 3 dim plum bags, 4 pale black bags, 3 dark red bags, 4 light maroon bags.
muted tomato bags contain 1 pale bronze bag, 3 dim crimson bags, 3 striped beige bags, 3 muted yellow bags.
dotted white bags contain 5 striped red bags.
wavy plum bags contain 2 dull indigo bags, 3 plaid turquoise bags, 1 dull silver bag, 5 clear tan bags.
light violet bags contain 3 dim crimson bags, 2 drab brown bags.
muted salmon bags contain 2 clear yellow bags, 3 faded plum bags.
plaid turquoise bags contain 4 faded yellow bags.
pale bronze bags contain 2 dim plum bags, 1 posh maroon bag, 4 dim lavender bags.
clear chartreuse bags contain 1 clear salmon bag, 4 faded purple bags, 5 mirrored tan bags.
bright purple bags contain 5 clear salmon bags, 5 shiny red bags, 5 dotted aqua bags, 1 wavy plum bag.
faded gold bags contain 2 faded indigo bags.
striped brown bags contain 1 posh magenta bag, 2 dull olive bags, 3 dotted purple bags, 1 dark beige bag.
faded gray bags contain 3 shiny green bags.
wavy purple bags contain 2 dark beige bags, 2 dotted bronze bags.
striped olive bags contain 1 clear tan bag, 2 dim salmon bags, 2 dotted gold bags.
dull crimson bags contain 2 drab red bags.
dark plum bags contain 1 dark blue bag, 2 light yellow bags, 2 striped silver bags.
faded violet bags contain 4 dotted gray bags, 5 muted blue bags.
plaid black bags contain 2 posh aqua bags, 5 plaid orange bags.
light green bags contain 4 muted silver bags, 2 muted tomato bags, 3 mirrored teal bags."""
c ="""shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
print('Count :', find(b))
