# ASSIGNMENT 2; Group 7

**Bachelor of Business Administration & Artificial Intelligence for Business - BBA & BAIB**  
**Software Development**  
**Assignment 2 Report: Practical Implementation of Git for Collaborative Development**

## Overview
This project documents all of the steps taken by our group to develop, integrate, test, and release features during Assignment 2 using Git and GitHub. Each team member was assigned a specific role, contributing to the successful development of several features, branch management, conflict resolution, and quality control. Below, we detail the team’s workflow, the process of resolving conflicts, the roles of each member, and the implementation of Git version control.

## Role Assignment
- **Master branch and final releases manager (Lead Integrator):** Lucas
- **Develop branch and quality control manager (Development Integrator):** Gael
- **Feature 1 Developer (Feature 1 Lead):** Carlos
- **Feature 2 Developer (Feature 2 Lead):** Nicky
- **Hotfix and maintenance manager (Maintenance and Hotfix Manager):** Albert
- **Advanced testing and project verification (QA and Final Verification):** Victor

## Our Workflow History

### STEP 0: GitHub Repository Implementation
- **Lucas** created the initial GitHub repository and performed the following:
  - Added repository name and description.
  - Cloned the repository: `git clone URL`.
  - Created a README file and added it to the main branch: `touch README.md`.
  - Made initial commits and pushed the main branch: 
    ```
    git commit -m "A: Initial creation of main branch with README.md"
    git push origin main
    ```
  - Created the `develop` branch to begin feature development:
    ```
    git checkout -b develop
    git push origin develop
    ```

---

### STEP 1: Feature Development
- **Carlos and Nicky** developed their respective features:
  - Checked out the `develop` branch and created feature branches for development:
    ```
    git checkout develop
    git checkout -b featureX
    git push origin featureX
    ```
- **Carlos** implemented Feature 1:
  - Created and implemented `file1_feature1.py`:
    ```
    touch file1_feature1.py
    git add file1_feature1.py
    git commit -m "C: Start of feature 1 implementation"
    ```
  - Finalized implementation and pushed Feature 1:
    ```
    git add file1_feature1.py
    git commit -m "D: Final implementation of feature 1 with some bugs"
    git push origin feature1
    ```
- **Gael** managed the merging process:
  - Merged Feature 1 into the `develop` branch:
    ```
    git checkout develop
    git pull origin develop
    git merge origin/feature1 -m "E: Merging feature1 into develop"
    git push origin develop
    ```
- **Nicky** worked on Feature 2:
  ```
  touch file1_feature2.py
  git add file1_feature2.py
  git commit -m "F1: Start of feature 2 implementation"
  git push origin feature2
  ```

---

### STEP 3: First Release (v1.00)
- **Gael** prepared for the first release:
  - Created a release branch and made final adjustments:
    ```
    git checkout develop
    git pull origin develop
    git checkout -b release1
    touch file_release1.py
    git add file_release1
    git commit -m "G: Final Adjustments for release v1.00"
    git push origin release1
    ```
- **Lucas** merged release 1 into `main` and tagged it as version 1.00:
  ```
  git checkout main
  git pull origin main
  git merge origin/release1 -m "H: Release v1.00"
  git push origin main
  git tag -a v1.00 -m "v1.00: First release"
  git push origin v1.00
  ```

---

### STEP 4: Bug Fixing
- **Albert** created a hotfix branch to fix critical bugs in Feature 1:
  ```
  git checkout main
  git pull origin main
  git checkout -b hotfix1
  git add file1_feature1.py
  git commit -m "K: Fixing the bug in file1_feature1.py"
  git push origin hotfix1
  ```
- **Lucas** merged the hotfix into `main` and tagged it as version 1.01:
  ```
  git checkout main
  git merge hotfix -m "L: Merging hotfix to file1_feature1.py"
  git tag -a v1.01 -m "Version 1.01: Hotfix for file1_feature1.py"
  git push origin main
  git push origin v1.01
  ```

---

### STEP 5: Subsequent Development and Second Release (v1.02)

**11. NICK (Feature 2 Continuation)**
- Made further updates to `file1_feature2.py`:
  - Edited the file:
    ```
    nano file1_feature2.py
    ```
  - Staged the changes:
    ```
    git add file1_feature2.py
    ```
  - Committed the update:
    ```
    git commit -m "F2: Additional improvements for feature 2"
    ```
  - Pushed the updated feature to the remote repository:
    ```
    git push origin feature2
    ```

**12. VICTOR (Feature 3 Development)**
- Created and developed Feature 3:
  - Checked out the `develop` branch and created a new feature branch:
    ```
    git checkout develop
    git checkout -b feature3
    ```
  - Created the new file for Feature 3:
    ```
    touch file1_feature3.py
    ```
  - Edited the file to add functionality:
    ```
    nano file1_feature3.py
    ```
  - Staged and committed the changes:
    ```
    git add file1_feature3.py
    git commit -m "X: Adding to feature 3"
    ```
  - Pushed the feature branch to the remote repository:
    ```
    git push origin feature3
    ```

**13. GAEL (Merging Feature 3 into Develop)**
- Merged Feature 3 into `develop`:
  - Ensured that `develop` was up to date:
    ```
    git checkout develop
    git pull origin develop
    ```
  - Merged `feature3` into `develop`:
    ```
    git merge origin/feature3 -m "Merge feature3 into develop"
    ```
  - Pushed the updated `develop` branch to the remote repository:
    ```
    git push origin develop
    ```

**14. LUCAS (Second Release - v1.02)**
- Prepared the second release by merging `develop` into `main`:
  - Checked out the `main` branch and ensured it was up to date:
    ```
    git checkout main
    git pull origin main
    ```
  - Merged the `develop` branch into `main`:
    ```
    git merge develop -m "Release version v1.02"
    ```
  - Tagged the commit to mark the second release:
    ```
    git tag -a v1.02 -m "Version 1.02: Second Release"
    ```
  - Pushed the `main` branch and the tag to the remote repository:
    ```
    git push origin main
    git push origin v1.02
    ```
  - **Note**: During this step, we encountered a small error where commit `X` should have been `Y`, and it appears incorrectly on GitHub. 

---

### STEP 6: Additional Feature (Optional Development)

**11. NICK**
- Continued work on Feature 2 by further enhancing functionality:
  - Edited `file1_feature2.py`:
    ```
    nano file1_feature2.py
    ```
  - Staged and committed the changes:
    ```
    git add file1_feature2.py
    git commit -m "F2: Enhancement and fixes for feature 2"
    ```
  - Pushed the updated feature branch:
    ```
    git push origin feature2
    ```

**12. VICTOR (Feature 3 Development and Testing)**
- Developed Feature 3 and created new functionality in `feature3` branch:
  - Edited `file1_feature3.py`:
    ```
    nano file1_feature3.py
    ```
  - Staged and committed the changes:
    ```
    git add file1_feature3.py
    git commit -m "X: Adding to feature 3 with improved functionality"
    ```
  - Pushed the feature branch to the remote repository:
    ```
    git push origin feature3
    ```

**13. GAEL (Merging Feature 3)**
- Merged Feature 3 into the `develop` branch for integration:
  ```
  git checkout develop
  git merge origin/feature3 -m "Merge feature3 into develop"
  git push origin develop
  ```

**14. LUCAS (Merging Develop to Main)**
- Merged `develop` directly into `main` to prepare the new version:
  - Checked out `main` and merged:
    ```
    git checkout main
    git pull origin main
    git merge develop -m "Release version v1.02"
    ```
  - Tagged the version:
    ```
    git tag -a v1.02 -m "Version 1.02: Second Release"
    git push origin main
    git push origin v1.02
    ```

---

### STEP 7: QA and Final Verification

**15. VICTOR (Advanced Testing and QA)**
- Victor, responsible for QA and final verification, started by cloning the repository to ensure the latest version of all branches and commits:
  ```
  git clone https://github.com/LucasEscayola/A2G07.git
  cd A2-G7
  ```
- Switched to the `main` branch and pulled all tags:
  ```
  git checkout main
  git pull origin main
  git fetch --tags
  ```
- Reviewed the commit history and overall workflow:
  - Used the following commands to check consistency and order:
    ```
    git log
    git log --oneline
    ```
- **Advanced Testing**:
  - Performed advanced testing for conflicts and bugs using the following steps, creating unittests for each feature:
  
  **Unittest for Feature 1**:
  - Created `test_feature1.py` to validate the division function, ensuring proper input handling:
    ```python
    import unittest
    import utils

    class TestUtils(unittest.TestCase):
        def test_division_valid(self):
            self.assertEqual(utils.division(10, 2), 5)
            self.assertEqual(utils.division(-6, 2), -3)

        def test_division_zero_division(self):
            with self.assertRaises(ZeroDivisionError):
                utils.division(10, 0)

        def test_division_invalid_input(self):
            with self.assertRaises(TypeError):
                utils.division("10", 2)
            with self.assertRaises(TypeError):
                utils.division(10, "2")
    ```

  **Unittest for Feature 2**:
  - Created `test_feature2.py` to validate character counting in strings:
    ```python
    import unittest
    import utils

    class TestUtils(unittest.TestCase):
        def test_count_string(self):
            self.assertEqual(utils.count_string("Chicken dinner"), 13)
    ```

  **Unittest for Feature 3**:
  - Created `test_feature3.py` to test additional functionalities added in Feature 3:
    ```python
    import unittest
    import utils

    class TestDivisionValid(unittest.TestCase):
        def test_division_valid(self):
            self.assertEqual(utils.division(10, 2), 5)
            self.assertEqual(utils.division(-6, 2), -3)
    ```

  **Running the Tests**:
  - Ran the unit tests to confirm the validity and integration of all features:
    ```
    python -m unittest test_feature1.py
    python -m unittest test_feature2.py
    python -m unittest test_feature3.py
    ```

Victor ensured that all the tests were successfully completed, confirming that all features were well integrated and the project was ready for final delivery.

## Conclusion
During this project, our team gained practical experience in using Git and GitHub for effective collaborative development. We structured our branch management, implemented features, and tested extensively using `unittest`. We faced challenges such as merge conflicts and branch mismanagement, which we overcame by communicating as a team and following best practices.

We hope that this repository serves as a demonstration of our efforts in applying Git techniques and collaborative workflows to build a well-structured project.
