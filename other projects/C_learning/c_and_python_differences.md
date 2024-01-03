# Topic of research

- comparing C with Python, and vice versa.
- analyse their similarities and differences by comparing source code written in both
- emphasising the syntactical and semantical changes.

# C and Python similarities and differences

## Introduction

- Python:
    - interpreted = much **slower** programs execution
    - high-level
    - general-purpose programming language

- C:
    - compiled = executes programs much **quicker**
    - general-purpose
    - procedural computer programming language

## Ease of use and syntax

Python is much easier to learn as it is a ***high level*** with simplistic syntax:
- Python is a dynamically typed language.
- It has a more concise syntax with dynamic typing; data types are inferred.
- Code blocks are defined by indentation using spaces or tabs (significant whitespace).
- No semicolons ';' are required for statement termination.
- Memory management is automatic (garbage collection).

Whereas C is much more ***low level*** programming language and more complex syntax:
- Statically typed language.
- Uses a more verbose syntax with explicit data type declarations.
- Code blocks are defined with curly braces '{}'.
- Semicolons ';' are used to terminate every statements.
- Indentation is not significant for code blocks; it's used for readability only.
- Memory management is manual (e.g., using 'malloc' and 'free').

## Declaration of variables

- Python:
    - No need to declare the type of variable.
    - Variables are untyped

- C:
    - Type of a variable must be declared when it is created
    - Only values of that type must be assigned to it

## Error Debugging

- Python
    - Error debugging is simple
    - Takes only one in instruction at a time
    - Compiles and executes simultaneously
        - Errors are shown instantly and the execution is stopped

- C
    - Error debugging is difficult
    - Compiler dependent language
        - Takes the entire source code, compiles it and then shows all the errors.

## Function renaming mechanism

- Python
    - Supports function renaming mechanism
        - The same function can be used by two different names.

- C
    - Does not support function renaming mechanism
        - The same function cannot be used by two different names.

---

# comparing source code

## Similarities:

### 1. Variables:

Both C and Python use variables to store data. In both languages, you can declare and assign values to variables.

C
```c
int x = 5;
```
Python
```py
x = 5
```

### 2. Control Structures:

Both languages support common control structures like conditional statements (if-else) and loops (for, while).

C
```c
if (x > 10) {
    // Code here
}
```

Python
```py
if x > 10:
    # Code here
```

### 3. Functions:

Both C and Python allow you to define and use functions for modular code organization.

C
```c
int add(int a, int b) {
    return a + b;
}
```

Python
```py
def add(a, b):
    return a + b
```

## Differences:

### 1. Data Types:

- C requires explicit data type declarations.
    - For example, in C, you must specify that a variable is an integer: 'int x = 5'.

- Python is dynamically typed
    - it infers the data type
        - you don't need to declare it explicitly: 'x = 5'.

### 2. Libraries and Modules:

- C
    - additional functionality is typically provided by including libraries and headers during compilation.

- Python
    - uses modules and libraries, which are imported as needed in the code.

### 3. Performance:

- C
    - is a statically typed language and offers ***finer control over memory and system resources***, making it well-suited for performance-critical applications.

- Python
    - is dynamically typed and has a layer of abstraction that can make it slower than C for certain tasks.

### Significant Whitespace:

C doesn't rely on indentation for code structure; it's used for ***readability only.***

Python enforces code structure through significant ***whitespace***, making indentation a semantically crucial aspect of the language.

---

# Summary

While C and Python share some similarities in basic programming constructs, they differ significantly in ***terms of syntax, data typing, memory management, and their typical use cases.***

The choice between the two depends on the specific requirements of a project, with C being favored for ***performance-critical applications*** and Python for its ***ease of use and rapid development.***