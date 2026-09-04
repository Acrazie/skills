# Jenkins Pipeline capability requirements

No plugin installation is performed by this repository. The Jenkins controller must already provide these capabilities:

| Required capability / syntax | Providing plugin |
|---|---|
| Declarative `pipeline`, `agent`, `stages`, `stage`, `steps`, `post`, `environment`, and `options` syntax | Pipeline: Declarative (`pipeline-model-definition`) |
| Core Pipeline execution and Groovy `script` blocks | Pipeline: Groovy (`workflow-cps`); the Pipeline job type is supplied by Pipeline: Job (`workflow-job`) |
| `checkout scm` for this Git repository | Pipeline: SCM Step (`workflow-scm-step`) with Git (`git`) as the SCM implementation |
| `sh` on the Linux agent | Pipeline: Nodes and Processes (`workflow-durable-task-step`), backed by Durable Task (`durable-task`) |
| `readFile`, `error`, and `timeout` steps | Pipeline: Basic Steps (`workflow-basic-steps`) |
| `input`, including `submitter` and `submitterParameter` for the production gate | Pipeline: Input Step (`pipeline-input-step`) |
| `withCredentials` and `usernamePassword` using credential ID `orders-registry` | Credentials Binding (`credentials-binding`); the credential record itself uses the Jenkins Credentials (`credentials`) username/password type |
| `junit` test-result publication | JUnit (`junit`) |
| `echo` | Pipeline: Basic Steps (`workflow-basic-steps`) |

The agent also needs non-plugin runtime prerequisites: a Unix shell, Git, PHP 8.3, Composer, Docker CLI/daemon access, access to `registry.example.invalid`, and permission to execute `ops/deploy.sh`. Jenkins must resolve the `orders-release-managers` group for the production `input` authorization check.
