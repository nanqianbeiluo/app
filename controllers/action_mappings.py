ACTION_MAPPING = {
    ## 清零
    '0':                 {'write_address': 600, 'status_address': 700, 'command_value': 0},
    ## 耗材准备
    '多孔板转移':          {'write_address': 600, 'status_address': 700, 'command_value': 1},
    '盒装移液头转移':       {'write_address': 600, 'status_address': 700, 'command_value': 2},
    '盒装移液头上盖转移':    {'write_address': 600, 'status_address': 700, 'command_value': 3},
    '增菌管治具转移':       [{'write_address': 601, 'status_address': 601, 'command_value': 1},
                         {'write_address': 600, 'status_address': 700, 'command_value': 4}],
    '培养皿治具转移-高':    [{'write_address': 601, 'status_address': 601, 'command_value': 1},
                         {'write_address': 600, 'status_address': 700, 'command_value': 5},],
    '培养皿治具转移-低':    [{'write_address': 601, 'status_address': 601, 'command_value': 2},
                         {'write_address': 600, 'status_address': 700, 'command_value': 6},],
    '培养皿治具高库到AGV区': {'write_address': 600, 'status_address': 700, 'command_value': 7},
    '培养皿治具低库到AGV区': {'write_address': 600, 'status_address': 700, 'command_value': 41},
    ## 末端快换
    '机械臂快换释放':       {'write_address': 600, 'status_address': 700, 'command_value': 8},
    '安装样品管夹爪':       {'write_address': 600, 'status_address': 700, 'command_value': 9},
    '安装研磨机压盖夹爪':    {'write_address': 600, 'status_address': 700, 'command_value': 10},
    '安装样品治具夹爪':     {'write_address': 600, 'status_address': 700, 'command_value': 11},
    '安装培养皿夹爪':       {'write_address': 600, 'status_address': 700, 'command_value': 12},
    '安装涂布作业工具':     {'write_address': 600, 'status_address': 700, 'command_value': 13},
    ## 样品准备
    '取样品管扫码':        [{'write_address': 602, 'status_address': 703, 'command_value': 1},
                         {'write_address': 600, 'status_address': 700, 'command_value': 14}],
    '样品管转移':          {'write_address': 600, 'status_address': 700, 'command_value': 15},
    '研磨机顶盖打开':       {'write_address': 600, 'status_address': 700, 'command_value': 16},
    '样品管放入研磨机_1':    [{'write_address': 602, 'status_address': 602, 'command_value': 1},
                         {'write_address': 600, 'status_address': 700, 'command_value': 17}],
    '样品管放入研磨机_2':    [{'write_address': 602, 'status_address': 602, 'command_value': 2},
                         {'write_address': 600, 'status_address': 700, 'command_value': 17}],
    '样品管放入研磨机_3':    [{'write_address': 602, 'status_address': 602, 'command_value': 3},
                         {'write_address': 600, 'status_address': 700, 'command_value': 17}],
    '装研磨压盖':          {'write_address': 600, 'status_address': 700, 'command_value': 18},
    '研磨机顶盖关闭':       {'write_address': 600, 'status_address': 700, 'command_value': 19},
    '取研磨压盖':          {'write_address': 600, 'status_address': 700, 'command_value': 20},
    '放入涡旋振荡':        {'write_address': 600, 'status_address': 700, 'command_value': 21},
    '涡旋振荡放入离心机':   {'write_address': 600, 'status_address': 700, 'command_value': 22},
    '移走离心机盖':        {'write_address': 600, 'status_address': 700, 'command_value': 23},
    '样品管研磨to离心机':   {'write_address': 600, 'status_address': 700, 'command_value': 24},
    '装回离心机盖':        {'write_address': 600, 'status_address': 700, 'command_value': 25},
    '样品管离心放回':       {'write_address': 600, 'status_address': 700, 'command_value': 26},
    ## 菌种保藏
    '取增菌液管(全新管)':   {'write_address': 600, 'status_address': 700, 'command_value': 27},
    '增菌液管转移':        {'write_address': 600, 'status_address': 700, 'command_value': 28},
    '增菌液管放回':        {'write_address': 600, 'status_address': 700, 'command_value': 29},
    '增菌液管开盖':        {'write_address': 600, 'status_address': 700, 'command_value': 71},
    '增菌液液面探高':      {'write_address': 600, 'status_address': 700, 'command_value': 72},
    '增菌液样本接种':      {'write_address': 600, 'status_address': 700, 'command_value': 73},
    '增菌液管合盖':        {'write_address': 600, 'status_address': 700, 'command_value': 74},
    '培养皿喷码':         {'write_address': 600, 'status_address': 700, 'command_value': 75},
    '培养皿扫码':         {'write_address': 600, 'status_address': 700, 'command_value': 76},
    '加梯度菌液to培养皿':  {'write_address': 600, 'status_address': 700, 'command_value': 77},
    '培养皿旋转扫码':      {'write_address': 600, 'status_address': 700, 'command_value': 78},
    '移液头末端标定':      {'write_address': 600, 'status_address': 700, 'command_value': 79},
    '挑菌作业':           {'write_address': 600, 'status_address': 700, 'command_value': 80},
    '增菌液菌群接种':      {'write_address': 600, 'status_address': 700, 'command_value': 81},
    ## 保种涂布
    '转移培养皿':          {'write_address': 600, 'status_address': 700, 'command_value': 30},
    '涂布工具灭菌(500度)':  {'write_address': 600, 'status_address': 700, 'command_value': 31},
    '样品涂布(小于30度)':   {'write_address': 600, 'status_address': 700, 'command_value': 32},
    '培养皿盖放回':         {'write_address': 600, 'status_address': 700, 'command_value': 33},
    '培养皿放回库位':       {'write_address': 600, 'status_address': 700, 'command_value': 34},
    '培养皿开盖':          {'write_address': 600, 'status_address': 700, 'command_value': 42},
    '培养皿琼脂探高':       {'write_address': 600, 'status_address': 700, 'command_value': 43},
    '培养皿拍照':          {'write_address': 600, 'status_address': 700, 'command_value': 44},
    ## 耗材废弃
    '移液头盒废弃':         {'write_address': 600, 'status_address': 700, 'command_value': 35},
    '多孔板废弃':          {'write_address': 600, 'status_address': 700, 'command_value': 36},
    '样品管废弃':          {'write_address': 600, 'status_address': 700, 'command_value': 37},
    '样品管治具废弃':       {'write_address': 600, 'status_address': 700, 'command_value': 38},
    '平皿废弃':            {'write_address': 600, 'status_address': 700, 'command_value': 39},
    '平皿治具废弃':         {'write_address': 600, 'status_address': 700, 'command_value': 40},
    ## 梯度稀释
    '多孔板加缓冲液':      {'write_address': 600, 'status_address': 700, 'command_value': 65},
    '安装移液头':         {'write_address': 600, 'status_address': 700, 'command_value': 66},
    '吸取样品悬浊液':      {'write_address': 600, 'status_address': 700, 'command_value': 67},
    '吹打混匀':           {'write_address': 600, 'status_address': 700, 'command_value': 68},
    '丢弃移液头':         {'write_address': 600, 'status_address': 700, 'command_value': 69},
    '吸取梯度稀释液':      {'write_address': 600, 'status_address': 700, 'command_value': 70},
    ## 其他动作映射
    '样品管开盖':          {'write_address': 600, 'status_address': 700, 'command_value': 60},
    '样品管加液':          [{'write_address': 608, 'status_address': 708, 'command_value': 100},
                         {'write_address': 600, 'status_address': 700, 'command_value': 61}],
    '样品管关盖':          {'write_address': 600, 'status_address': 700, 'command_value': 62},
    '样品研磨操作(启动)':   {'write_address': 600, 'status_address': 700, 'command_value': 63},
    '样品离心操作(启动)':   {'write_address': 600, 'status_address': 700, 'command_value': 64},
    '加研磨球':           [{'write_address': 622, 'status_address': 622, 'command_value': 3},
                         {'write_address': 600, 'status_address': 700, 'command_value': 82}],
    '行架XY轴调用':       {'write_address': 600, 'status_address': 700, 'command_value': 83},
    '行架Z轴调用':         {'write_address': 600, 'status_address': 700, 'command_value': 84},
    '移液头库位数据重置':   {'write_address': 646, 'status_address': 646, 'command_value': 1},
    '消毒加热炉温度设置':   {'write_address': 631, 'status_address': 631, 'command_value': 1},
    '开启消毒加热炉':      {'write_address': 630, 'status_address': 737, 'command_value': 1},
    '原点回归':           {'write_address': 611, 'status_address': 701, 'command_value': 1},
    '系统启动':           {'write_address': 612, 'status_address': 702, 'command_value': 1},
    '系统重置':           {'write_address': 614, 'status_address': 703, 'command_value': 1},
    '紧急停止':           {'write_address': 615, 'status_address': 702, 'command_value': 1},
}

ACTION_GROUPS = {
    'start':                    ['原点回归', '系统启动'],
    'reset':                    ['系统重置','0'],
    'test':                     ['安装样品管夹爪', '机械臂快换释放'],
    'sample preparation':       ['安装样品管夹爪', '移走离心机盖', '装回离心机盖', '机械臂快换释放'],
    'consumables preparation':  ['安装样品治具夹爪', '多孔板转移', '盒装移液头转移', '盒装移液头上盖转移', '移液头库位数据重置',
                                 '增菌管治具转移', '0', '培养皿治具转移-高', '0', '安装样品管夹爪'],
    'grinding':                 ['样品管转移', '样品管开盖', '样品管加液', '加研磨球', '0', '样品管关盖', '研磨机顶盖打开',
                                 '样品管放入研磨机_1', '0', '样品管放入研磨机_2', '0', '样品管放入研磨机_3', '0',
                                 '安装研磨机压盖夹爪', '装研磨压盖', '研磨机顶盖关闭', '样品研磨操作(启动)',
                                 '研磨机顶盖打开', '取研磨压盖'],
    'centrifugal':              ['安装样品管夹爪', '移走离心机盖', '样品管研磨to离心机', '装回离心机盖', '样品离心操作(启动)',
                                 '移走离心机盖', '样品管离心放回'],
    'sample making':            ['增菌液管开盖', '安装移液头', '增菌液液面探高', '丢弃移液头', '样品管开盖', '安装移液头',
                                 '吸取样品悬浊液', '增菌液样本接种', '丢弃移液头', '增菌液管合盖', '增菌液管放回'],
    'serial dilution(T1)':      ['多孔板加缓冲液', '安装移液头', '吸取样品悬浊液', '吹打混匀', '丢弃移液头'],
    'serial dilution(T2)':      ['安装移液头', '吸取样品悬浊液', '吹打混匀', '0', '丢弃移液头'],
    'serial dilution(T3)':      ['安装移液头', '吸取样品悬浊液', '吹打混匀', '0', '丢弃移液头'],
    'serial dilution(T4)':      ['安装移液头', '吸取样品悬浊液', '吹打混匀', '0', '丢弃移液头'],
    'serial dilution(T5)':      ['安装移液头', '吸取样品悬浊液', '吹打混匀', '0', '丢弃移液头'],
    'set temperature':          ['消毒加热炉温度设置'],
    'petri dish coating':       ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取样品悬浊液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'petri dish coating(T1)':   ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取梯度稀释液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'petri dish coating(T2)':   ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取梯度稀释液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'petri dish coating(T3)':   ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取梯度稀释液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'petri dish coating(T4)':   ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取梯度稀释液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'petri dish coating(T5)':   ['开启消毒加热炉', '安装培养皿夹爪', '转移培养皿', '培养皿开盖',
                                 '培养皿喷码', '培养皿扫码', '安装涂布作业工具', '涂布工具灭菌(500度)', '安装移液头',
                                 '培养皿琼脂探高', '丢弃移液头', '安装移液头', '吸取梯度稀释液', '加梯度菌液to培养皿',
                                 '丢弃移液头', '样品涂布(小于30度)', '涂布工具灭菌(500度)', '安装培养皿夹爪', '培养皿盖放回',
                                 '培养皿放回库位'],
    'Workbench tidying':        ['样品管关盖'],
    'Isothermal culture':       ['安装样品治具夹爪']
    # 可以定义更多的动作组
    }
