# coding=UTF-8
import time

import pandas as pd
flows = pd.read_csv('app_behavior_02.csv', encoding='utf-8')

from floweaver import *

# Set the default size to fit the documentation better.
size = dict(width=570, height=300)

nodes = {
    'app_behavior': ProcessGroup(['查询余额', '查询账单', '密码错误']),
    'evaluation': ProcessGroup(['命中', '未命中']),
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
nodes['intend'] = Waypoint()

# 2. Update the ordering to show where the waypoint goes: in the middle
ordering = [
    ['app_behavior'],
    ['intend'],
    ['evaluation'],
]

intend = Partition.Simple('intend', ['了解分期活动', '延迟还款', '账单分期','重置查询密码','重置交易密码','更改交易密码','其它'])


# 3. Update the bundle definition to send the flows via the waypoint
bundles = [
    Bundle('app_behavior', 'evaluation', waypoints=['intend']),
]

# Update the SDD with the new nodes, ordering & bundles.
sdd = SankeyDefinition(nodes, bundles, ordering,
                       flow_partition=intend)

nodes['intend'] = Waypoint(intend)

print("going to produce")
# weave(sdd, flows).to_widget(**size).auto_save_png("ivr_rec.png")
# weave(sdd, flows).to_widget().auto_save_png('ivr_rec.png')
weave(sdd, flows).to_json('ivr_rec_sankey.json', format="widget")
