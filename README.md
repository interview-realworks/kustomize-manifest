

```markdown
# Hello World Python Application Deployment with Kustomize, Reloader and istio

This repository contains Kubernetes manifest files for deploying a simple "Hello World" Python application using Kubernetes, Kustomize, Reloader and Istio. The can be deployed multiple environments (test and prod) within the same Kubernetes cluster and namespace.

## Prerequisites

Before you begin, it is important to ensure that you have the following installed:

- [Kubernetes](https://kubernetes.io/docs/setup/)
- [Kustomize](https://kubectl.docs.kubernetes.io/installation/kustomize/)
- [Reloader](https://reloader.dev/docs/v0.0.0/getting-started/)
- [Istio](https://istio.io/latest/docs/setup/getting-started/)

## Manifest Explanation

The following Kubernetes resources will be created and managed using Kustomize, Reloader, and Istio:

1. **ServiceAccount**: Defines a service account for managing permissions.
2. **ClusterRole**: Specifies permissions to access resources.
3. **ClusterRoleBinding**: Binds the service account to the cluster role.
4. **ConfigMap**: Contains a simple message to display in the application.
5. **Service**: Exposes the application on port 80.
6. **Deployment (Reloader)**: Deploys the `reloader` container for automatic configuration updates.
7. **Deployment (Hello World)**: Deploys a simple "Hello World" Python application container.
8. **Gateway**: Defines an Istio gateway for external access.
9. **VirtualService**: Routes incoming traffic to the service.

## How to Run

1. Ensure that your Kubernetes cluster up and running.

2. Use the links provided below to install Kustomize, Reloader, and Istio.

3. Clone this repository:

   ```bash
   https://github.com/interview-realworks/kustomize-manifest.git
   ```

4. The deployment configuration can be customized by editing the Kustomize overlays in the `kustomize` directory.    
   Customization may include adjusting environment-specific settings, such as the number of replicas and image tags.

5. The Kustomize overlays for the desired environment (test or prod) can be applied using the following command:

   ```bash
   kubectl apply -k kustomize/overlays/<environment>
   ```

   Replace `<environment>` with the name of the environment (`test` or `prod`).

6. Access the application using the Istio Gateway:

   - Determine the IP of your Istio Ingress Gateway:

     ```bash
     kubectl get svc -n istio-system istio-ingressgateway
     ```

   - Open a web browser and navigate to: `http://<INGRESS_IP>/message`

7. You should see the "Hello World" message displayed on the page.

8. To test the automatic configuration updates, modify the `message.txt` value in the ConfigMap. Reloader will detect the change and trigger a rolling restart of the application.

## Cleanup

To remove the deployed resources, run:

```bash
kubectl delete -k kustomize/overlays/<environment>
```

## Notes

- This is a simplified example for demonstration purposes.
- Modify the Kustomize overlays as needed to suit your actual application requirements.
- Additional configuration or customization may be required based on your specific environment.

```

