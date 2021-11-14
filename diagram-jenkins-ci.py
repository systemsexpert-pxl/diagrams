# diagram.py
from diagrams import Cluster, Diagram, Edge
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

with Diagram("Jenkins CI Pipeline", filename="ci_pipeline", show=False):
    user = User("code change")
    github = Git("Github")
    jenkins = Jenkins("Jenkins server")
    with Cluster("CI pipeline"):
        jenkins_test = Java("Test Code")
        jenkins_build = Docker("Build Image")
        jenkins_push = OCIRegistry("Push to docker repo")
        [jenkins_test >> jenkins_build >> jenkins_push]
    user >> Edge(label="commit") >> github >> Edge(
        label="triggers") >> jenkins
    jenkins >> jenkins_test
    jenkins >> jenkins_build
    jenkins >> jenkins_push
