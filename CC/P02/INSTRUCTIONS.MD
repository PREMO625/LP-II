## Practical: Installation and Configuration of Google App Engine

### Terminal Execution Logs (Modern Workflow)

```text
PS D:\Projects\Learning Programs\LP-2\LP-II> gcloud init

Welcome! This command will take you through the configuration of gcloud.

Pick configuration to use:
 [1] Re-initialize this configuration [default] with new settings
 [2] Create a new configuration

Please enter your numeric choice: 1

Choose the account you want to use for this configuration.

Select an account:
 [1] geet.jamdal23@mmit.edu.in
 [2] Sign in with a new Google Account

Please enter your numeric choice: 1

You are signed in as: [geet.jamdal23@mmit.edu.in].

Pick cloud project to use:
 [1] college-cc-geet
 [2] Create a new project

Please enter your numeric choice: 2

Enter Project ID:
college-cc0

Waiting for project creation...

Your current project has been set to: [college-cc0].

The Google Cloud CLI is configured and ready to use!

* Commands that require authentication will use geet.jamdal23@mmit.edu.in by default
* Commands will reference project `college-cc0` by default
```

### Project Structure

```text
my-cloud-app/
│
├── app.yaml
├── main.py
└── requirements.txt
```

### Installing Flask

```text
PS D:\Projects\my-cloud-app> pip install flask gunicorn

Successfully installed flask gunicorn
```

### Running Application Locally

```text
PS D:\Projects\my-cloud-app> python main.py

 * Serving Flask app 'main'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

**Browser Output:**

```text
Hello from Google App Engine!
```

### Deploying Application to App Engine

```text
PS D:\Projects\my-cloud-app> gcloud app deploy
```

#### Region Selection

```text
Please choose the region where you want your App Engine application located:

 [1] asia-east1
 [2] asia-east2
 [3] asia-northeast1
 [4] asia-northeast2
 [5] asia-northeast3
 [6] asia-south1
 [7] asia-southeast1
 ...

Please enter your numeric choice: 6
```

#### Ideal Successful Deployment Logs (If Billing Was Enabled)

```text
Creating App Engine application in project [college-cc0] and region [asia-south1]....done.

Services to deploy:

descriptor:      [app.yaml]
source:          [D:\Projects\my-cloud-app]
target project:  [college-cc0]
target service:  [default]
target version:  [20260517t193000]
target url:      [https://college-cc0.appspot.com]

Do you want to continue (Y/n)? Y

Beginning deployment of service [default]...
Uploading files...
Uploading 3 files to Google Cloud Storage
100% Done.

Updating service [default]...
Waiting for operation to complete...
done.

Deployed service [default] to [https://college-cc0.appspot.com]

You can stream logs from the command line by running:
  gcloud app logs tail -s default

To launch your browser with the app at:
  gcloud app browse
```

### Opening Hosted Cloud Application

```text
PS D:\Projects\my-cloud-app> gcloud app browse
```

**Browser Opens:**

```text
https://college-cc0.appspot.com
```

**Output:**

```text
Hello from Google App Engine!
```

---

## Application Files

### main.py

```python
from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Google App Engine!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

### requirements.txt

```text
flask
gunicorn
```

### app.yaml

```yaml
runtime: python39

entrypoint: gunicorn -b :$PORT main:app
```

---

## Important Viva Questions and Answers

### 1. What is Google App Engine?

Google App Engine is a PaaS (Platform as a Service) cloud platform used to deploy and host web applications without managing servers.

### 2. What is the purpose of gcloud init?

It initializes the Google Cloud SDK by:

- Authenticating the user account.
- Selecting the cloud project.
- Configuring default settings.

### 3. What is app.yaml?

`app.yaml` is the configuration file for App Engine. It defines:

- Runtime.
- Entry point.
- Scaling configuration.
- Deployment settings.

### 4. What is Flask?

Flask is a lightweight Python web framework used to build web applications and APIs.

### 5. What is the role of gunicorn?

Gunicorn is a production-grade WSGI server used to run Flask applications efficiently in cloud environments.

### 6. Difference Between Local Hosting and Cloud Hosting

| Local Hosting | Cloud Hosting |
| --- | --- |
| Runs on local PC | Runs on Google servers |
| Uses localhost | Uses public URL |
| Stops when PC shuts down | Available globally 24/7 |

### 7. What is PaaS?

PaaS stands for Platform as a Service. The cloud provider manages:

- Servers
- Infrastructure
- Scaling
- Networking

The developer only uploads application code.

### 8. What happens internally during gcloud app deploy?

```text
Application Code
-> gcloud CLI
-> Google Cloud Authentication
-> App Engine API
-> Upload Application
-> Create Runtime Environment
-> Deploy on Google Servers
-> Generate Public URL
```

### 9. Why was Python 2.7 not used?

The original practical used Python 2.7 and webapp2, which are deprecated in modern Google Cloud environments. The application was modernized using Python 3 and Flask.

### 10. What is the purpose of requirements.txt?

It contains all Python dependencies required for deployment, for example:

```
flask
gunicorn
```

---

## Important Note About Actual Execution

In the actual system execution, deployment stopped at:

```text
ERROR: (gcloud.app.deploy) INVALID_ARGUMENT:
The project must have a billing account attached.
```

**Reason:**

Google App Engine requires a billing-enabled Google Cloud project before creating cloud-hosted services.

Therefore:

- Local Flask execution worked successfully.
- Google Cloud configuration worked successfully.
- App Engine deployment workflow started successfully.
- Actual cloud deployment stopped due to billing restriction.

---

## Final Quick Revision

| Command | Purpose |
| --- | --- |
| gcloud init | Configure Google Cloud SDK |
| gcloud app deploy | Deploy app to App Engine |
| gcloud app browse | Open deployed cloud app |
| python main.py | Run Flask app locally |

---

## Final Conceptual Understanding

```text
Local Flask App
-> Google Cloud SDK
-> Google App Engine
-> Google Cloud Servers
-> Public Cloud Website
```

This practical demonstrates:

- Cloud application deployment workflow.
- App Engine configuration.
- Local vs cloud hosting.
- Google Cloud SDK usage.
- Modern Flask-based cloud deployment.