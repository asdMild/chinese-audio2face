from pypinyin import pinyin, lazy_pinyin, Style
'''
shengmu_l = '玻坡摸佛得特讷勒哥科喝基欺希知吃诗日资雌思医屋'
yunmu_l = '飘啊呀蛙喔哟窝鹅耶约哀厓歪诶威熬腰欧忧安烟弯冤恩因温晕昂央汪鞥英翁轰雍思儿也居略虚训允姐'
shengmu_l = lazy_pinyin(shengmu_l, style=Style.INITIALS, strict=False)
yunmu_l = lazy_pinyin(yunmu_l, style=Style.FINALS, strict=False)
shengmu_l = list(set(shengmu_l))
yunmu_l = list(set(yunmu_l))
# print(shengmu_l)
# print(yunmu_l)
'''

shengmu_level = {0: ['b', 'p', 'm'],
                 1: ['f'],
                 2: ['d', 't', 'z', 'c', 's', 'n', 'l'],
                 3: ['zh', 'ch', 'sh', 'r'],
                 4: ['j', 'q', 'x'],
                 5: ['g', 'k', 'h'],
                 6: ['y', 'w'], }

yunmu_level = {0: ['ai', 'an', 'a', 'ang', 'uan', 'ia', 'ua', 'uai', 'ian', 'iang', 'van', 'uang'],
               1: ['ou', 'o', 'ao', 'iao', 'uo', 'iu'],
               2: ['e', 'er', 'en', 'eng', 've'],
               3: ['ei', 'ui'],
               4: ['i', 'in', 'ing', 'ie'],
               5: ['u', 'ong', 'iong'],
               6: ['v', 'un', 'vn'],}

shengmu2level = {}
yunmu2level = {}
for i, j in shengmu_level.items():
    for k in j:
        shengmu2level[k] = i
for i, j in yunmu_level.items():
    for k in j:
        yunmu2level[k] = i


all_code = ['b', 'p', 'm', 'f', 'd', 't', 'z', 'c', 's', 'n', 'l', 'zh', 'ch', 'sh',
            'r', 'j', 'q', 'x', 'g', 'k', 'h', 'y', 'w', 'ai', 'an', 'a', 'ang', 'uan',
            'ia', 'ua', 'uai', 'ian', 'iang', 'ou', 'o', 'ao', 'iao', 'uo',
            'e', 'er', 'en', 'eng', 've',
            'ei', 'i', 'in', 'ing', 'u', 'ong', 'iong', 'v', 'un', 'vn', 'van', 'ui', 'uang', 'ie', 'iu']

shengmu_similar = {'b': ['p', 'm'],  # 波
                   'f': [],  # 夫
                   'd': ['t', 'z', 'c', 's', 'n', 'l'],  # 的
                   'zh': ['ch', 'sh', 'r'],  # 知
                   'j': ['q', 'x'],  # 鸡
                   'g': ['k', 'h'],  # 鸽
                   'y': ['w'],  # 无
                   }

yunmu_similar = {'a': ['ai', 'an', 'ang', 'uan', 'ia', 'ua', 'uai', 'ian', 'iang', 'van', 'uang'],  # 啊
                 'ou': ['ao', 'o', 'iao', 'uo', 'iu'],  # 欧
                 'e': ['er', 'en', 'eng', 've'],  # 额
                 'ei': ['ui'],  # 诶
                 'i': ['in', 'ing', 'ie'],  # 一
                 'ong': ['u', 'iong'],  # 工
                 'v': ['un', 'vn'],  # 鱼
                 }

all_similar = {'b': [],  # 波
               'f': [],  # 夫
               'd': ['zh', 'j', 'g'],  # 的知鸡鸽
               'a': [],  # 啊
               'ou': [],  # 欧
               'e': ['ei'],  # 额诶
               'i': [],  # 一
               'v': ['y', 'ong'],  # 鱼无工
               }

bs2face_level_1 = {'b': '波',
                   'f': '夫',
                   'd': '的',
                   'zh': '知',
                   'j': '鸡',
                   'g': '鸽',
                   'y': '无',
                   'a': '啊',
                   'ou': '欧',
                   'e': '额',
                   'ei': '诶',
                   'i': '一',
                   'ong': '工',
                   'v': '鱼', }
bs2face_level_2 = {'b': '波',
                   'f': '夫',
                   'd': '知',
                   'a': '啊',
                   'ou': '欧',
                   'e': '额',
                   'i': '一',
                   'v': '鱼',
                   }

# child to parent dict
c_to_p_1 = {}
c_to_p_2 = {}
for i, j in shengmu_similar.items():
    for k in j:
        if k in c_to_p_1.keys():
            print('error: ', k)
        c_to_p_1[k] = i
for i, j in yunmu_similar.items():
    for k in j:
        if k in c_to_p_1.keys():
            print('error: ', k)
        c_to_p_1[k] = i
for i, j in all_similar.items():
    for k in j:
        if k in c_to_p_2.keys():
            print('error: ', k)
        c_to_p_2[k] = i


def check_parent(in_code, lazy=True):
    return_code = in_code
    if in_code in c_to_p_1.keys():
        return_code = c_to_p_1[in_code]
    if lazy:
        if return_code in c_to_p_2.keys():
            return_code = c_to_p_2[return_code]
    if return_code in all_code:
        return return_code
    return '-1' + return_code


def anaylise(shengmu, yunmu, d=2, lazy=True):
    sl = 100
    yl = 100
    if shengmu in shengmu2level.keys():
        sl = shengmu2level[shengmu]
    if yunmu in yunmu2level.keys():
        yl = yunmu2level[yunmu]
    if abs(sl-yl) > d:
        if sl > yl:
            return [check_parent(yunmu, lazy=lazy)]
        else:
            return [check_parent(shengmu, lazy=lazy)]
    else:
        return [check_parent(shengmu, lazy=lazy), check_parent(yunmu, lazy=lazy)]


# test data
try:
    if 1:
        pinyin_data = []
        pinyin_data_lazy = []
        data = '我在这里看到了你的姐姐晕倒在了鱼云之上'
        for i in data:
            py1 = lazy_pinyin(i, style=Style.INITIALS, strict=False)
            py2 = lazy_pinyin(i, style=Style.FINALS, strict=False)
            for p in range(len(py1)):
                if py1[p] in all_code or py2[p] in all_code:
                    pinyin_data_lazy += [anaylise(py1[p], py2[p])]
                    pinyin_data += [anaylise(py1[p], py2[p], lazy=False)]

        ay_lazy = []
        ay = []
        for i in pinyin_data_lazy:
            for j in i:
                if j in bs2face_level_2.keys():
                    ay_lazy.append(bs2face_level_2[j])
        for i in pinyin_data:
            for j in i:
                if j in bs2face_level_1.keys():
                    ay.append(bs2face_level_1[j])

        print('level 1 data:','-'*10)
        print(pinyin_data)
        print(ay)
        print('level 1 data:','-'*10)
        print('level 2 data:','-'*10)
        print(pinyin_data_lazy)
        print(ay_lazy)
        print('level 2 data:','-'*10)
        exit()
except:
    pass
