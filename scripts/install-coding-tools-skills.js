#!/usr/bin/env node

const fs = require("fs");
const os = require("os");
const path = require("path");

const repoRoot = path.resolve(__dirname, "..");
const sourceRoot = path.join(repoRoot, "skills", "coding-tools");

function usage() {
  console.log(`Install Coding.Tools Codex skills.

Usage:
  npx github:<owner>/<repo> [--target <dir>] [--force] [--dry-run]
  node scripts/install-coding-tools-skills.js [--target <dir>] [--force] [--dry-run]

Options:
  --target <dir>  Destination skills directory. Defaults to $CODEX_HOME/skills or ~/.codex/skills.
  --force         Overwrite existing Coding.Tools skill folders.
  --dry-run       Print what would be installed without copying files.
  --list          List bundled skills.
  --help          Show this help.
`);
}

function defaultTarget() {
  const codexHome = process.env.CODEX_HOME || path.join(os.homedir(), ".codex");
  return path.join(codexHome, "skills");
}

function parseArgs(argv) {
  const args = {
    target: defaultTarget(),
    force: false,
    dryRun: false,
    list: false,
    help: false
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (arg === "--target") {
      const value = argv[index + 1];
      if (!value) throw new Error("--target requires a directory path.");
      args.target = path.resolve(value);
      index += 1;
    } else if (arg === "--force") {
      args.force = true;
    } else if (arg === "--dry-run") {
      args.dryRun = true;
    } else if (arg === "--list") {
      args.list = true;
    } else if (arg === "--help" || arg === "-h") {
      args.help = true;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }

  return args;
}

function listSkillDirs() {
  if (!fs.existsSync(sourceRoot)) {
    throw new Error(`Missing skill source directory: ${sourceRoot}`);
  }
  return fs
    .readdirSync(sourceRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => entry.name)
    .sort();
}

function copyDir(source, target) {
  fs.mkdirSync(target, { recursive: true });
  for (const entry of fs.readdirSync(source, { withFileTypes: true })) {
    const from = path.join(source, entry.name);
    const to = path.join(target, entry.name);
    if (entry.isDirectory()) {
      copyDir(from, to);
    } else {
      fs.copyFileSync(from, to);
    }
  }
}

function removeDir(target) {
  fs.rmSync(target, { recursive: true, force: true });
}

function main() {
  let args;
  try {
    args = parseArgs(process.argv.slice(2));
  } catch (error) {
    console.error(error.message);
    usage();
    process.exitCode = 1;
    return;
  }

  if (args.help) {
    usage();
    return;
  }

  const skills = listSkillDirs();

  if (args.list) {
    for (const skill of skills) console.log(skill);
    return;
  }

  if (!args.dryRun) fs.mkdirSync(args.target, { recursive: true });

  let installed = 0;
  let skipped = 0;
  for (const skill of skills) {
    const source = path.join(sourceRoot, skill);
    const target = path.join(args.target, skill);
    if (fs.existsSync(target) && !args.force) {
      console.log(`skip ${skill} (already exists; pass --force to overwrite)`);
      skipped += 1;
      continue;
    }
    if (args.dryRun) {
      console.log(`install ${skill} -> ${target}`);
    } else {
      if (fs.existsSync(target)) removeDir(target);
      copyDir(source, target);
      console.log(`installed ${skill}`);
    }
    installed += 1;
  }

  const action = args.dryRun ? "Would install" : "Installed";
  console.log(`${action} ${installed} Coding.Tools skills to ${args.target}. Skipped ${skipped}.`);
}

main();
