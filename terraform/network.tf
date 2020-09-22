resource "google_compute_network" "gaming-hoge-vpc" {
  name = "gaming-hoge-vpc"
  auto_create_subnetworks = false
}
resource "google_compute_subnetwork" "gaming-hoge-subnet" {
  name          = "gaming-hoge-subnet"
  ip_cidr_range = "10.240.0.0/24"
  network       = google_compute_network.gaming-hoge-vpc.name
  description   = "gaming-hoge-subnet"
  region        = "us-west1"
}