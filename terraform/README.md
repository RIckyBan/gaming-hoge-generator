# Infrastructure as Code by terraform

## Setup a instance with kubeadm

1. install terraform
2. `terraform init`
3. `gcloud config set project {your-project}`
4. `gcloud auth application-default login`
5. `terraform apply`

## Setup kubernetes cluster with kubeadm

### Controller Node Setup

```bash
sudo kubeadm init --pod-network-cidr 192.168.0.0/16
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
kubectl taint nodes $(hostname) node-role.kubernetes.io/master:NoSchedule-
```

### Workder Node Setup

```bash
sudo kubeadm join 10.240.0.11:6443 --token vazvte.cpc8jurckkoczt67 \
    --discovery-token-ca-cert-hash sha256:9f166b4aaa483b11be7fa96f7c009611396ca4162596aadfba61352e444da1c0
```

### CNI setup

```bash
# on Controller
curl https://docs.projectcalico.org/manifests/calico.yaml -O
kubectl apply -f calico.yaml
```

## Further Reading

- [Creating a cluster with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/)
- [Creating Highly Available clusters with kubeadm](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/high-availability/)


