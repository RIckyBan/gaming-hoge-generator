data "external" "get_project" {
  program = ["/bin/bash", "${path.module}/get_project.sh"]
}

provider "google" {
    project = lookup(data.external.get_project.result, "project")
    region = var.region
    zone = var.region_zone
}