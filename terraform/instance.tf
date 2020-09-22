resource "google_compute_instance" "gaming-hoge-controller" {
  name         = "gaming-hoge-controller"
  machine_type = "n1-standard-4"
  zone         = "us-west1-a"
  description  = "gaming-hoge-controller"
  tags         = ["gaming-hoge", "public-controller"]
  can_ip_forward = true
  
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
      size  = "30"
      type  = "pd-standard"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.gaming-hoge-subnet.name
    network_ip = "10.240.0.11"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOT
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y docker.io
    sudo groupadd docker 
    sudo usermod -aG docker $USER
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo apt install -y apt-transport-https curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
  EOT
}

resource "google_compute_instance" "gaming-hoge-worker-0" {
  name         = "gaming-hoge-worker-0"
  machine_type = "n1-standard-2"
  zone         = "us-west1-b"
  description  = "gaming-hoge-controller"
  tags         = ["gaming-hoge", "public-worker"]
  can_ip_forward = true
  
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
      size  = "30"
      type  = "pd-standard"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.gaming-hoge-subnet.name
    network_ip = "10.240.0.20"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOT
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y docker.io
    sudo groupadd docker 
    sudo usermod -aG docker $USER
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo apt install -y apt-transport-https curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
  EOT
}

resource "google_compute_instance" "gaming-hoge-worker-1" {
  name         = "gaming-hoge-worker-1"
  machine_type = "n1-standard-2"
  zone         = "us-west1-c"
  description  = "gaming-hoge-controller"
  tags         = ["gaming-hoge", "public-worker"]
  can_ip_forward = true
  
  boot_disk {
    initialize_params {
      image = "ubuntu-os-cloud/ubuntu-1804-lts"
      size  = "30"
      type  = "pd-standard"
    }
  }

  network_interface {
    subnetwork = google_compute_subnetwork.gaming-hoge-subnet.name
    network_ip = "10.240.0.21"

    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOT
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y docker.io
    sudo groupadd docker 
    sudo usermod -aG docker $USER
    sudo systemctl enable docker
    sudo systemctl start docker
    sudo apt install -y apt-transport-https curl
    curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-add-repository "deb http://apt.kubernetes.io/ kubernetes-xenial main"
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
  EOT
}