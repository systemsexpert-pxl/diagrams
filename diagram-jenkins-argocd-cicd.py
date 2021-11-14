# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from urllib.request import urlretrieve
from diagrams.k8s.compute import Deployment, ReplicaSet, Pod
from diagrams.k8s.network import Service, Ingress
from diagrams.k8s.podconfig import Secret
from diagrams.k8s.storage import PersistentVolume, PersistentVolumeClaim, Volume
from diagrams.k8s.ecosystem import Helm
from diagrams.onprem.ci import Jenkins
from diagrams.onprem.gitops import ArgoCD
from diagrams.onprem.vcs import Git, Gitea, Github, Gitlab
from diagrams.onprem.container import Docker
from diagrams.onprem.client import User
from diagrams.generic.os import LinuxGeneral
from diagrams.programming.framework import Angular, Flask, Flutter, Spring
from diagrams.programming.language import Go, Java, NodeJS, PHP
from diagrams.programming.flowchart import Document, MultipleDocuments
from diagrams.onprem.database import MongoDB, MariaDB, MySQL, PostgreSQL
from diagrams.onprem.iac import Ansible, Terraform
from diagrams.onprem.inmemory import Memcached, Redis
from diagrams.onprem.logging import Graylog, Loki
from diagrams.onprem.monitoring import Datadog, Grafana, Prometheus
from diagrams.onprem.network import Apache, HAProxy, Internet, Nginx, Traefik, Pfsense, ETCD
from diagrams.onprem.storage import CEPH, Glusterfs
from diagrams.oci.compute import OCIRegistry

with Diagram("Jenkins CI/CD Pipeline", filename="jenkins_argocd_cicd_pipeline", show=False):
    user_url = "https://image.freepik.com/free-vector/woman-officer-working-woman-flat-design-illustrator-icon_35659-24.jpg"
    user_icon = "bastion_qfjova.png"
    urlretrieve(user_url, user_icon)
    user = Custom("code change", user_icon)
    github = Git("Github")
    jenkins = Jenkins("Jenkins server")
    argocd = ArgoCD("ArgoCD")
    dockerhub = OCIRegistry("Docker Hub")
    with Cluster("Jenkins CI pipeline"):
        jenkins_test = Java("Test Code")
        jenkins_build = Docker("Build Image")
        jenkins_push = Docker("Push to docker repo")
        [jenkins_test >> jenkins_build >> jenkins_push]
    with Cluster("ArgoCD"):
        argocd
    with Cluster("Kubernetes Cluster"):
        with Cluster("Deployment"):
            with Cluster("ReplicaSet"):
                app_deploy = Pod("app")
                app_grp = [app_deploy, Pod("app"), Pod("app")]
    user >> Edge(label="commit") >> github >> Edge(
        label="triggers") >> jenkins
    jenkins_push >> dockerhub
    jenkins >> jenkins_test
    dockerhub >> Edge(label="image") >> argocd
    argocd >> app_grp
    github >> Edge(label="deployment config") >> argocd
