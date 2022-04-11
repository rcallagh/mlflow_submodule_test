#!/usr/bin/env python3
import mlflow
import submod_for_mlflow_test.submod as sm


def main():

    with mlflow.start_run() as run:
        print('Running the mlflow test')
        print('Running a submodule function ')
        sm.print_statement()

        git_commit = run.data.tags['mlflow.source.git.commit']

        print('Mlflow worked on commit {}'.format(git_commit))
        mlflow.log_metric('worked', 1)
        mlflow.log_param('git_commit', git_commit)

if __name__ == "__main__":
    main()
