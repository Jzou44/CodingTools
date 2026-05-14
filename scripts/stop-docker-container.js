const { spawnSync } = require("child_process");
const containerName = process.env.DOCKER_CONTAINER_NAME || "coding-tools-test";

const result = spawnSync("docker", ["rm", "-f", containerName], {
  stdio: "inherit",
  shell: false
});

if (result.status !== 0) {
  process.exit(result.status || 1);
}
