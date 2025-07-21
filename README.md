# Ken McTran -- Exploratory SQL 

## Purposes
    The purpose of this repository  is to implement project 05 for SQL exploration

## Workflow:
    Repeatable workflows include the following:
    1. Follow best-practices for git-update-push to ensure workable code are regularly checked-in into cloud-based Github repository. After this step, do a 'git clone' to clone remote cloud-based GitHub repository into ~/Repos/datafun-05-sql directory
    2. On Mac, change to ~/Repos/datafun-05-sql directory created above. This step create a local .venv directory to install tool into --> 
    ```
    cd ~/Repos/datafun-05-sql      
    python3 -m venv .venv
    ```
    
    3. On Mac, next 2 lines install needed tools (documented in requirements.txt ) into .venv environment
    ```
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install -r requirements.txt
    ```

    4. On Mac, this command would activate the environment
    ```
    source .venv/bin/activate 
    ```

    5. At terminal, use the command:
    ``` 
    code ~/Repos/datafun-05-sql
    ``` 
    to launch VS Code (previously installed on MAC) to open/edit/execute code related to this project.
