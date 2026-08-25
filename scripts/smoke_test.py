"""Post-deploy smoke test for the staging environment.

Unlike the unit tests in tests/test_core.py (which check business logic
in isolation, before anything is deployed anywhere), this check runs
*after* deploy_staging and simulates a minimal "is the deployed thing
alive" probe against the staging environment.
"""


def main():
    staging_is_healthy = 1 == 2  # simulated health-check result
    assert staging_is_healthy, "smoke test failed: staging environment did not respond as expected"
    print("Smoke test passed: staging is healthy.")


if __name__ == "__main__":
    main()
