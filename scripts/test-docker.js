#!/usr/bin/env node

const { spawnSync } = require("child_process");

const containerName = process.env.DOCKER_CONTAINER_NAME || "coding-tools-test";
const hostPort = process.env.DOCKER_TEST_PORT || "8080";
const imageName = process.env.DOCKER_IMAGE || "coding-tools";

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    stdio: options.stdio || "inherit",
    shell: false,
    env: Object.assign({}, process.env, options.env || {})
  });
  if (!options.allowFailure && result.status !== 0) {
    throw new Error(`${command} ${args.join(" ")} failed with exit code ${result.status}`);
  }
  return result;
}

function cleanup() {
  run("docker", ["rm", "-f", containerName], { allowFailure: true, stdio: "ignore" });
}

try {
  cleanup();
  run("docker", ["build", "-t", imageName, "."]);
  run("docker", ["run", "-d", "--name", containerName, "-p", `${hostPort}:80`, imageName]);
  run(process.execPath, ["scripts/test-docker-container.js"], {
    env: {
      DOCKER_TEST_URL: `http://127.0.0.1:${hostPort}`
    }
  });
} catch (error) {
  console.error(error.message);
  run("docker", ["logs", containerName], { allowFailure: true });
  process.exitCode = 1;
} finally {
  cleanup();
}

