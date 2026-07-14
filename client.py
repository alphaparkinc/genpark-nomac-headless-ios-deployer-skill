class NoMacHeadlessIosDeployerClient:
    def deploy_agent(self, agent_bundle_path: str, target_environment: str) -> dict:
        return {"build_success": True, "deploy_url": f"https://nomac.app/deploy/genpark-app-live"}