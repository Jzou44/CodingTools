const { spawnSync } = require("child_process");
const containerName = process.env.DOCKER_CONTAINER_NAME || "coding-tools-test";
const hostPort = process.env.DOCKER_TEST_PORT || "8080";
const imageName = process.env.DOCKER_IMAGE || "coding-tools";

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    stdio: options.stdio || "inherit",
    shell: false
  });
  if (!options.allowFailure && result.status !== 0) {
    process.exit(result.status || 1);
  }
  return result;
}

run("docker", ["rm", "-f", containerName], { allowFailure: true, stdio: "ignore" });
run("docker", ["run", "-d", "--name", containerName, "-p", `${hostPort}:80`, imageName]);
