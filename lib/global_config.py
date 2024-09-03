# the ID of the current Access Point

this_swarm_id = '1000'
# ap_communication_switch_port = 500

swarm_backbone_switch_port = 501

REDIS_PORT = 6379
CASSANDRA_PORT = 9402

# currently assuming a /24 mask
this_swarm_subnet='192.168.10.0'
this_swarm_dhcp_start = 2
this_swarm_dhcp_end  = 200

database_hostname = '192.168.1.128'
database_port = 9042

coordinator_physical_ip = '192.168.1.128'
coordinator_vip='192.168.10.1'
coordinator_mac = 'd8:3a:dd:a5:ca:b6'
coordinator_tcp_port = 29997
node_manager_tcp_port = 29997

default_thrift_port = 9090


ap_list = {
    'AP:004': ['34:13:e8:61:0a:35', '192.168.4.1'],
    'AP:005': ['34:13:e8:62:7f:0f', '192.168.5.1']
    }
