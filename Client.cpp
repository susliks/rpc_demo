#include "Serv.h"
#include <thrift/transport/TSocket.h>
#include <thrift/transport/TBufferTransports.h>
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/protocol/TCompactProtocol.h> 

using namespace apache::thrift;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

//using boost::shared_ptr;
using std::shared_ptr;

int main(int argc, char **argv)
{
    //std::shared_ptr<TSocket> socket(new TSocket("localhost", 9090));
    std::shared_ptr<TSocket> socket(new TSocket("127.0.0.1", 9090));
    std::shared_ptr<TTransport> transport(new TBufferedTransport(socket));
    //std::shared_ptr<TProtocol> protocol(new TBinaryProtocol(transport));
    std::shared_ptr<TProtocol> protocol(new TCompactProtocol(transport));

    transport->open();

    //调用server服务
    Student s, stu;
    s.sno = 123;
    s.sname = "hao973";
    s.ssex = 1;
    s.sage = 30;
    Node n1, n2;
    n1.id = 1;
    n1.resource.push_back(10);
    n1.resource.push_back(20);
    n2.id = 2;
    n2.resource.push_back(30);
    n2.resource.push_back(40);
    s.nodes.push_back(n1);
    s.nodes.push_back(n2);
    
    ServClient client(protocol);
    client.put(s);
/*
    ServClient client(protocol);
    printf("sno=%d sname=%s ssex=%d sage=%d\n", s.sno, s.sname.c_str(), s.ssex, s.sage);
    //put
    client.put(s);
    //icall scall
    std::string strname = "";
    client.scall(strname, s);
    printf("icall=%d, scall=%s\n", client.icall(s), strname.c_str());
    //stcall
    client.stcall(stu, s);
    printf("student sno=%d sname=%s ssex=%d sage=%d\n", stu.sno, stu.sname.c_str(), stu.ssex, stu.sage);
*/

    transport->close();

    return 0;
}

