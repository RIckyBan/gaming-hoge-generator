resource "google_compute_firewall" "gaming-hoge-allow-internal" {
  name    = "gaming-hoge-allow-internal"
  network = google_compute_network.gaming-hoge-vpc.name

  allow {
    protocol = "tcp"
  }

    allow {
    protocol = "udp"
  }

    allow {
    protocol = "icmp"
  }

  allow {
    protocol = "ipip"
  }

  source_ranges = ["10.240.0.0/24"]
}

resource "google_compute_firewall" "gaming-hoge-allow-external" {
  name    = "gaming-hoge-allow-external"
  network = google_compute_network.gaming-hoge-vpc.name

  allow {
    protocol = "tcp"
    ports    = ["22", "6443"]
  }

    allow {
    protocol = "icmp"
  }

  source_ranges = ["0.0.0.0/0"]
}