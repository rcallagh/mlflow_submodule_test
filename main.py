#!/usr/bin/env python3
import mlflow
import submod_for_mlflow_test.submod as sm



def main():

    print('Running the mlflow test')
    print('Running a submodule function ')
    sm.print_statement()

    print('Mlflow worked')
    mlflow.log_metric('worked', 1)

if __name__ == "__main__":
    main()
