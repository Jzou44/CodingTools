const { spawnSync } = require("child_process");

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

run("docker", ["rm", "-f", "coding-tools-test"], { allowFailure: true, stdio: "ignore" });
run("docker", ["run", "-d", "--name", "coding-tools-test", "-p", "8080:80", "coding-tools"]);
