import math
import re

print('day6')


def find(s):
    l = s.split("\n\n")
    print('l: ', l)

    def getCount(egs):
        lG = len(egs.split('\n'));
        ns = re.sub(r"\W", "", egs)
        d = {}
        c = 0;
        for ch in ns:
            if ch not in d:
                d[ch] = 1;
                # c += 1;
            else:
                d[ch] += 1
        for eD in d:
            if d[eD] == lG:
                c += 1
        print('c:', c)
        return c;

    tc = 0;
    for egs in l:
        tc += getCount(egs)
    return tc;


a = """ymw
w
wm
vsw
wm

vs
lqn
ti
uvl

fryuv
pngtvuhfr
fcbrulv

pr
rp

tdvcspxnujak
vektaowjncs
ifybztmhlasqrjkgc

exvbqomlucjfi
cufeiomgvl
uolcfvmie
eoculrifnmv
fvclmdnoeiu

iyomzvhpdjtrw
rpnovdhwzmityj

emplyqxzfjrwb
xrezwjlsqpb
prdvzbhljqxaw

wtuolk
kwtluj

kixnqubme
adjgfwvl

lkzqupo
nsfhbc
rki

gkmqehib
ngiemuh

m
s
s
w

tu
arudi
gukp
u

hkfs
hpfjk

yzkuhrncx
dqasvifwne

x
x
x
x
x

zabmrcequtghsnlvdpkfij
drbelmtjasiupnhqgfvkc
hdvlprtebgamqfknijycsu
pcirvatkgmhndefulbqjs
hinfqkldbzcretsuvamjpg

eoc
omvqig
aglo

qgnjkcirewz
vmwhuafoxpt

zinoybesugqjhr
fzgeasrhynq
myzngtrwqvl

gdma
dq

haugzib
xeghuf

fsl
fsg
fs
fts
sf

bysucwlra
ucwylrbas
sbkuarlcwy

skmphtzonuydfxi
xpidmolthzywfusg
hxtysznfimdpou

gonabqykhrzmpsl
pyrblhznoswkgqam
pgbohakrqzslmny
ogbqmyprlnkahzs

hdcl
cdlh
hdcl
hldc
ldhc

fiwztpbcxreqodunljvyh
fsrmnugobhydpkc

fcloanbrm
dnkaglrxot
swvylepanjhqzoui

upali
kyilvspz
rlejqntbmoxi
iklfdw

tdxwaqsybovjgm
bmxjznqdt
ujtmehxqpldb
qbltpkrxjmd
qjxdzmbit

avnituwozrgcjmsd
rwsaocnugzjmdtv
zanrotwdusjgcvm

duqy
iu

rnatpelzuiv
eaizntulvr
fntbrilvaezu

vwprtg
nfrwluaodtphg
gtrszpw
writqgmp

ayxievonwmtchp
aytxowvcpmihe
xtehvomypcwifa
hwmoytcvipjxae
yvawtmeiocxfhp

dnrpaivezcktfwy
vdpnyfzrmcktwi
icfnyrtpzdkwv

gejt
getj
ejgto
jtge

btmwidzrun
mtunzdrbi
oiebudtxkrmyz
ztmbdrui
dmzbrtui

rasxhidbgw
klxwvhbeacidsg
dhxlacgusirbn
sqabjmhtifxodg

utpkgqjiycexosvanwl
grjfvnbuscwadmihxzk

ktnhpvqxzfuwosmgl
fwxmtvzohnrlkgsup
hvlzfroxucmgpksnt
pslyfovbigtukzxnmh

zde
zed
zed

v
v

calfotjxbg
etagbc
brackuvtzpgi
mdhapbtygcv

hkdb
eahrxg
pohs
hujbq
dchbt

nw
ewgr
amyh
pquwn

o
o
o
o
ou

oakzcxnp
xoclan
oxazcknp
hwcomfxna

iymzjovgkdrqpalehubc
ptcgyqhrboazuv
vxyohunafqcswzgprb

azwb
zabw
bzaw
zabw

zu
zxi
fldo
u
p

ejhtlbm
etblhm
mtbelh
hbltme
thbelm

tnqxahufm
bhftnxumaq
ufbahtqnxm
amnhfxtuq
qfxumwanht

vgdtjm
tdga

wkzbx
tksxbwz

niasv
cirenka

pvbjswzixkcug
bxvjwsiugck
xcwjbkisugv
bgikucvdsjxlw
aswuxibjgcpvk

vrjcpfuhetkd
mjbhzwctpeyk
qhwepmtljksc

mkdb
bkmd
omkdb
kmdub
dmkb

tmharzskfycvnio
abdmulpwjyxeqgc

skmacnpgzho
ghsnpaczkmo
haposzmgnkc

mrngvewdsqca
tfjyqhkxes

ampi
m
mt

kcduvyaqgtpfmij
vxgfiqcdlajypuk
gcyoeufqkpdijmav
cvfuqpiyeadjkg

tblyemri
teburlymi
tneidylbrmfc

jtmkxgehipfuasqrbwvcdyn
azwkvfhsbynrjpgmutdcqex
uobjpcgzstharyvkxefmnwdq

etgikbzjd
zdybhkwteqig
ouitdbrfgeznvkxs
bekipadqgtzlc

v
ale
c
h

neqvowybzx
nybezqwxvo
zbenxwvoyq
vqbxwznyeo

kwdm
k

eahrozxdj
aopndezjx
emjaonxyzd
jxeaufdosz
yaoedxjz

hzwc
s

bnemwzv
mbzwnve
envbamzw
ebnwmvz
ezvntwbm

djkqnrcvpseohazmflb
jyzftduhbnparmlscqovk
zksbneljmxcfdprwaovgqh

zxfgtveb
xfbetvgz
txevgfbz
tfxbvegz

mfcr
cfmr
mfcr
frmc
rfcm

qsdvzyixl
zvdlqy
znydvqlku
lvndzyq

vpok
hoyb

lucohageisvdtfqnbrxk
naekdgslcqoftxrhbvui
oxgrunehtafkbidqclvs
vrdsfanugtihkxqlcobe

poayngfzwb
mzyi
clxuesdvqythrjk

vtsxloimpq
sqvxulbiomtp

xlo
xol
lox
lxo
lox

mqtafugsj
wahiptqjbe

nuosc
usocn
cnuso
socaun

rwchjlkmidbtxupfvg
jkudgvprhalcfbnymtw

uptazbcdxywqf
buqywadtfhcx
klbduawtqyx

klfyrxdzn
lsnrcyvzokhx
eafrzqkxly
xzlqryk
xwriykmljzugp

gfvxdi
vtwigxdj
xdnvgyi

vs
sepvngak
vs

dqzfx
xqdfz
qfdzx
qxzfd

lfdksujt
ijcdtslkf

rxqevdwishmjfluy
lwshvauecgrfiqxyjm
txisrubqelyfwvmhj

ijlvuenzdsykfwc
qkxacuydnehzbglsrfm

purkflqgovscyedzhtinxa
ensuvzrftpdgcxykhqilo

f
p
jkxa
p

rwqcyxtbvn
rtbwcxqnyv
ytwvnbxqrc
vwxcrqtnyb

takohlgzesf
katgsozeflh
aolgtesfhkz

jakvrlxipqgwn
xwjhigvkqarlpn
vrlitwjqcagnkxp
ngcljqvpkrwiax

csg
sgc
sgc
gsc
sgc

xftrpzkynwjcils
tyzjfncspxwilrk
clxjtnsriykzpwf
rcflzkwpxjynsti
ntwxsapejzkcrilfy

gmabr
mrbag

idrvzjbafosemw
fvewdrjazsmibo
woisjrtdvxezkabmuf
aifmbdjowzvres
jzesabwvmdiofr

cvsr
scvr
srvc
zcrsv
rscv

ldjs
sdjl
sdjgl
ldjs
jlds

vf
vf
vf
vf

nqi
gmiywb
il

bsvamr
qkvrab
abrqv
ktabvhr
rvbhax

cpgsqnorkay
yproncgkqsa
okapcgqsnyr

fhcrk
wjaxbchs
flunch
khorczi

uyj
jyau
yuj
yju
ykjiu

yuqwkzf
jaocfzyxpw

ayqun
vwpzfoj

ftkx
nftjkr

saupfiylrhckzdmq
idwlp
ldip
wlidjp

qhiu
suqni
iuxnq
qui
iumqzg

xvoqnda
dloqvnxa
donvqax
vqdnoax

ctblovfpygsmwqrjai
ivfwqgrpsjtacm
pmvqtjfragcwis

m
ms
m
m

v
vxcjl
tvgn

agcvutldfnwpoqhe
panwfvugetxqo
tusfwgmoaeyvnjkpq
wvutgfoeraqmzpn

pfelnjvha
qmzexonlv
rbyiugdswk

spmzxl
nhbuvqcagdi

vpfmjgitk
vefgrdkpit
gfitvkbp
pftjvgik

eiczmbkfargtosjdlyhwuxqn
uiqdwkptonjzxlfsrgemahycb
mnfzskoytqlbhuidjagwexrc

ylcroxz
azolxycr
rcxoylz

ipjvbtacrsuklozxqg
gkczovaibqptulxsjr
zsuctpolbxjikqrgva
aglbcjqsvzxokrupti
tlpurqvxgazoibjsck

chjtiyplzb
rzcplthisq
lcwgmnzvhei

uvbqnetmkdsg
tcgizb

anet
tnea

b
lbm
b
b

rjsgkvxnoctybf
onhbkjryzvtcfag
rvtbyfgxsonkjc
fcgoktjnbryv
cvgpjdnyrotfixbk

woyzins
vml
l
ekh

imurfjexb
iufxme
midneuxf
ztudmxife
kymfxieuod

fjevlykwshit
jfpwistkglev
ljidewskvtf
orqwblzsevtcikjfu
xayemltwksfjivn

jmfbqzsu
jsxbiumfv

kuytgfqzwolpxdcnjhrsme
xwzjpqsgfmdklhytocuren

tswk
ztqw
mdrpthif
t
tw

rnskdcauhe
rukeyndhasc
ahsrknuecd

mxsaerbdhgqcy
xvqybdmahreos
qyxbmgjsradhe
bqxheasyirmd
rdqehysabmx

bkzxw
xzkwb
xkwbz
wxjzkb
bwzxk

avlwfyqrp
jkozmedhgubsxnct

ie
gkec
epx

xvbisfp
zxprafsim
pwiqhkfucsx
sflxmjbivyp

mkhg
dpnflvzhesrt
bmhu

mpl
pml
pml
pml
pml

hdrtnziabqscwxp
btdczqxhuwranspi
prwatsxhzbdnicq
hxrnzawpcsqbitd

gxzafpjvciywskn
wnzvjifscrxykapog
ncsjiapyzkgvxwf
jkexzingwpvscayf
iyjzfwnckavpxsg

xtdblwyqfsjak
uwtsncvjlm
switjlm

j
je

ce
c
cy

semxdiqw
lbnmaq

n
n
n
n

rq
rqes
qr
rq
qr

ibndxgtuawhokzc
wkxhgdcznjtoaiubp
uxzwtdnblapkchogi
zhtidxwvecobkgyuna
cgabuhrpioxkwdztn

ekcrfujsopgvbwxtya
jeykusfvpxbowacrztg
frkjsygapcowxubetv
shjoyanumqkertxgbdfwpvc

mfw
pfwm
mwfi

ocyhq
chqye

nzsxagpfuhmqkcy
flyqunphxm
qmpnhxufy
mjurwfpqhnyxe

pxqf
pqx
xpq
qgpx

bzhprgot
rzhpaoug
rmhygacqxvkpjzo

tlzpvdgkafqw
clqvpgtkafd
lgetfbksxivdprqah
kuptalqgjfdnv

rfkwoalbjdi
bkilwjfro
orwjlkibf
okbdflrjiaw
nrwjzoibflk

n
n
n
n

vznusdgkmcrxfpwojtleqhy
rveftohngkxzdljq
lefikohvbxqrjtdzng
xqtnjzvdglfkrheao

xohambwtulqnpgf
ruxmopbjwtfncdgal
bnsptuwyvlmxzogif

azbsgpwihlcfmuk
ahfgulbckzsm
gslafkcombuzhj
hujmklzgbafcs

nzdqthy
wjeagzcxyiq
qzfycp

hudclx
quczdxhl
chudlx
hlcxdu

nrmypdbzvolxga
ykgtvfcasz
yagwvqze
zfvygja
iyzgauvht

eitov
aizw
qjai

ruptmgzobxa
hjvsdwylieqnkf

njsgbwltpyeohf
gxsojntpyfwlehb
fontbepsjwgyh
mdfhypjeobsriktqanwug

pcunvqdgxjfzokwm
awighqdejvnflp
iqdnvfpjwlgs

upqz
zhyxjdtlv

nq
qpns
nqfu
qnps

lve
pi
ipf

uafxbjp
lfpjcw
rjfp

obh
h
h
h
h

ezx
xze
xze
efxz
zxe

yshdxqelnzmuipowr
oqsedljrinmytwuphx
ljnbcirxshyouqdzewp
wbiqxtrducehoylspn
rvshygoewlqunidpxfak

e
e
e
e

hyuwjlgxoa
chajowynxlf
wyfhlnjaox
aztohyxlwj

eqldmuxigyhktfwbczapnrvjso
vpxflgohmqijwadnbykrecustz
kswxetzualphigncdoqjmfrybv
znilqdpkgratwjvuybxhemfocs
izjbnyvastgdchfeoxmrwqpklu

qwjzem
ewzmcqj
cqzwejm
mwqejz
qbmkjdzew

rvuoscwqldtnjfpyk
dstluofwkrqcjnyp
ujnytlcqwsdaokprf

cbhwotxiglrm
iwlhgcbtrom
ibvrotmjscgwh
gkcltbmrhoxwi
tzrgowmcbihx

dc
cd
cd
dc
cd

pnsjqghf
ntqjfhgp
nfphezrjmgv

gotlaypnhj
ylonphtgja
gahjotynlp
lpajtyonhg
lynopgtajh

uqkwycrbd
dubvkqrcywm
uqdkybcrw

hvwialzjfqecpukxdobr
fhkeaczluqwbpvrxdoji
qkabjohpwcurvxlidezf

zjrqhwbkcdv
cvxjhbqkpwdz
omdzlwkbqgcajhv
rjcvqwzhtdkbp

olmvrwtagfuyjbzi
mfrtbuvjizaylgow
vafmjgyubzliorwt
orbmjpvigztwafuyl

rgmodkbs
mogs
suogdrm
togm
mogv

hf
fha
tfh

bcazwpirygekfoxjdtnlmuqhvs
fzkrwyuslvmajxqdienot

xdanjtygfrwhkzblpq
jamxfwzklchngrby
hyvlbzfjrwkonga

shaxbk
rztkmls
nwjvucedk
okt

rpvukdoaqfywlciehjnt
qxwhtregcnilvapskuodf
ltacrhfwquvnizkdjpoey
vtqekcpnwauflhiord
hvqlkurptfaiwnemodc

huqwrpfsilxotcazvygdnj
navdfwistcpzljgruqxoyh
lhdipqtczywaxunbfojvrsg
wotlyvzfjdqgcuarhnxpsi
qfgyonxuzavspjrdhlciwt

qdzjxfhpnmbwtuskyceg
sxyaqfwcjehkprodzvg
iykjhqscdzfpwxoevg
qsveyhjxczwgdolfkp

jf
xn
gpw
k
n

nc
c
c

iyfavqodmwgzspceblxuhk
favzwqtgkyspuixdcbhr

hdcazlv
wtqbg
seu
krbju

myldhzr
wutkednmhla
yidhlvcmr
omhrdgfqblpc
jlsmdxh

omnhyavdercx
qzncxyamro
wmxynozpbauric
kcnwomxyrba
pnocxymrka

bj
ybjk
bj

lgqkmsndwhx
knxsqdmhlgw
msxdqwnghlk
nyxcmgwkseqhldtv

th
qzxyw
a
m
ohu

sujpydikhnv
vnjyhuitksp
ajenhpviskuy

gnjvqlwfxor
fithnsacxjbkmez

rf
uwklarfc
xrf
vrfd
fjr

gtoxeicdfqm
gtiqmeochpdx
tedlycbxqmigao

muxsonhgp
yudpsohm
shpmou
rmpohus
ojmhups

cjsgzxr
axclosqg
cgxs
cgxsj
ixscg

v
v
srgbv
vo

doaphkmvec
adrwme
wytmaesdbun
ieqgzdxfjyam

lcgmfa
agflc
alcfg
faolgk

i
ibe

jemfp
mp
pms
mp

u
u
rda
u

hzdl
xrgdz
vjfgdzr
zknswaeuidcmq
zd

rjwpoqyvzcxektf
xqzwjvetofrcypk
exwjyovkrfzqpct
zctewjxlnorpqakfvy
otxcrkyqfpjewzv

vyhnmjlgekxobps
prgbyltswioquvfmzex

q
feq
dqwx
q
q

i
vbytcon
zksragjq
xdf

lqtzbjudwhm
etgyxpcvarsnko

dupshvrnafz
zafnhrpvodus
vzpsufdnrhxa

ylkzmodvqg
dgmvzqkloy
qkvzgdloym
glqomyzvdk
mldgqkyvoz

v
o
v

actqvguieyrf
uvzgaryipqtl
hrlixgyvatu
dsjokyumvirgwt

q
q

xqln
lqxnu
xqn
oqxvns

i
i
xi
i

cxtnd
dtxcn
vxctdn

vspoaczketurxdwj
vkjlrwznespouxfcadtg
pwsrxvedktacojzu

qdis
sud
dnsquvf
bexgrdsj

mfjcevsywhnuplxiqrzba
ibxrpeunqhzscyfljwmv
yjbqzixfvsupcrhwlenm

wpvmzkhb
zbvkhpwm
mbhyizvwakp

bqfzaeoig
fbzixgaoq
foqizgb
dkibvjquszgofy
ogbfizq

wnz
nwz
nzw

vthxfdk
hfdkgt
vsfdthxkq

uzr
rltz
krfqz

aoshypdlikqfutvebgjnz
qgtdkobisc
rotbdmcwgskqxi

trbziwe
qlmuxkbyngrt

nuqdyjmg
nmgqydu
uqmyicgwnvld

phmc
pd
pd

slj
usqjl

q
q
q
q

zsryajnihfexcguvltk
zvhcanygretxiuk
izcquegtyhxvnakr
nrixgcuaevtyhzk
aeckhzgyqxnvtrui

bkyhnwitqoflxuz
oqhzbntkuwyxfa
hxbywtkqnzouf
qwgkxntozihyubf
nxkzusfeocbtqwy

xwloszbpcatn
pwzblgtanoc
abcngtwlozp
lfzabtnwpoc

paof
paof
aokpf

yermvpgouhilaxtsf
hiuapfsmvergxl
ulemxsipgvhfar
gfimvphualerxs
pusxveifrmglha

qwzfjcbxvhaedmu
hczufqwejvmabdx
bvumhayeoxcqdfzjw
awhvdxnfcqzebjmu
xcfwaqubhdzmjve

p
u

pabrkst
kptxsb
nofjptbglks

pwxtihaoryfqjcmk
yrzwjqiokaevmx
ypmdqrkgxubljownai

wrezth
nbvma

cxz
xzc

botydczsvwgikrfa
otkfryqwmgnacisubzxd
zfcdkyaosrbtvigw

rpestzqxokcb
qrxgimauceftnzkbhdsjw

msuerxvhajnckb
rcahunbemkljsx
cgmsvxrhjbkuna
zxabprinwjmcshku
rucajnktbmxsh

infwrgjphdvokebsqzy
eahcnxpljksfqbwdum
ktdpefljwqnabhs

oilcxdjheuyprna
cpydlhaorjxuie
jzairyhpcouxeldn
hucoibrejxyldap

jbiglmtowxvkdch
ygmjiwtdlohcxkv
cwtfxlhkmsgnvojid
rakpdiolcvxegjtmhwz
chojlykxmvtgiudw

vnqoimutgcwyhx
iwqnecovmyg
dsgmiqeyocwnv

wzjtrynsfqkga
awxkqtnjozdruyg
yngqeajwtzkr

jrg
jgx
jg
gj
gj

ryaxghznduqmkve
kxnrfzbye
nzysjlbriexk
rzfxjclenykpw
teyzrkxwno

mhlaqj
luajh
jhla
jalh

rdbvoqszekg
ekltghbudosivqarz
qkbgsreovzd

r
r
r

il
io
ix
i

nkyrthauqjb
jyktnabhrgq

rkjnluewc
ybgmizxto
efwlprvc

ga
a
a
w
a

goexmwfchknjbliap
hbxcklgnfipajwmot

nwzgbjo
njwyclbsk
nhqjirbwv
fwvbnrjo
wjbnud

thlemzwakn
taylrneqzmh
exsovpcnzitmfua
aetmjzn

hcozjrtsx
sxrczhtoq
ohxgzirsct

yojqc
ocqy
oqycd
aycqo
doqcy

jvuigo
zvujgx

isolkxcghzvfpajdeuyrb
hutcjnmxgyqvrkeow

rocqg
g
gcsx
gile
ngu

jwhoelbgiscfzakmx
wtxkmcoslzigjebafh
fzshoicblxgkemwaj

mubtlkhjspeynw
lkstuweyjmbhnp

tdpy
dypt

set
ts
stol
ts

tfisjzu
tusfzji
fusjizt
szfitju

cwlvjiuqkgom
twedofxgvynjqa

jhuwldvt
twhd
trwdh

mzlqyv
gzydvqm
mejzytqvb
qmybzv

qsdpagrf
ybfuikxm
fjdprszch
jdzcofn

cuemfrdviynwko
ucisbdwftjyxh

wim
wi
wi
wi

velqabhypocmxjs
ckvqlnybrughtmapwdzs

fleghjbtvqrzdpy
njfzrpqyhbkvdlwet
lefdyjvxrhtbqpz

n
qn
dpn

hsdxgiartqfczkmeoy
dmothqjezsfyikgx
wsgndtmezoyikqhfx
dfsxqpotemigyknzh

dhirx
jxbltqdrf
rxnzdyw
xyrdw

gztrajypuesxmonwlhdbf
opjvelthnqxgfkbdsayrzmwu

dsqzkpj
kspqjdyz
qszdpljkm
zjpqksdn

bdvmoeinsw
ldvma
pcytgzqrhufxmjk

qtvdacproxhyfeig
iqevdchgxtypfr
iqyedcpgxfrvht

tnkvcfobej
jicwsrbxeamy

rvqnbulwdgocf
kxgoulzs
mlugyok
kuehijpagtlo

pnayvm
vmpany
mpvnya
ymapvn
manvpy

juandk
bqamunz
cnuxt
oshgeinw
nur

artidpmywzx
bowqmgenkcruj

ymbgfnv
mynvbfgl
bmfyng
mnfgbiy
nfymgb

yc
x
y
ksfv
o

t
gmq
lhrx
zfvb

rzaokythm
madgkjqyhltz
thaozykm

jlecfkhazwyqtrsgn
clrwndzstjfqkgeamh
zenxwahslptgrfcjkq

lhn
qztv
yp

gv
xqg
cwpierytzuh

u
tvfy
uo
j

ywofspubhrgjmcilekv
skejhiorglvbyufw
arezwfukjbgysvhlio

xpnldkub
wkdnqupx
gkyjduxon

qubrihmgokzjclvytdfaw
brueisfpazonxcqk

mykiwzenjtblqasdoux
njuxkbytmwleqridzspa
aubkqjmyinslwdxzte

kjdn
ts
xw
sypu
c

iumldrvwogjbs
ujwsemlrvdibgo

zlknvwbhy
nzms
nitsz
rnzm

ngde
lge
buatigrcvz
xewgy
jlopdg

xjnythqakgsruicbld
ezfwpmov

es
se
nsaer
sxcwplje
gems

r
s
r
r

enkqydmrgjvsbhau
hmbgservnjkuyd
dherisgymjvbunk
beyvnhjxgumsrikd

a
aex
oa
oa

ibedyc
ondfctsjy
cdykvga
ywacdbvuq

mlowux
wqplxc
lhxkwp
pwxl
lxws

truzalwqfpcinjoh
baxwplhjrzvgfynqoic

fdbshvkcm
dcgzskfwb
iadczkfb
ydfrqcobk

gpisnoletr
symv
qhmfws

bjfm
ml
mvcd
mv

levr
v
qv
vq
v

j
j
j

uepmnys
ymgphe

bvlrqpgj
qbvgrpmlj
vpjgrlqcb

fmsuteojyqchwrdv
rdyefmqoschwj

cnudzpksyvbeoxrijqa
iuokqscnjyvpzedarxb
sxijkqybuoavpdrzcen
zckabxsoerjduvpqiyn

qdwinxo
cxabnqgmiwo
ienqflorpxy

tsbxdevwi
evbtwidx
vbextiwd
dvtwixeb

pedufvxjgarqzwy
zvgpfyqrtu
lfzybuscgmvonpr

pgmqjt
ulaib

jefg
vb

ltqevp
grik
qelv

jh
xh
h

diaukxtvohzwnbecsgjr
znyrixahutkgbsopvewjcd
zxsbcivunhqojegrtfakwd
dwuzeagjhtcvrbnikoxs

qnasfbreph
bpka
lpbao
paylb

flmoxzuakb
dhtnicpys

vsnxozukyfqmj
ritpgwelahdbc

ndripfaw
fry
rf
rfy
rf

dqpouiscz
dfouc
wocdlmuneb

coiwvtezuf
tvzofcwui
cfoiwutvz
uvtocwfiz
ntvuoczifpw

aycwonkebidt
vbekioyctad
ckmafdbiyroet

bne
ben
ebny
nheb

bcnvuf
fvubqnc
fuvnbc
bcevnuf

catnl
anclt
catnl
tngcal
nlzcato

pcohyrgfwitkjzxa
pswmtxigkzhlrjafy
rfahwkxzgtjynspi
vhfgpjtinwxakyzr
jebyraqiwfzkgtuhxdp

ifzpyvnrxscqmealb
ypnrofazxsbelqvmci
mzxfpgroayqnbscvlie
cesyrfqvixkbhznpalm
pqsenbmxzrfyvidcal

zyrnivgqhjxsopftadmk
humogbldxfecrpqjwa

lgwkuxemhaifprosq
rgfsxaiwuqhkpmeol
axgfepmsukroliqhw
aiwqlusgfokmehxrp

wmanq
owqpagm
abctmxq

azsnmugchqfv
cqvsmfzebuhagn
qlwafvnxusgmczihd
ekzfcusqhypangvm

jdfau
ufa
auf
ufna
fua

jrvyckoizf
bmka

rvmoylsthqca
ohsriqxyaczt

gkajpilzfeodcunwsvbrhmqtyx
jdqgenacxzrhotlwbvumfkpyis

xewygnkia
xyinagekw
nkayewgix
anyxegkiw

qlykxzcthnprfbej
rlckniyjtzpqbefxh
cxgbtephmkryzjfswqln
hpjtfkcebzyvxlrdnq
ftkyrxblchneqpijz

p
b

vc
t
t
t

vagutfpbqhielzn
bpnligtvqhaefuz
fpevuihnqbatlzg
efvzlhigupqabtn
lufiztepnqghabv

rfbsmiknjogvhyq
mqpikvjrtfonycsbdh
svyfkbhnpmiqrojz
whnsijavbuyqkrfom
kiyjxoqvblmhfrsn

gaxwn
pgmeaw
bfxagw
gwlsa
gkawyc

cxqozuawvliptyjhfs
ahvuqityolspfjwzxc
xifpthoyclaqzvsjwu

syfbj
ysjfeb
fsbj
jbgsfwk

rquip
pjiq
pqi
piq
dqpfikv

p
kiwh
z
fyvmrc

yh
hygs
haye

uqxvaojkbw
jqawxuokvb
vuxbqkjawo

pvzba
bymav
xbyavn
abv

nfasjxqwrgimztvcludob
ldsxumwtircqvzbynofjga
uchrlvstdmixzkjanqgowbf

xbsdla
hupjrknzficy
tveoa

cafoqgjdemsnk
fjivltcdmg
fgdwphcumjb
vyfxjcrgzmid

orciqajldy
ohdqiylacm

y
y
yu
y

li
ilh

lta
avle

wnkha
awnkh
nahw
vhanlwd

cfmurandsiexvwq
vzidurtyboemj

gosh
hoesg
hgotel
gobhj

wransfipukq
riflauznhqbpt
rtvaiunfqocpl

vdajgmsqrpefytzil
txdrisplvafzujk

elwgstkh

epwji
jpfe
hmsryxap

za
abokz
tazefsl
apz
zbar

wxtufcbpdlesrzkvhgmnyjaqo
oeflsvhjwmrznckxdaqgytu

wxydrbvmokunatqpe
xoeawvpqtdbmskrun
ovwxrkuqatdpenbm
wreubavpxmtqdnko
xwpkontbvueaqdrm

npjrtougxm
ptojgmrnx
ngmxpjtfr
jgzxmtrnkp

c
sc
jg

vszrmkhqjpgayc
otswxfuibdl

snwpgtufhaqoxberyjmkdi
tsmbkenrfdujayhwpogqi
fkgsmebvjyanocwurhdqzi

w
s
w
w
ciy

ydxstgncopql
umfrvjawnekibhz

xjw
jwx
xwj
jwx
wjx

kwgxylvafh
fyvhxklawg
klhygafwv
wyfktslgahv
wkxlmyahfgv

git
igt
gti
otgi
git

vnih
vionh
invh

pstycrxzeg
yrcgtzpe
ctpzyrgs
tkyvpcbgzmri
gzpytrc

hvlq
hzj
hz

knrgyxumlio
dyirljutgnv
zagpinwuyhr

mzlvrsgpid
pftrocn
awqprfnhux

wvlpjegodb
dvbegwjpol
lzdwjkfgpobveth

slwmnda
swmdl
sqwdlm

iahz
hzai
iazh
izha

ozaq
zoq
zweqo
zoq

a
qo

vbylpk
gferiaouxwntc
qjk
hqmks

kmtqnhjuorx
gjmutoxqdnr
uomnjxqt
omvpxuytqnj

mdjgyzhnrbqlkixwup
umbnjkwsdolhizgrqpx

estfmkocwlzua
wertfzuslakm
zsxntkfewylm

ewozvybutrlc
pcmtlz
ctflzx
zsamtckl

rcnabkwmljygzdhpos
rpadmzhwgbolknsycj
ojhgrczpwsymklbdan
hmrwybldcskaojgznp

vuyj
rjuy
ugyvjz

gtbvkoi
otkbvg

wzmshqxk
uafswryemj
cvhskzwm
xwohmgqzcs

fezyavinmdjxwqthp
uhmydqjoewfzaxt

ytobegs
rebynogpaw
cgyboueh

hqmen
okqwimt

n
n
n
n
n

mtgye
mezq

njpgvcwbxzqhauds
nghbqsjawpvuxdzc
zsqdahuxwpvbgnjc
vhdaqbspzwgnucxj

sfebtowpijhcl
xtokqyecmwphlid
urtighewvpoza
tbpofwinehd

xmlctywhong
rliwocgutxaeyvn
ptydglnfjzxbso
nogqtlxmywauvh

rjecz
aehocvg
pyufxqbmsltw

wquytmaroexfgzkclvb
umtzxhavjsqgwrckpb

cgvbhlyxtifkzsewjru
rhsftpjgmwabzlcvqkuxone

ndgizukav
zuinkavdg
udzgkvai
wgudikvza

kfvpnot
nvpotkf
ktpvfon
pokfnvt
vfoktpn

kqrd
rdkq
krqd
vfrqkd
qkdr

zyqijxlfdu
zdjfixyq
zihxyfjdq
xoyikqjdbfezg

rq
qur

bozhntm
oeprf

ltx
ij
s
fyvhcdqkm

cqivpm
vmcpqi

ntb
tbfn
nbt
pbtn
cbnpt

a
b
yexo
f
t

tqfazuimjbxgsvedkp
exczvifmsqwakpjtbug
xijzfqcgsvkbpteamy
esorqhmlpnbaijvtgzfxk
evsjiztqmpafgxkb

vhljf
iknboam

kg
jbovgtl
g
gw
iugx

j
j
j
j
j

omsul
ucsim

zykn
aisxbtez
lmzc
zl

a
a
c
a

pkso
noku

rpo
opr

jh
j
j

akqpzhoyrjwitlcxvbdume
mwyrjqzavueokiphxlbtc
yxbrckaepwiomvzqltuhj
voithcspxmwlkyaujbeqrz

naqe
efnq
qne
qenk

chwluymniztgrxafdb
tghnclypeiufsbkwrxam
iynhrfluwgcmadtobx

icgwkoretxmyuzaljdvq
qxgfkuicowleaszyvrdmj
gukrvdczaqojyliewmx
rzosixlycukgdmwejavq
qmuleoaygkrjdicxvzw

erqbuao
peoaiqnf
axoqegwm

ikaydnx
ykja
yksae

jmwfaqxrztivlknscghbu
zkruqhclxainsgtjvfm

mykilgzq
gqzmlki
kwlbiqrzpdgsxj
mgqkuaiznl
cloikfzgyuq

euba
auewb
leabfu

zoqb
boqz
obzq
qbzo
ozqb

lrjvtqf
jrzqltvfha
tlqfjrv

xosvzaq
qsoa
atqso
asolq
aoqs

ckilsdrut
ldrsjtgenqiu

etvizsnywkjobh
jskwoevzltyibnqh

ctkpmiyohjgbuldarn
hoyfbkvdt
zwthxsoykbd

dciagsvnmzyruephk
aslrwitjvenxgcd
vebdqnarctisgl

nlzs
zobwxsln
zsnl
rsiucynlz

gziwqfy
lodmh
knarujextpscbv

uhmobwlgj
obhmwugl
hmabwuglo
oawblgumh
owlbughm

ucsfwbizqdenro
npsrtkmeobfdg

rvhcidqaysukjxbpgzoe
vauhokjrsybiqcdepzgx
cjibvqsxzoyrkeufphagd
cyzpukrhxdsebogajqvi

zcojuprtbhg
pdwbauchjtsgkn
gprtulcfhjyba
xbecghvmjtpiu

qclaiywnujprxdotf
fiuqtwlxocrnayjdp
wdfoacnjipyqtluxr
ejdyblqnihcftpwroavux
nqiayfgucrdjlwxopt

xhzrepycnwsm
iaxfykeblwp

eaqkisdgcojhzw
ckhbasd
ckdhpasb
hcpydabks
sckdha

kn
nk
nuk"""
b = """abc

a
b
c

ab
ac

a
a
a
a

b"""
print('Max seat:', find(a))
