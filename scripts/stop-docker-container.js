const { spawnSync } = require("child_process");

const result = spawnSync("docker", ["rm", "-f", "coding-tools-test"], {
  stdio: "inherit",
  shell: false
});

if (result.status !== 0) {
  process.exit(result.status || 1);
}
