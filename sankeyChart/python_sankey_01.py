# coding=UTF-8
import time

import pandas as pd
flows = pd.read_csv('app_behavior_02.csv', encoding='utf-8')

from floweaver import *

# Set the default size to fit the documentation better.
size = dict(width=570, height=300)

nodes = {
    'app_behavior': ProcessGroup(['查询余额', '查询账单', '密码错误'], title="来电前行为"),
    'evaluation': ProcessGroup(['命中', '未命中'], title='推荐结果'),
}
ordering = [
    ['app_behavior'],
    ['evaluation'],
]

app_behavior = Partition.Simple('process', [
    '查询余额',
    '查询账单',
    '密码错误',
])

# This is another partition.
evaluation = Partition.Simple('process', [
    '命中', '未命中'
])

# Update the ProcessGroup nodes to use the partitions
nodes['app_behavior'].partition = app_behavior
nodes['evaluation'].partition = evaluation


# 1. Define a new waypoint node
nodes['intend'] = Waypoint(title='来电意图')

# 2. Update the ordering to show where the waypoint goes: in the middle
ordering = [
    ['app_behavior'],
    ['intend'],
    ['evaluation'],
]
intend = Partition.Simple('intend', ['欢迎词', '延迟还款业务', '延迟还款', '账单分期业务', '账单分期', '分期优惠活动', '分期优惠活动_', '查询密码重置', '查询密码重置_', '交易密码重置', '交易密码重置_','修改交易密码', '修改交易密码_','新办信用卡', '理财业务咨询','其它'])


# 3. Update the bundle definition to send the flows via the waypoint
bundles = [
    Bundle('app_behavior', 'evaluation', waypoints=['intend']),
]

# Update the SDD with the new nodes, ordering & bundles.
sdd = SankeyDefinition(nodes, bundles, ordering,
                       flow_partition=intend)

nodes['intend'] = Waypoint(intend, title='来电意图')

print("going to produce")
# weave(sdd, flows).to_widget(**size).auto_save_png("ivr_rec.png")
# weave(sdd, flows).to_widget().auto_save_png('ivr_rec.png')
# weave(sdd, flows).to_json('ivr_rec_sankey.json', format="widget")
weave(sdd, flows,
      palette='Set2_8',
      link_color=CategoricalScale('isLastHit', palette='Set2_8'),
      measures=['value', 'isLastHit'],
      link_width='value').to_json('ivr_rec_sankey.json', format="widget")