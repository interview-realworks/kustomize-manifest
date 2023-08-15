Certainly! Here's the updated `readme.md` file for your Kubernetes manifest that uses Kustomize and Reloader as a controller:

```markdown
# Hello World Kubernetes Deployment with Kustomize and Reloader

This repository contains Kubernetes manifest files for deploying a simple "Hello World" application using Kubernetes, Kustomize, and Reloader.

## Prerequisites

Before you begin, make sure you have the following installed:

- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Kustomize](https://kubectl.docs.kubernetes.io/installation/kustomize/)
- [Reloader](https://reloader.dev/docs/v0.0.0/getting-started/)

## Manifest Explanation

This repository includes the following Kubernetes resources managed using Kustomize:

1. **ServiceAccount**: Defines a service account for managing permissions.
2. **ClusterRole**: Specifies permissions to access resources.
3. **ClusterRoleBinding**: Binds the service account to the cluster role.
4. **ConfigMap**: Contains a simple message to display in the application.
5. **Service**: Exposes the application on port 80.
6. **Deployment (Reloader)**: Deploys the `reloader` container for automatic configuration updates.
7. **Deployment (Hello World)**: Deploys a simple "Hello World" application container.
8. **Gateway**: Defines an Istio gateway for external access.
9. **VirtualService**: Routes incoming traffic to the service.

## How to Run

1. Make sure you have a Kubernetes cluster up and running.

2. Install Kustomize and Reloader by following the provided links.

3. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/hello-world-k8s.git
   cd hello-world-k8s
   ```

4. Customize the deployment configuration if needed by editing the Kustomize overlays in the `kustomize` directory.

5. Apply the Kustomize overlays using the following command:

   ```bash
   kubectl apply -k kustomize
   ```

6. Access the application using the Istio Gateway:

   - Determine the IP of your Istio Ingress Gateway:

     ```bash
     kubectl get svc -n istio-system istio-ingressgateway
     ```

   - Open a web browser and navigate to: `http://<INGRESS_IP>/message`

7. You should see the "Hello World" message displayed on the page.

## Cleanup

To remove the deployed resources, run:

```bash
kubectl delete -k kustomize
```

## Notes

- This is a simplified example for demonstration purposes.
- Modify the Kustomize overlays as needed to suit your actual application requirements.
- Additional configuration or customization may be required based on your specific environment.

```

Please customize this `readme.md` file further to match your specific repository structure, any additional information you want to provide, and any specific instructions for your environment or application.