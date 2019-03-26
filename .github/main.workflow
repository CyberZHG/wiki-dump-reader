workflow "Code Style" {
  on = "push"
  resolves = ["lint-action"]
}

action "lint-action" {
  uses = "CyberZHG/github-action-python-lint@master"
  args = "--max-line-length=120 wiki_dump_reader tests"
}

workflow "Unit Test" {
  on = "push"
  resolves = ["test-action"]
}

action "test-action" {
  uses = "CyberZHG/github-action-python-test@master"
  args = "tests"
}
