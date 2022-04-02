from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2ElasticIpAddress
from diagrams.aws.network import InternetGateway, RouteTable, VPCRouter
from diagrams.onprem.compute import Nomad
from diagrams.onprem.network import Consul

# Variables
outformat = "png"
filename = "nomad-aws-diagram"


with Diagram(filename=filename, outformat=outformat, ) as diag:
    with Cluster("Region:   eu-north-1"):
        with Cluster("VPC"):
            with Cluster("AZ:   eu-north-1a"):
                with Cluster("public-subnet"):
                    consul_server = Consul("consul-server")
                    eip_consul_server = EC2ElasticIpAddress('eIP-server')
                    consul_server >> eip_consul_server

                    nomad_server = Nomad("nomad-server")
                    eip_nomad_server = EC2ElasticIpAddress('eIP-server')
                    nomad_server >> eip_nomad_server

                    nomad_client = Nomad("nomad-client")
                    eip_nomad_client = EC2ElasticIpAddress('eIP-client')
                    nomad_client >> eip_nomad_client

                    with Cluster("", direction='LR'):
                        route_table = RouteTable("route-table")
            internet_gatway = InternetGateway("internet-gateway")
            vpcRouter = VPCRouter()
    [ eip_nomad_server, eip_nomad_client, eip_consul_server ] >> route_table >> vpcRouter >> internet_gatway