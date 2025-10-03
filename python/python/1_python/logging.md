### **create the file**
```python
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Output logs to a file
        logging.StreamHandler()          # Output logs to the console
    ]
)

logger = logging.getLogger(__name__)

@router.get("/user-list-with-all-data/")
def get_user_list(db: Session = Depends(get_db)):
    logger.info("Root endpoint accessed11")
```

### **create the file under the log foler**
```python
# Define the log folder and file name
log_folder = "logs"
log_file_name = "app.log"

# Create the log folder if it doesn't exist
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Create the full path to the log file
log_file_path = os.path.join(log_folder, log_file_name)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),  # Output logs to the specified file
        logging.StreamHandler()              # Output logs to the console
    ]
)

logger = logging.getLogger(__name__)
```

### **create the file under the log foler with date**
```python
# Generate the current date
current_date = datetime.now().strftime("%d_%m_%Y")


log_folder = "logs"
log_file_name = f"app_{current_date}.log"
```


### **log calling in function**
```python
# with all data
@router.get("/user-list-with-all-data/")
def get_user_list(db: Session = Depends(get_db)):
    logger.info("Root endpoint accessed11")
```

### log config in saprate file
```python
project/
│
├── logs/
│   └── app_25_12_2024.log
│
├── logger_config.py
├── main.py

create the logger_config.py file 
and put the code

# and call main.py file
from logger_config import logger

def main():
    # Example log messages
    logger.info("This is an info message from main.py")
    logger.error("This is an error message from main.py")
```

### **saprate file for log and call in main.py file.**
```python
# Create the logger_config.php and put the code
#-----------------------------------------------
import os
import logging
from datetime import datetime

def configure_logging():
    # Generate the current date
    current_date = datetime.now().strftime("%d_%m_%Y")

    # Define the log folder and file name
    log_folder = "logs"
    log_file_name = f"app_{current_date}.log"

    # Create the log folder if it doesn't exist
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)

    # Create the full path to the log file
    log_file_path = os.path.join(log_folder, log_file_name)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),  # Output logs to the specified file
            logging.StreamHandler()              # Output logs to the console
        ]
    )

# Call the function to configure logging
configure_logging()

# Get the logger
logger = logging.getLogger(__name__)

# call in main.py/route file
#__________________________

from logger_config import logger

@router.get("/user-list-with-all-data/")
def get_user_list(db: Session = Depends(get_db)):
    logger.info("Root endpoint accessed11")

```

### **using package**
* refrence:-   https://loguru.readthedocs.io/en/stable/overview.html
* install package
```python
pip install loguru
```