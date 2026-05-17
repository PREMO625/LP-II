# Oral Viva Guide - CC P02 (Google App Engine)

## Quick One-Liners

- **GAE**: PaaS to deploy apps without managing servers.
- **app.yaml**: App Engine config file.
- **gcloud**: Google Cloud CLI.
- **Flask**: Python web framework.
- **gunicorn**: Production WSGI server.

---

## Basic Questions

1. What is Google App Engine?
   - A PaaS platform to host web apps on Google Cloud.
2. What is gcloud init?
   - Initializes the Google Cloud SDK, account, and project.
3. What is app.yaml?
   - Configuration file defining runtime and entrypoint.
4. What is Flask?
   - Lightweight Python web framework.
5. What is gunicorn?
   - WSGI server for running Flask in production.
6. What is requirements.txt?
   - Lists Python dependencies.
7. What does gcloud app deploy do?
   - Deploys the app to App Engine.
8. What does gcloud app browse do?
   - Opens the deployed app in a browser.
9. What does gcloud app logs tail do?
   - Streams application logs.
10. What is PaaS?
    - Platform as a Service where infrastructure is managed by provider.

---

## Intermediate Questions

11. Why use Python 3 instead of Python 2.7?
    - Python 2.7 is deprecated.
12. What is the default port for App Engine?
    - The runtime uses $PORT provided by the platform.
13. Why use gunicorn instead of flask run?
    - Gunicorn is production-ready.
14. Local hosting vs cloud hosting?
    - Local runs on PC, cloud runs on Google servers.
15. What happens during gcloud app deploy?
    - Uploads code, builds runtime, deploys service, gives URL.
16. What is a service in App Engine?
    - A versioned set of instances serving a specific app component.
17. What is a version in App Engine?
    - A deployable snapshot of your code.
18. What is the default service name?
    - default.
19. What is the runtime used here?
    - python39.
20. Why is billing required?
    - App Engine needs a billing-enabled project to deploy.

---

## Advanced Questions

21. What is the difference between Standard and Flexible environment?
    - Standard is faster scaling; Flexible gives more control.
22. How do you set environment variables in App Engine?
    - In app.yaml under env_variables.
23. How do you enable scaling rules?
    - In app.yaml (automatic, manual, or basic scaling).
24. What is a health check?
    - A probe to ensure instances are alive.
25. What is a firewall rule in App Engine?
    - Controls incoming traffic sources.
26. How is logging handled?
    - Logs are sent to Cloud Logging.
27. What is the entrypoint?
    - The command that starts the app.
28. What is WSGI?
    - Python standard for web server interface.
29. Can App Engine connect to a database?
    - Yes, via Cloud SQL or other services.
30. What are common deployment errors?
    - Billing disabled, invalid app.yaml, missing dependencies.

---

## External Examiner Questions

31. Is App Engine serverless?
    - It is managed PaaS (serverless-like), but not the same as Cloud Functions.
32. Can you run Docker on App Engine Standard?
    - Not directly; use Flexible for custom runtimes.
33. Why use App Engine instead of Compute Engine?
    - App Engine manages infrastructure and scaling.
34. What happens if you stop your local machine?
    - Cloud app continues running.
35. Can you deploy multiple services?
    - Yes, using multiple app.yaml files or service configs.

---

## Quick Memory Sheet

- gcloud init = configure
- app.yaml = config
- gunicorn = server
- deploy = publish
- browse = open URL
