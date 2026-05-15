const { spawnSync } = require("child_process");
const containerName = process.env.DOCKER_CONTAINER_NAME || "coding-tools-test";

const result = spawnSync("docker", ["rm", "-f", containerName], {
  encoding: "utf8",
  shell: false
});

if (result.error) {
  console.error(result.error.message);
  process.exit(1);
}

if (result.status !== 0 && !/No such container/i.test(result.stderr || "")) {
  if (result.stderr) {
    process.stderr.write(result.stderr);
  }
  if (result.stdout) {
    process.stdout.write(result.stdout);
  }
  process.exit(result.status || 1);
}
