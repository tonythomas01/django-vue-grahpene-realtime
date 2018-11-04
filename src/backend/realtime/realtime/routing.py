from channels import include

project_routing = [
    include('dashboard.routing.app_routing', path=r'^/snippet-ws'),
]
