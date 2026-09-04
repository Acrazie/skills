#!/usr/bin/env python3
"""Deterministic checks for Jenkins skill evaluation outputs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def contains(path: Path, text: str) -> bool:
    return path.exists() and text in path.read_text(errors="replace")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("eval_id", type=int)
    parser.add_argument("outputs", type=Path)
    parser.add_argument("--fixture", type=Path, required=True)
    args = parser.parse_args()

    out = args.outputs
    fixture = args.fixture
    checks: dict[str, object] = {
        "eval_id": args.eval_id,
        "outputs": str(out),
        "files": sorted(str(p.relative_to(out)) for p in out.rglob("*") if p.is_file() and "target" not in p.parts),
    }

    if args.eval_id == 1:
        result = (out / "RESULT.md").read_text(errors="replace") if (out / "RESULT.md").exists() else ""
        result_lower = result.lower()
        checks.update({
            "jenkinsfile_absent": not (out / "Jenkinsfile").exists(),
            "adr_files_absent": not any(p.is_file() for p in out.glob("docs/adr/*")),
            "result_exists": bool(result),
            "result_mentions_credential_id": "checkout-registry" in result,
            "result_mentions_immutable_promotion": "immutable" in result_lower,
            "result_mentions_all_repo_commands": all(x in result for x in ["pnpm lint", "pnpm test:ci", "pnpm build", "pnpm image:build", "ops/deploy.sh", "ops/rollback.sh"]),
            "result_distinguishes_unknown_controller_facts": all(x in result_lower for x in ["controller", "plugin", "agent", "unknown"]),
            "result_mentions_plugin_capabilities": "plugin" in result_lower and ("input" in result_lower or "approval" in result_lower),
            "result_flags_approver_policy_unresolved": any(x in result_lower for x in ["submitter", "approver", "approbateur"]) and any(x in result_lower for x in ["unresolved", "unknown", "confirm", "missing", "block"]),
            "deploy_script_unchanged": sha256(out / "ops/deploy.sh") == sha256(fixture / "ops/deploy.sh"),
            "rollback_script_unchanged": sha256(out / "ops/rollback.sh") == sha256(fixture / "ops/rollback.sh"),
        })
    elif args.eval_id == 2:
        jf = (out / "Jenkinsfile").read_text(errors="replace") if (out / "Jenkinsfile").exists() else ""
        result = (out / "RESULT.md").read_text(errors="replace") if (out / "RESULT.md").exists() else ""
        result_lower = result.lower()
        checks.update({
            "jenkinsfile_exists": bool(jf),
            "declarative_pipeline": "pipeline {" in jf,
            "legacy_top_level_node_absent": not jf.lstrip().startswith("node("),
            "hardcoded_password_absent": "insecure-example" not in jf,
            "credential_id_present": "orders-registry" in jf,
            "composer_lock_install_present": "composer install" in jf,
            "composer_ci_scripts_present": all(x in jf for x in ["ci:lint", "ci:test", "ci:build"]),
            "docker_build_count": jf.count("docker build"),
            "docker_push_count": jf.count("docker push"),
            "deploy_script_present": "ops/deploy.sh" in jf,
            "rollback_script_present": "ops/rollback.sh" in jf,
            "production_input_present": "input" in jf and "production" in jf.lower(),
            "approval_timeout_30_minutes": "timeout" in jf and "30" in jf and "MINUTES" in jf.upper(),
            "approval_submitter_restricted": "submitter:" in jf and "orders-release-managers" in jf,
            "approval_identity_captured": "submitterParameter" in jf,
            "junit_present": "junit" in jf,
            "pipeline_input_plugin_reported": any(x in result_lower for x in ["pipeline: input step", "pipeline input step", "pipeline-input-step"]),
            "controller_validation_limit_reported": "controller" in result_lower and any(x in result_lower for x in ["not performed", "not run", "not executed", "non exécut"]),
            "adr_unchanged": sha256(out / "docs/adr/0001-modernize-jenkins.md") == sha256(fixture / "docs/adr/0001-modernize-jenkins.md"),
            "result_exists": bool(result),
        })
    elif args.eval_id == 3:
        jf_path = out / "Jenkinsfile"
        original = (fixture / "Jenkinsfile").read_text()
        expected = original.replace("cargo junit --locked", "cargo test --locked")
        actual = jf_path.read_text(errors="replace") if jf_path.exists() else ""
        checks.update({
            "exact_approved_jenkinsfile": actual == expected,
            "cargo_test_present": "cargo test --locked" in actual,
            "cargo_junit_absent": "cargo junit --locked" not in actual,
            "adr_files_absent": not any(p.is_file() for p in out.glob("docs/adr/*")),
            "result_exists": (out / "RESULT.md").is_file(),
            "result_mentions_exit_101": contains(out / "RESULT.md", "101"),
            "result_mentions_fmt": contains(out / "RESULT.md", "cargo fmt --check"),
            "result_mentions_test": contains(out / "RESULT.md", "cargo test --locked"),
        })
    else:
        raise SystemExit(f"unsupported eval_id: {args.eval_id}")

    print(json.dumps(checks, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
