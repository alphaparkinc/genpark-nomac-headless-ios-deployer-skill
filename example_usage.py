from client import NoMacHeadlessIosDeployerClient
client = NoMacHeadlessIosDeployerClient()
print(client.deploy_agent("/bundles/my-agent", "production"))