import yaml

with open("centos.yaml") as f:
     tpl = yaml.safe_load(f)

edges = ["edge-amine1","edge-amine2","edge-amine3", "edge-amine4"]
for edge in edges:
  for i in range(2):
    name = f"centos-{edge}{i}"
    with open(f"resources/{name}.yaml", 'w') as f1:
       tpl["metadata"]["name"]= name
       tpl["spec"]["nodeName"] = edge
       yaml.dump(tpl, f1)
