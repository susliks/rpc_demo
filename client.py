#!/usr/bin/env python  
import sys  
sys.path.append('./gen-py')  
sys.path.append('../gen-py')  

#from scheduler import UserService  
from scheduler import Serv  
from scheduler.ttypes import *  
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TCompactProtocol  
  

def construct_req_demo():
    req = Request()
    req.request_id = 2018
    req.v_node_num = 3
    req.v_edge_num = 3
    req.node_resource_dim_num = 2
    req.node = list()
    req.edge = list()
    req.v_map_p = list()

    tmp_node = Node()
    tmp_node.id = 1
    tmp_node.resource_need = dict()
    tmp_node.resource_need["cpu"] = 2
    tmp_node.resource_need["memory"] = 5
    req.node.append(tmp_node)

    tmp_node = Node()
    tmp_node.id = 2
    tmp_node.resource_need = dict()
    tmp_node.resource_need["cpu"] = 3
    tmp_node.resource_need["memory"] = 4
    req.node.append(tmp_node)

    tmp_node = Node()
    tmp_node.id = 3
    tmp_node.resource_need = dict()
    tmp_node.resource_need["cpu"] = 3
    tmp_node.resource_need["memory"] = 3
    req.node.append(tmp_node)

    tmp_edge = Edge()
    tmp_edge.from_id = 1
    tmp_edge.to_id = 2
    tmp_edge.bandwidth_needed = 2
    req.edge.append(tmp_edge)

    tmp_edge = Edge()
    tmp_edge.from_id = 2
    tmp_edge.to_id = 3
    tmp_edge.bandwidth_needed = 3
    req.edge.append(tmp_edge)

    tmp_edge = Edge()
    tmp_edge.from_id = 1
    tmp_edge.to_id = 3
    tmp_edge.bandwidth_needed = 3
    req.edge.append(tmp_edge)

    tmp_node_map = NodeMap()
    tmp_node_map.v_id = 1
    tmp_node_map.p_id = 1
    req.v_map_p.append(tmp_node_map)

    tmp_node_map = NodeMap()
    tmp_node_map.v_id = 2
    tmp_node_map.p_id = 2
    req.v_map_p.append(tmp_node_map)
    
    tmp_node_map = NodeMap()
    tmp_node_map.v_id = 3
    tmp_node_map.p_id = 7
    req.v_map_p.append(tmp_node_map)

    return req





# Make socket  
transport = TSocket.TSocket('127.0.0.1', 9090)  
# Buffering is critical. Raw sockets are very slow  
transport = TTransport.TBufferedTransport(transport)  
# Wrap in a protocol  
protocol = TCompactProtocol.TCompactProtocol(transport)  
# Create a client to use the protocol encoder  
client = Serv.Client(protocol)  
# Connect!  
transport.open()  
# Call Server services    

req = construct_req_demo()

res = client.put(req)  

print(res)
  
