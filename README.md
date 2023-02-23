# Fetch-SWE

## Description

Fetch users accumulate reward points in their accounts owing to transactions pertaining to certain payers. While the particulars of these transactions are abstracted from the user, the accounting team ensures that these points are spent appropriately in the order of the transaction timestamp.

The Fetch-SWE program is intended to parse and collect data from a csv file containing a list of the before-mentioned transactions. After storing this data within custom user-defined object classes, the code within this repository spends the transaction points according to the following rules dictated by the accounting team:

* The oldest points are spent first (oldest based on transaction timestamp and not the order they’re received) 
* No payer's points can go negative.

After the points are spent, the program will output a dictionary listing the remaining points for each payer in the following format:
```
{
      "payer1": remaining points,
      "payer2": remaining points,
      ...
}
```

## How to use the program?

The project is coded entirely in Python v3.10.7. Before running this program, please ensure that you've downloaded and installed the latest Python version.

If you're using VSCode as your IDE, you can download the necessary Python extensions within VSCode. Otherwise, you can visit [https://www.python.org/downloads/](https://www.python.org/downloads/) to download the latest Python version. Before downloading, make sure to read the available Python versions in order to install the right package corresponding to your machine's OS.

If you've previously downloaded and used Python, please ensure that you're running a version >= 3.10.7 before running this project. You can check the current Python version by running the following command in your terminal:
```
python3 --version
```
If this does not work, you can alternatively run the following command:
```
python --version
```
If you're running a version < 3.10.7., please update Python to the latest version by following the above link and instructions.

Once you've downloaded the latest Python version, you can compile and run the program by typing the following command in your terminal:
```
python3 mycode.py [POINTS] [CSV_FILE_NAME]
```
An alternate way to run the program is:
```
python mycode.py [POINTS] [CSV_FILE_NAME]
```
While running the program, please ensure that you pass positive integers for the points and the input csv file exists in the same working directory as the Python code.
