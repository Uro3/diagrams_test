from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS, ElastiCache
from diagrams.aws.network import ELB
from diagrams.onprem.client import Users

with Diagram("システム構成図", show=False):
    with Cluster("AWS"):
        with Cluster("Auto Scaling Group"):
            fleet = [EC2("web1"), EC2("web2"), EC2("web3")]

        with Cluster("DB Cluster"):
            rds_primary = RDS("primary")
            rds_secondary = RDS("secondary")
            rds_primary - rds_secondary

        alb = ELB("alb")
        redis = ElastiCache("redis")

    users = Users("ユーザ")

    users >> alb >> fleet
    fleet >> rds_primary
    fleet >> redis
