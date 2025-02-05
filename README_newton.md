# ME700 Assignemnt 1 Part 1

## Newton's Method

Rebecca Shannon
2/10/2025

Development Notes

1. need to make for matricies, not just 1D systems
2. update check maxIter to exit if it fails and still pass the test

## About the solver

## Definitions

## Using the Code

### Initial Setup

Set up the conda environlment and test that the code is functioning. 

1. Create a new conda environment and activate it.  

    ```bash
    conda create --name A1-newton-method-env python=3.12
    ```

    ```bash
    conda activate A1-newton-method-env
    ```

2. Confirm that the right version of Python and pip setuptools are being used. Python should be version 3.12; the second command will update setuptools if necessary.

    ```bash
    python --version
    ```

    ```bash
    pip install --upgrade pip setuptools wheel
    ```

3. Navigate to the warmUp directory.  
4. Install an editable version of the code. Note that the *pyproject.toml* file is required for this.  

    ```bash
    pip install -e .
    ```

5. Test the code with pytest. This command returns code coverage for all files in the directory. Coverage for *warmUp/fnAssignment1.py* should be 100% and all tests should pass.  

    ```bash
    pytest -v --cov=warmUp  --cov-report term-missing
    ```  