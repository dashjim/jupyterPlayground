
import time

import pandas as pd
flows = pd.read_csv('app_behavior_02.csv', encoding='utf-8')

from floweaver import *

# Set the default size to fit the documentation better.
size = dict(width=570, height=300)

nodes = {
    'app_behavior': ProcessGroup(['余额', 'checking_bills', 'invalid_password']),
    'evaluation': ProcessGroup(['hit', 'miss']),
}
ordering = [
    ['app_behavior'],
    ['evaluation'],
]

app_behavior = Partition.Simple('process', [
    '余额',
    'checking_bills',
    'invalid_password',
])

# This is another partition.
evaluation = Partition.Simple('process', [
    'hit', 'miss'
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

intend = Partition.Simple('intend', ['installment_campaign', 'delay_payment','billing_installment','reset_password_lookup','reset_password_trading','change_password_trading','others'])


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
weave(sdd, flows, measures={'isLastHit': 'sum'}, link_color=QuantitativeScale('isLastHit')).to_json('ivr_rec_sankey.json', format="widget")
